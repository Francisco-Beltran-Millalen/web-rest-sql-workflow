# Run All Tests Skill

Run the full test suite for the current project.

## Process

1. Read `docs/tech-stack.md` to identify the test framework and language
2. Determine the test command based on the framework:

   | Framework | Command |
   |-----------|---------|
   | pytest    | `cd prototype-code && python -m pytest` |
   | jest      | `cd prototype-code && npm test` |
   | vitest    | `cd prototype-code && npm run test` |
   | go test   | `cd prototype-code && go test ./...` |
   | cargo test| `cd prototype-code && cargo test` |
   | JUnit/Maven | `cd prototype-code && mvn test` |
   | JUnit/Gradle | `cd prototype-code && ./gradlew test` |

   If the framework is not in this list, infer the command from the project structure (check `prototype-code/` for `package.json`, `Cargo.toml`, `pom.xml`, `build.gradle`, `pyproject.toml`, etc.).

3. Run the command and show the full output.

4. Report:
   - How many tests passed / failed / skipped
   - If any failed: show the failure names and error messages
   - If all passed: confirm clearly
