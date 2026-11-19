# TDD shopping cart instructions

Follow test-driven development strictly.

- Tests are normally executed with `uv run pytest`.
- On this Windows ARM64 machine, the pytest launcher may be blocked by Application Control. Do not change security settings.
- The code of `src/ostos.py` and `src/tuote.py` must never be changed.
- Tests must not be edited unless explicitly asked.
- Always implement absolutely minimal code that makes the current tests pass.
- Do not implement future requirements based on comments or guesses.
- Work on only one numbered TDD step at a time.
- Never weaken or remove assertions to make tests pass.
- Do not commit or push unless explicitly asked.
- Explain which production-code lines you changed and why.

For steps 1-7, the human writes the test first. You may only modify the implementation in `src/ostoskori.py`.

For steps 8-12, write one requested test first, verify that it fails, and only then implement the minimum code to pass it.

For steps 13-15, follow the same red-green-refactor cycle.