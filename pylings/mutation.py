"""Mutation runner for TDD-mode exercises.

Usage: python -m pylings.mutation <exercise.py> <mutants.py> [target]

Loads the learner's exercise file, collects every zero-argument `test_*`
function, then swaps the target function/class for each buggy "mutant" and
re-runs the tests. A mutant is "killed" if at least one test fails on it.
Prints a single line `PYLINGS_JSON:{...}` with the report.
"""

from __future__ import annotations

import contextlib
import importlib.util
import inspect
import io
import json
import sys


def _load(path: str, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise ImportError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def main() -> None:
    exercise_path, mutants_path = sys.argv[1], sys.argv[2]
    target = sys.argv[3] if len(sys.argv) > 3 and sys.argv[3] else None

    with contextlib.redirect_stdout(io.StringIO()):
        module = _load(exercise_path, "pylings_exercise_under_test")
        mutants = _load(mutants_path, "pylings_mutants")

    target = target or getattr(mutants, "TARGET")
    tests = []
    bad_signature = []
    for name, obj in list(vars(module).items()):
        if name.startswith("test_") and callable(obj):
            if inspect.signature(obj).parameters:
                bad_signature.append(name)
            else:
                tests.append((name, obj))

    original = getattr(module, target)
    results = []
    for mutant_name, mutant in mutants.MUTANTS.items():
        setattr(module, target, mutant)
        killed_by = None
        for test_name, test in tests:
            try:
                with contextlib.redirect_stdout(io.StringIO()):
                    test()
            except BaseException as e:
                if isinstance(e, (KeyboardInterrupt, SystemExit)):
                    raise
                killed_by = test_name
                break
        results.append({"name": mutant_name, "killed": killed_by is not None, "by": killed_by})
    setattr(module, target, original)

    report = {"tests": len(tests), "bad_signature": bad_signature, "mutants": results}
    print("PYLINGS_JSON:" + json.dumps(report))


if __name__ == "__main__":
    main()
