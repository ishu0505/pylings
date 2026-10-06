"""pylings CLI — rustlings, but for industry Python.

Commands (run with `uv run pylings <command>`):
  watch (default)   Re-run the current exercise every time you save it.
  list              Show every exercise and its status.
  run [name]        Run one exercise (default: current).
  hint [name]       Reveal the next progressive hint (--all for every hint).
  next              Show the current exercise and where it lives.
  progress          Per-track progress bars.
  status --json     Machine-readable progress (for Claude Code / Codex).
  verify            Re-check every exercise and refresh progress.
  focus <track>     Work on one track first (e.g. `focus fastapi`). --clear to undo.
  skip <name|track> Mark as skipped (already mastered). `unskip` undoes.
  reset <name>      Restore an exercise to its original version (via git).
  solution <name>   Print the reference solution (only after you finish, or --force).
  sync              Regenerate the auto block in PROGRESSION.md.
  check-solutions   (maintainers) exercises fail as shipped, solutions pass.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import queue
import subprocess
import sys
import threading
import time
import tomllib
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass, field
from pathlib import Path

MARKER = "# I AM NOT DONE"
AUTO_START = "<!-- pylings:auto:start -->"
AUTO_END = "<!-- pylings:auto:end -->"
TIMEOUT_S = 60


# --------------------------------------------------------------------------- paths
def find_root() -> Path:
    env = os.environ.get("PYLINGS_ROOT")
    if env:
        return Path(env).resolve()
    here = Path.cwd().resolve()
    for p in [here, *here.parents]:
        if (p / "exercises").is_dir() and (p / "pyproject.toml").exists():
            return p
    return Path(__file__).resolve().parent.parent


ROOT = find_root()
EXERCISES = ROOT / "exercises"
SOLUTIONS = ROOT / "solutions"
MUTANTS = ROOT / "mutants"
STATE_FILE = ROOT / ".pylings-state.json"
PROGRESSION = ROOT / "PROGRESSION.md"


# --------------------------------------------------------------------------- colors
def _c(code: str):
    def paint(s: str) -> str:
        if os.environ.get("NO_COLOR") or not sys.stdout.isatty():
            return s
        return f"\033[{code}m{s}\033[0m"

    return paint


GREEN, RED, YELLOW, CYAN, DIM, BOLD = (_c(x) for x in ("32", "31", "33", "36", "2", "1"))
DIFF_COLOR = {"easy": GREEN, "medium": YELLOW, "hard": RED}


# --------------------------------------------------------------------------- model
@dataclass
class Exercise:
    name: str
    title: str
    track: str
    track_title: str
    difficulty: str = "easy"
    mode: str = "test"  # "test" or "tdd"
    hints: list[str] = field(default_factory=list)
    tags: list[str] = field(default_factory=list)
    target: str | None = None
    min_tests: int = 3
    ships_passing: bool = False

    @property
    def path(self) -> Path:
        return EXERCISES / self.track / f"{self.name}.py"

    @property
    def solution(self) -> Path:
        return SOLUTIONS / self.track / f"{self.name}.py"

    @property
    def mutants(self) -> Path:
        return MUTANTS / self.track / f"{self.name}.py"

    @property
    def rel(self) -> str:
        return str(self.path.relative_to(ROOT))

    def has_marker(self, path: Path | None = None) -> bool:
        try:
            text = (path or self.path).read_text()
        except FileNotFoundError:
            return False
        return any(line.strip() == MARKER for line in text.splitlines())


@dataclass
class RunResult:
    passed: bool
    output: str


def load_exercises() -> list[Exercise]:
    exercises: list[Exercise] = []
    seen: set[str] = set()
    if not EXERCISES.is_dir():
        sys.exit(f"No exercises/ directory found under {ROOT}")
    for track_dir in sorted(p for p in EXERCISES.iterdir() if p.is_dir()):
        info = track_dir / "info.toml"
        if not info.exists():
            continue
        data = tomllib.loads(info.read_text())
        track_title = data.get("title", track_dir.name)
        for raw in data.get("exercises", []):
            name = raw["name"]
            if name in seen:
                sys.exit(f"Duplicate exercise name '{name}' in {info}")
            seen.add(name)
            exercises.append(
                Exercise(
                    name=name,
                    title=raw.get("title", name),
                    track=track_dir.name,
                    track_title=track_title,
                    difficulty=raw.get("difficulty", "easy"),
                    mode=raw.get("mode", "test"),
                    hints=list(raw.get("hints", [])),
                    tags=list(raw.get("tags", [])),
                    target=raw.get("target"),
                    min_tests=int(raw.get("min_tests", 3)),
                    ships_passing=bool(raw.get("ships_passing", False)),
                )
            )
    return exercises


def tracks_of(exercises: list[Exercise]) -> list[str]:
    out: list[str] = []
    for e in exercises:
        if e.track not in out:
            out.append(e.track)
    return out


def resolve_track(arg: str, exercises: list[Exercise]) -> str | None:
    for t in tracks_of(exercises):
        short = t.split("_", 1)[-1]
        if arg in (t, short) or t.startswith(arg + "_"):
            return t
    return None


def find_exercise(name: str, exercises: list[Exercise]) -> Exercise:
    for e in exercises:
        if e.name == name:
            return e
    close = [e.name for e in exercises if name in e.name]
    hint = f" Did you mean: {', '.join(close[:5])}?" if close else ""
    sys.exit(f"Unknown exercise '{name}'.{hint}")


# --------------------------------------------------------------------------- state
def now() -> str:
    return dt.datetime.now().isoformat(timespec="seconds")


def load_state() -> dict:
    data = json.loads(STATE_FILE.read_text()) if STATE_FILE.exists() else {}
    for key in ("done", "skipped", "attempts", "hints_used"):
        data.setdefault(key, {})
    data.setdefault("focus", None)
    return data


def save_state(state: dict) -> None:
    STATE_FILE.write_text(json.dumps(state, indent=2, sort_keys=True) + "\n")


def pending(exercises: list[Exercise], state: dict) -> list[Exercise]:
    return [e for e in exercises if e.name not in state["done"] and e.name not in state["skipped"]]


def current_exercise(exercises: list[Exercise], state: dict) -> Exercise | None:
    todo = pending(exercises, state)
    if state.get("focus"):
        focused = [e for e in todo if e.track == state["focus"]]
        if focused:
            return focused[0]
    return todo[0] if todo else None


def pick(name: str | None, exercises: list[Exercise], state: dict) -> Exercise:
    if name:
        return find_exercise(name, exercises)
    cur = current_exercise(exercises, state)
    if cur is None:
        sys.exit(GREEN("🎉 Every exercise is done or skipped!"))
    return cur


# --------------------------------------------------------------------------- running
def _env() -> dict:
    env = dict(os.environ)
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    env.setdefault("AWS_DEFAULT_REGION", "us-east-1")
    env.setdefault("AWS_ACCESS_KEY_ID", "testing")
    env.setdefault("AWS_SECRET_ACCESS_KEY", "testing")
    return env


def _run(cmd: list[str]) -> tuple[int, str]:
    try:
        p = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True, timeout=TIMEOUT_S, env=_env())
        return p.returncode, (p.stdout + p.stderr).rstrip()
    except subprocess.TimeoutExpired:
        return -1, RED(f"⏱  Timed out after {TIMEOUT_S}s — is there an infinite loop?")


def _pytest(path: Path) -> tuple[int, str]:
    return _run(
        [
            sys.executable, "-m", "pytest", str(path),
            "-q", "--no-header", "--tb=short", "-p", "no:cacheprovider", "--import-mode=importlib",
        ]
    )


def _mutation(ex: Exercise, path: Path) -> tuple[bool, str]:
    if not ex.mutants.exists():
        return False, RED(f"Missing mutants file {ex.mutants.relative_to(ROOT)}")
    code, out = _run([sys.executable, "-m", "pylings.mutation", str(path), str(ex.mutants), ex.target or ""])
    line = next((l for l in out.splitlines() if l.startswith("PYLINGS_JSON:")), None)
    if line is None:
        return False, RED("Mutation runner crashed:\n") + out
    report = json.loads(line.removeprefix("PYLINGS_JSON:"))
    ok = True
    lines = [BOLD("\n🧬 Mutation check — can your tests catch planted bugs?")]
    if report["bad_signature"]:
        ok = False
        lines.append(RED(f"  ✘ Tests must take no arguments (no fixtures): {', '.join(report['bad_signature'])}"))
    if report["tests"] < ex.min_tests:
        ok = False
        lines.append(RED(f"  ✘ Found {report['tests']} test(s); write at least {ex.min_tests}."))
    for m in report["mutants"]:
        if m["killed"]:
            lines.append(GREEN(f"  ✔ caught: {m['name']}") + DIM(f"  (by {m['by']})"))
        else:
            ok = False
            lines.append(RED(f"  ✘ slipped through: {m['name']}"))
    return ok, "\n".join(lines)


def run_file(ex: Exercise, path: Path) -> RunResult:
    code, out = _pytest(path)
    tests_ok = code == 0
    if code == 5:
        out += "\n" + YELLOW("No tests were collected.")
    if ex.mode == "tdd":
        mut_ok, mut_out = _mutation(ex, path)
        return RunResult(tests_ok and mut_ok, out + "\n" + mut_out)
    return RunResult(tests_ok, out)


def run_and_record(ex: Exercise, state: dict) -> RunResult:
    result = run_file(ex, ex.path)
    if ex.name not in state["done"]:
        state["attempts"][ex.name] = state["attempts"].get(ex.name, 0) + 1
    if result.passed and not ex.has_marker():
        if ex.name not in state["done"]:
            state["done"][ex.name] = {
                "completed_at": now(),
                "attempts": state["attempts"].get(ex.name, 1),
                "hints_used": state["hints_used"].get(ex.name, 0),
            }
            save_state(state)
            sync_progression(load_exercises(), state)
    save_state(state)
    return result


# --------------------------------------------------------------------------- display
def bar(done: int, total: int, width: int = 24) -> str:
    filled = int(width * done / total) if total else width
    return GREEN("█" * filled) + DIM("░" * (width - filled))


def header(ex: Exercise) -> str:
    diff = DIFF_COLOR.get(ex.difficulty, str)(ex.difficulty)
    mode = CYAN(" [TDD: you write the tests]") if ex.mode == "tdd" else ""
    return f"{BOLD(ex.name)} — {ex.title}  ({diff}){mode}\n{DIM(ex.track_title)} · {CYAN(ex.rel)}"


def verdict(ex: Exercise, result: RunResult) -> str:
    if result.passed and ex.has_marker():
        return GREEN("✅ Tests pass! ") + f"Review your code, then delete the line `{MARKER}` to move on."
    if result.passed:
        return GREEN(f"✅ {ex.name} complete!")
    return RED(f"✘ {ex.name} isn't passing yet.") + f" Edit {CYAN(ex.rel)}  ·  stuck? `pylings hint {ex.name}`"


def print_list(exercises: list[Exercise], state: dict) -> None:
    cur = current_exercise(exercises, state)
    track = None
    for e in exercises:
        if e.track != track:
            track = e.track
            print("\n" + BOLD(f"{e.track}  {e.track_title}"))
        if e.name in state["done"]:
            mark = GREEN("✔")
        elif e.name in state["skipped"]:
            mark = DIM("⤼")
        elif cur and e.name == cur.name:
            mark = YELLOW("▶")
        else:
            mark = DIM("·")
        diff = DIFF_COLOR.get(e.difficulty, str)(f"{e.difficulty:<6}")
        tdd = CYAN(" tdd") if e.mode == "tdd" else ""
        print(f"  {mark} {e.name:<22} {diff} {e.title}{tdd}")


def print_progress(exercises: list[Exercise], state: dict) -> None:
    total = len(exercises)
    done = sum(1 for e in exercises if e.name in state["done"])
    skipped = sum(1 for e in exercises if e.name in state["skipped"])
    print(BOLD(f"Overall  {bar(done + skipped, total)}  {done} done, {skipped} skipped / {total}\n"))
    for t in tracks_of(exercises):
        items = [e for e in exercises if e.track == t]
        d = sum(1 for e in items if e.name in state["done"] or e.name in state["skipped"])
        print(f"  {t:<22} {bar(d, len(items), 16)} {d}/{len(items)}")
    cur = current_exercise(exercises, state)
    if cur:
        print("\nNext up: " + header(cur))
    if state.get("focus"):
        print(DIM(f"(focus: {state['focus']})"))


# --------------------------------------------------------------------------- PROGRESSION.md
def sync_progression(exercises: list[Exercise], state: dict) -> None:
    total = len(exercises)
    done = sum(1 for e in exercises if e.name in state["done"])
    cur = current_exercise(exercises, state)
    lines = [
        AUTO_START,
        "_Auto-generated by `pylings` (run `uv run pylings sync`). Do not edit inside this block._",
        "",
        f"- **Updated:** {now()}",
        f"- **Exercises done:** {done}/{total} (skipped: {len(state['skipped'])})",
        f"- **Current exercise:** `{cur.name}` — {cur.title} ({cur.track})" if cur else "- **Current exercise:** all done 🎉",
        f"- **Focus track:** {state['focus']}" if state.get("focus") else "- **Focus track:** none (linear order)",
        "",
        "| Track | Done | Progress |",
        "|---|---|---|",
    ]
    for t in tracks_of(exercises):
        items = [e for e in exercises if e.track == t]
        d = sum(1 for e in items if e.name in state["done"])
        s = sum(1 for e in items if e.name in state["skipped"])
        pct = int(100 * (d + s) / len(items)) if items else 0
        extra = f" (+{s} skipped)" if s else ""
        lines.append(f"| {t} | {d}/{len(items)}{extra} | {pct}% |")
    recent = sorted(state["done"].items(), key=lambda kv: kv[1].get("completed_at", ""), reverse=True)[:8]
    if recent:
        lines += ["", "**Recently completed** (attempts = test runs before passing, hints = hints revealed):", ""]
        lines += ["| Exercise | Completed | Attempts | Hints |", "|---|---|---|---|"]
        for name, info in recent:
            lines.append(
                f"| {name} | {info.get('completed_at', '')} | {info.get('attempts', '?')} | {info.get('hints_used', 0)} |"
            )
    lines.append(AUTO_END)
    block = "\n".join(lines)

    text = PROGRESSION.read_text() if PROGRESSION.exists() else "# Coding Mastery Tracker\n"
    if AUTO_START in text and AUTO_END in text:
        before, rest = text.split(AUTO_START, 1)
        _, after = rest.split(AUTO_END, 1)
        text = before + block + after
    else:
        text = text.rstrip() + "\n\n## pylings Auto Progress\n" + block + "\n"
    PROGRESSION.write_text(text)


# --------------------------------------------------------------------------- commands
def cmd_list(args, exercises, state):
    print_list(exercises, state)


def cmd_progress(args, exercises, state):
    print_progress(exercises, state)


def cmd_next(args, exercises, state):
    ex = pick(None, exercises, state)
    print(header(ex))
    print(DIM("\nOpen the file, read the docstring, make the tests pass. `uv run pylings` watches for saves."))


def cmd_run(args, exercises, state):
    ex = pick(args.name, exercises, state)
    print(header(ex) + "\n")
    result = run_and_record(ex, state)
    print(result.output)
    print("\n" + verdict(ex, result))
    sys.exit(0 if result.passed else 1)


def cmd_hint(args, exercises, state):
    ex = pick(args.name, exercises, state)
    if not ex.hints:
        print(YELLOW("No hints for this one — ask your mentor (Claude Code / Codex): 'give me a hint'."))
        return
    used = state["hints_used"].get(ex.name, 0)
    level = len(ex.hints) if args.all else min(used + 1, len(ex.hints))
    print(header(ex) + "\n")
    labels = ["Hint 1 (Approach)", "Hint 2 (Optimization / Edge cases)", "Hint 3 (Almost there)"]
    for i in range(level):
        label = labels[i] if i < len(labels) else f"Hint {i + 1}"
        print(YELLOW(f"💡 {label}: ") + ex.hints[i])
    if level < len(ex.hints):
        print(DIM(f"\n({level}/{len(ex.hints)} hints shown — run again for the next one)"))
    state["hints_used"][ex.name] = max(used, level)
    save_state(state)


def cmd_status(args, exercises, state):
    cur = current_exercise(exercises, state)
    data = {
        "root": str(ROOT),
        "current": cur.name if cur else None,
        "current_path": cur.rel if cur else None,
        "focus": state.get("focus"),
        "done": len(state["done"]),
        "skipped": len(state["skipped"]),
        "total": len(exercises),
        "exercises": [
            {
                "name": e.name,
                "title": e.title,
                "track": e.track,
                "difficulty": e.difficulty,
                "mode": e.mode,
                "tags": e.tags,
                "path": e.rel,
                "status": "done" if e.name in state["done"] else "skipped" if e.name in state["skipped"] else "pending",
                "attempts": state["attempts"].get(e.name, 0),
                "hints_used": state["hints_used"].get(e.name, 0),
                "completed_at": state["done"].get(e.name, {}).get("completed_at"),
            }
            for e in exercises
        ],
    }
    if args.json:
        print(json.dumps(data, indent=2))
    else:
        print_progress(exercises, state)


def cmd_verify(args, exercises, state):
    targets = exercises
    if args.track:
        t = resolve_track(args.track, exercises) or sys.exit(f"Unknown track {args.track}")
        targets = [e for e in exercises if e.track == t]
    targets = [e for e in targets if e.name not in state["skipped"]]
    with ThreadPoolExecutor(max_workers=os.cpu_count() or 4) as pool:
        results = list(pool.map(lambda e: (e, run_file(e, e.path)), targets))
    passed = 0
    for ex, res in results:
        complete = res.passed and not ex.has_marker()
        if complete:
            passed += 1
            state["done"].setdefault(ex.name, {"completed_at": now(), "attempts": state["attempts"].get(ex.name, 1)})
            print(GREEN("  ✔ ") + ex.name)
        else:
            state["done"].pop(ex.name, None)
            why = "marker still present" if res.passed else "failing"
            print(DIM(f"  · {ex.name} ({why})"))
    save_state(state)
    sync_progression(exercises, state)
    print(f"\n{passed}/{len(targets)} complete.")


def cmd_focus(args, exercises, state):
    if args.clear or not args.track:
        state["focus"] = None
        print("Focus cleared — back to linear order.")
    else:
        t = resolve_track(args.track, exercises)
        if not t:
            sys.exit(f"Unknown track '{args.track}'. Tracks: {', '.join(tracks_of(exercises))}")
        state["focus"] = t
        print(f"Focusing on {BOLD(t)}.")
    save_state(state)
    sync_progression(exercises, state)


def _names_for(arg: str, exercises: list[Exercise]) -> list[str]:
    t = resolve_track(arg, exercises)
    if t:
        return [e.name for e in exercises if e.track == t]
    return [find_exercise(arg, exercises).name]


def cmd_skip(args, exercises, state):
    for n in _names_for(args.target, exercises):
        if n not in state["done"]:
            state["skipped"][n] = now()
            print(DIM(f"skipped {n}"))
    save_state(state)
    sync_progression(exercises, state)


def cmd_unskip(args, exercises, state):
    for n in _names_for(args.target, exercises):
        if state["skipped"].pop(n, None):
            print(f"unskipped {n}")
    save_state(state)
    sync_progression(exercises, state)


def cmd_reset(args, exercises, state):
    ex = find_exercise(args.name, exercises)
    added = subprocess.run(
        ["git", "log", "--diff-filter=A", "--format=%H", "--", ex.rel],
        cwd=ROOT, capture_output=True, text=True,
    ).stdout.split()
    if not added:
        sys.exit("Can't reset: this exercise isn't committed to git yet.")
    original = subprocess.run(
        ["git", "show", f"{added[-1]}:{ex.rel}"], cwd=ROOT, capture_output=True, text=True, check=True
    ).stdout
    ex.path.write_text(original)
    state["done"].pop(ex.name, None)
    state["attempts"].pop(ex.name, None)
    state["hints_used"].pop(ex.name, None)
    save_state(state)
    sync_progression(exercises, state)
    print(f"Reset {ex.rel} to its original version. Fresh start — good for spaced review!")


def cmd_solution(args, exercises, state):
    ex = find_exercise(args.name, exercises)
    if ex.name not in state["done"] and not args.force:
        sys.exit(YELLOW("Finish the exercise first (or use --force). Struggling is where learning happens!"))
    if not ex.solution.exists():
        sys.exit("No reference solution for this exercise.")
    print(ex.solution.read_text())


def cmd_sync(args, exercises, state):
    sync_progression(exercises, state)
    print(f"Updated {PROGRESSION.relative_to(ROOT)}")


def cmd_check_solutions(args, exercises, state):
    targets = exercises
    if args.track:
        t = resolve_track(args.track, exercises) or sys.exit(f"Unknown track {args.track}")
        targets = [e for e in exercises if e.track == t]

    def check(ex: Exercise) -> list[str]:
        problems = []
        if not ex.path.exists():
            return [f"missing exercise file {ex.rel}"]
        if not ex.has_marker():
            problems.append("exercise is missing the I AM NOT DONE marker")
        if not ex.ships_passing and run_file(ex, ex.path).passed:
            problems.append("exercise passes as shipped (it should fail until solved)")
        if not ex.solution.exists():
            problems.append("missing solution file")
        else:
            if ex.has_marker(ex.solution):
                problems.append("solution still contains the marker")
            res = run_file(ex, ex.solution)
            if not res.passed:
                problems.append("solution FAILS:\n" + res.output)
        if len(ex.hints) < 2:
            problems.append("needs at least 2 hints")
        return problems

    with ThreadPoolExecutor(max_workers=os.cpu_count() or 4) as pool:
        results = list(pool.map(lambda e: (e, check(e)), targets))
    bad = 0
    for ex, problems in results:
        if problems:
            bad += 1
            print(RED(f"✘ {ex.name}"))
            for p in problems:
                print("    " + p.replace("\n", "\n    "))
        else:
            print(GREEN(f"✔ {ex.name}"))
    print(f"\n{len(results) - bad}/{len(results)} OK")
    sys.exit(1 if bad else 0)


# --------------------------------------------------------------------------- watch
def cmd_watch(args, exercises, state):
    commands: queue.Queue[str] = queue.Queue()

    def reader():
        for line in sys.stdin:
            commands.put(line.strip().lower())

    threading.Thread(target=reader, daemon=True).start()
    footer = DIM("\n[h]int  [l]ist  [p]rogress  [r]erun  [q]uit   (type a letter + Enter)")
    current: Exercise | None = None
    last_mtime: float | None = None
    last_screen = ""

    while True:
        exercises = load_exercises()
        state = load_state()
        nxt = current_exercise(exercises, state)
        if nxt is None:
            print(GREEN(BOLD("\n🎉 All exercises done! Ask your mentor for a mock interview or new exercises.")))
            return
        if current is None or nxt.name != current.name:
            current, last_mtime = nxt, None
        mtime = current.path.stat().st_mtime
        if mtime != last_mtime:
            last_mtime = mtime
            result = run_and_record(current, state)
            done = len(state["done"]) + len(state["skipped"])
            last_screen = "\n".join(
                [
                    f"{bar(done, len(exercises))} {done}/{len(exercises)}",
                    "",
                    header(current),
                    "",
                    result.output,
                    "",
                    verdict(current, result),
                    footer,
                ]
            )
            print("\033[2J\033[H" + last_screen, flush=True)
            if result.passed and not current.has_marker():
                time.sleep(1.5)
                continue
        try:
            cmd = commands.get(timeout=0.4)
        except queue.Empty:
            continue
        if cmd in ("q", "quit", "exit"):
            return
        if cmd in ("h", "hint"):
            cmd_hint(argparse.Namespace(name=current.name, all=False), exercises, state)
        elif cmd in ("l", "list"):
            print_list(exercises, state)
        elif cmd in ("p", "progress"):
            print_progress(exercises, state)
        elif cmd in ("r", "rerun"):
            last_mtime = None
        print(footer)


# --------------------------------------------------------------------------- main
def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(prog="pylings", description="Rustlings-style Python exercises.")
    sub = parser.add_subparsers(dest="command")

    sub.add_parser("watch", help="re-run the current exercise on every save (default)")
    sub.add_parser("list", help="list all exercises")
    sub.add_parser("progress", help="progress bars per track")
    sub.add_parser("next", help="show the current exercise")
    p = sub.add_parser("run", help="run an exercise")
    p.add_argument("name", nargs="?")
    p = sub.add_parser("hint", help="reveal the next hint")
    p.add_argument("name", nargs="?")
    p.add_argument("--all", action="store_true")
    p = sub.add_parser("status", help="progress summary (use --json for agents)")
    p.add_argument("--json", action="store_true")
    p = sub.add_parser("verify", help="re-check all exercises")
    p.add_argument("--track")
    p = sub.add_parser("focus", help="prioritise a track")
    p.add_argument("track", nargs="?")
    p.add_argument("--clear", action="store_true")
    p = sub.add_parser("skip", help="skip an exercise or a whole track")
    p.add_argument("target")
    p = sub.add_parser("unskip", help="undo skip")
    p.add_argument("target")
    p = sub.add_parser("reset", help="restore an exercise to its original version")
    p.add_argument("name")
    p = sub.add_parser("solution", help="show the reference solution")
    p.add_argument("name")
    p.add_argument("--force", action="store_true")
    sub.add_parser("sync", help="refresh the auto block in PROGRESSION.md")
    p = sub.add_parser("check-solutions", help="maintainers: validate exercises + solutions")
    p.add_argument("--track")

    args = parser.parse_args(argv)
    handlers = {
        None: cmd_watch, "watch": cmd_watch, "list": cmd_list, "progress": cmd_progress, "next": cmd_next,
        "run": cmd_run, "hint": cmd_hint, "status": cmd_status, "verify": cmd_verify, "focus": cmd_focus,
        "skip": cmd_skip, "unskip": cmd_unskip, "reset": cmd_reset, "solution": cmd_solution,
        "sync": cmd_sync, "check-solutions": cmd_check_solutions,
    }
    try:
        handlers[args.command](args, load_exercises(), load_state())
    except KeyboardInterrupt:
        print()


if __name__ == "__main__":
    main()
