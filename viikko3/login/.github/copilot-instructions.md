# Copilot instructions for this repository

## Project overview
This repository contains a small Flask application for a login and registration flow. The app is intentionally simple and mostly server-side: routes in `src/app.py` render templates and call the service layer, while the in-memory repository stores users for the lifetime of the process.

The most important moving parts are:
- `src/index.py`: starts the Flask app on `127.0.0.1:5001`
- `src/app.py`: routes, form handling, redirects, and flash-based error messages
- `src/services/user_service.py`: domain logic for credential checks and validation
- `src/repositories/user_repository.py`: in-memory user storage and uniqueness checks
- `src/entities/user.py`: plain user model
- `src/templates/*.html`: Jinja templates for the login, registration, and landing pages
- `src/tests/*.robot`: Robot Framework browser tests for the end-to-end login and registration flows

## Build, test, and lint commands
This project uses `uv` and declares dev dependencies in `pyproject.toml`.

- Install project and dev dependencies: `uv sync --group dev`
- Run the app locally: `uv run python src/index.py`
- Run the full browser test suite: `./run_robot_tests.sh`
- Run the whole Robot suite directly: `uv run robot --variable HEADLESS:true src/tests`
- Run one Robot file: `uv run robot --variable HEADLESS:true src/tests/login.robot`
- Run one Robot test case: `uv run robot --variable HEADLESS:true src/tests/login.robot --test "Login With Correct Credentials"`

## Architecture and workflow
- The app is not database-backed. `UserRepository` keeps users in a Python list, and the global singleton instance is shared by the service layer.
- Business logic lives in `UserService`, not in the route methods. Keep validation and credential checks in the service layer, and keep routes focused on HTTP concerns (`request.form`, `redirect`, `flash`).
- Routes in `src/app.py` are thin orchestration layers: they read form data, call `user_service`, and either redirect to another page or show an error via `flash()`.
- The HTML templates are route-driven and rely on the same route names used by Flask (`render_login`, `render_register`, and so on). If you change route names or redirect targets, update the templates and Robot tests together.
- The end-to-end tests live in `src/tests` and hit the real app over HTTP on port `5001`; they use the `Browser` library and the helper methods in `src/AppLibrary.py` to create users and reset the application state.

## Key conventions specific to this codebase
- Keep the local development server on port `5001`. The Robot tests hard-code `http://localhost:5001` in `src/tests/resource.robot`.
- `UserRepository.find_by_username()` is the central uniqueness check. Usernames must be unique across the in-memory dataset; do not bypass or duplicate this rule in a different layer without updating tests.
- Validation rules are centralized in `UserService.validate()`: username and password are required, username length must be at least 3 characters, password length must be at least 8 characters, and duplicate usernames are rejected.
- Error messages are surfaced as `flash()` strings and must match the test expectations exactly. The current tests expect strings such as `"Invalid username or password"`, `"Username must be at least 3 characters"`, `"Password must be at least 8 characters"`, and `"Username already exists"`.
- The test reset flow depends on `POST /tests/reset` in `src/app.py` and `AppLibrary.reset_application()`. If you introduce new state, update the reset logic so browser tests remain deterministic.
- The project is intentionally minimal and has no database layer or migration system. Prefer keeping features in the existing Flask + service + repository structure instead of introducing framework-heavy patterns unless the task requires it.

## Browser testing
- Robot browser tests require Flask to be running on port 5001.
- The script `bash run_robot_tests.sh` starts the app automatically.
- On this Windows ARM64 machine, robotframework-browser-batteries cannot be installed locally.
- Run and verify browser tests using GitHub Actions on Linux instead.
- Never claim tests passed without an actual successful run.