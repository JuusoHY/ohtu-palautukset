# TDD shopping cart: work review (draft)

This draft is based on the committed implementation, tests, and observed test runs. It does not describe personal learning or feelings; the user should add those if the course reflection requires them.

## Implementation quality

The cart stores one `Ostos` per product object and updates its quantity for repeated additions. Item count and price are calculated from those entries, avoiding duplicated cached totals that could drift out of sync. Removing the last item removes its `Ostos`; `tyhjenna()` clears the entries.

The implementation treats repeated additions as the same product when they use the same `Tuote` instance. The tests do not establish whether separate `Tuote` instances with identical names should be treated as the same product; confirm that interpretation against the course requirements if relevant.

## Test quality

The suite contains 15 tests, including the initial empty-cart test. Each step's test focuses on its requested behavior and uses the existing `Tuote` and `Ostos` interfaces. The agent-written tests use the shared `Tuote` import and directly assert the requested values.

The human-written snippets for steps 2-7 were appended exactly as provided. They include local `Tuote` imports even though the test module already imports `Tuote`; this redundancy was preserved as requested. The tests cover the listed add, aggregate, remove, and clear scenarios, but do not cover every edge case, such as removing a product not in the cart or repeated removal after it reaches zero.

## TDD process and minimal changes

- Steps 2 and 3 each had a failing test before the implementation change and passed afterward.
- Step 4 was already green before any production change. At the user's direction, its test-only change was committed and the missing RED phase is recorded rather than fabricated.
- Steps 5-7 were already green with the implementation from earlier steps, so they were committed as test-only changes.
- Step 8 had a RED/GREEN cycle. Steps 9-10 were already green after step 8 and required no extra production changes.
- Steps 11-15 each had a RED/GREEN cycle.
- Production changes were limited to the behavior required by each step. No expected product names, prices, or quantities were hardcoded in production code. Zero values in the initial-cart behavior are the required empty-state result, not a test-specific product case.
- After step 15, a separate refactor removed cached count and price fields and derives both from the `Ostos` entries. The full test suite passed after this behavior-preserving refactor.

## Human-written and agent-written tests

Steps 2-7 came from user-authored snippets and were not altered. Steps 8-15 were written by the agent from the supplied requirements. The agent-written tests use the same `unittest` structure and Finnish step-based method names, but rely on the module-level `Tuote` import rather than repeating local imports. Review whether their naming and edge-case coverage match the course's preferred style.

## Personal review to complete

Please add your own assessment of how AI assistance affected your TDD process and learning. In particular, judge whether the agent-written tests reflect your intended test design, whether the already-green steps were handled appropriately for the course, and whether the implementation meets any requirements not expressed by these tests.
