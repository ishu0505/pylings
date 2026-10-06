# 06 Test-Driven Development (TDD)

TDD is the engineering discipline that separates hobby scripts from production systems.

### The Loop: Red → Green → Refactor
1. **Red:** Write a failing test for the next smallest piece of behavior.
2. **Green:** Write the simplest possible code to make the test pass.
3. **Refactor:** Clean up duplication, improve names, optimize algorithms with confidence that the tests catch regressions.

### Mutation Testing: Who Tests the Tests?
In `pylings` TDD-mode exercises, you write the tests against a working implementation. pylings then injects realistic bugs ("mutants") into the code. If your tests still pass when a bug is present, the mutant *slipped through*. A test suite only passes when it kills every mutant!
