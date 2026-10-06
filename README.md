# pylings 🐍

Small exercises to get you **job-ready in Python fast**, in the style of [rustlings](https://github.com/rust-lang/rustlings),
and set up so an AI mentor (Claude Code, Codex, or Antigravity) can teach you and keep track of your progress.

**What you'll practise:** Pythonic code → OOP → TDD → DSA / NeetCode patterns → async → FastAPI →
SQS/SNS workers → AI-backend patterns (streaming, retries, rate limits, structured LLM output).

## Quick start

```bash
uv sync                 # install deps (Python 3.12+)
uv run pylings          # watch mode: edit the current exercise, save, see the tests run
```

How it works:
1. Open the file watch mode shows you (e.g. `exercises/00_intro/intro1.py`).
2. Make the tests at the bottom of the file pass: **Red → Green → Refactor**.
3. Delete the `# I AM NOT DONE` line. pylings moves you on to the next exercise.

## Commands

| Command | What it does |
|---|---|
| `uv run pylings` | Watch mode (type `h` / `l` / `p` / `r` / `q` + Enter) |
| `uv run pylings list` | All exercises with status |
| `uv run pylings run [name]` | Run one exercise |
| `uv run pylings hint [name]` | Next progressive hint (`--all` shows every hint) |
| `uv run pylings progress` | Progress bars per track |
| `uv run pylings focus fastapi` | Work on one track first (`--clear` to undo) |
| `uv run pylings skip <name or track>` | Skip things you already know |
| `uv run pylings reset <name>` | Restore an exercise to its original version (to re-solve it later for review) |
| `uv run pylings solution <name>` | Reference solution (once you've finished) |
| `uv run pylings status --json` | Machine-readable progress for AI agents |
| `uv run pylings verify` | Re-check everything and refresh `PROGRESSION.md` |

## Exercise modes

- **test**: fix or implement code until the tests you're given pass.
- **tdd**: the code already works and **you write the tests**. pylings then plants realistic bugs
  ("mutants") in the code, and your tests have to catch every one of them. This is how you learn to write tests that actually protect code.

## Using an AI mentor

Open Claude Code / Codex / Antigravity in this folder. They read [`AGENTS.md`](AGENTS.md) (Claude reads it via `CLAUDE.md`).
Then say things like:

- **"check and correct"**: reviews your current exercise, runs the tests, explains what went wrong with an analogy, and updates `PROGRESSION.md`
- **"teach me the current topic"**: a short lesson before you start
- **"diagnostic"**: works out your level and skips topics you've already mastered
- **"new exercise on sliding window"**: generates more practice in the same format
- **"mock interview"**: a timed NeetCode-style question
- **"review"**: spaced repetition of problems you've already solved

Claude Code slash commands: `/check`, `/teach`, `/diagnostic`, `/new-exercise`, `/interview`, `/review`.

## Layout

```
exercises/<NN_track>/   info.toml (order + hints), README.md (notes), *.py exercises
solutions/<NN_track>/   reference solutions
mutants/<NN_track>/     planted bugs for TDD-mode exercises
PROGRESSION.md          your mastery tracker (the mentor writes notes, pylings writes the auto block)
docs/EXERCISE_FORMAT.md how to write new exercises
```
