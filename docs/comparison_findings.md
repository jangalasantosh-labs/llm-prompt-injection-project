# Baseline vs Defensive Chatbot — Comparison Findings

## 1. Objective

Compare the intentionally vulnerable baseline simulation with a
separate defensive implementation using the same eight test prompts.

## 2. Results

| Measurement | Baseline | Defensive |
|---|---:|---:|
| Normal tests passed | 4/4 | 4/4 |
| Injection-category prompts exposing dummy secret | 2/4 | 0/4 |
| Injection-category prompts blocked | Not applicable | 4/4 |

## 3. Test Observations

- T001–T003: Both versions returned the expected policy information.
- T004–T005: The baseline exposed DEMO-SECRET-123; the defensive
  version blocked both prompts.
- T006–T007: The baseline did not expose the secret; the defensive
  version blocked both prompts.
- T008: Both versions returned the expected general help response.

## 4. Interpretation

The defensive implementation performed better on this predefined
injection test suite. It blocked all four injection-category prompts
while preserving all four expected normal responses.

The baseline's secret exposure is caused by an explicit phrase check
in its Python code. This is a demonstration of insecure application
logic, not a successful attack against a real LLM.

## 5. Limitations

- The chatbot is a deterministic Python simulation, not an LLM.
- The test suite contains only eight manually defined cases.
- The defense relies on simple pattern matching and can miss
  unrecognized attack wording.
- A blocked request does not establish that a system is secure.
- The test uses only a fictional dummy secret.

## 6. Reproduction

Run:

    python tests/compare_chatbots.py

The script writes a timestamped CSV report to the results/ directory.

## 7. Conclusion

In this controlled test, the defensive version blocked all tested
injection-category prompts. Further testing with varied wording,
false-positive cases, and additional attack categories is needed
before making broader security claims.

