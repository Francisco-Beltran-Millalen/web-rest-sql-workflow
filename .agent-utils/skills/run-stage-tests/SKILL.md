# Run Stage Tests Skill

Run the tests for the current use case being implemented.

## Process

### 1. Identify the Current Use Case

Read `consolidation-artifacts/implementation-decisions.md`.

Look for the use case marked as in-progress, or if none is in-progress, the most recently completed one.

If the file doesn't exist or is unclear, ask the user: "Which use case should I run tests for?"

### 2. Determine the Test Filter

Read `docs/tech-stack.md` to identify the framework, then determine the right filter:

| Framework | Filter command |
|-----------|----------------|
| pytest    | `cd prototype-code && python -m pytest -k "<use-case-keyword>"` |
| jest      | `cd prototype-code && npm test -- --testPathPattern="<use-case-keyword>"` |
| vitest    | `cd prototype-code && npm run test -- --reporter=verbose <use-case-keyword>` |
| go test   | `cd prototype-code && go test ./... -run "<UseCase>"` |
| cargo test| `cd prototype-code && cargo test <use_case_keyword>` |
| JUnit/Maven | `cd prototype-code && mvn test -Dtest="*<UseCase>*"` |
| JUnit/Gradle | `cd prototype-code && ./gradlew test --tests "*<UseCase>*"` |

Derive `<use-case-keyword>` from the use case name (e.g., "User can view orders" → `orders` or `view_orders`).

If filtering is uncertain (test files have custom names), scan `prototype-code/` for test files matching the use case entity or verb, and run those files directly.

### 3. Run and Report

Run the filtered command and show the full output.

Report:
- Which use case was tested
- How many tests passed / failed / skipped
- If any failed: show failure names and error messages
- If all passed: confirm clearly
