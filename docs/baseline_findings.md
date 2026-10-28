# LLM Prompt Injection Lab — Baseline Findings

## 1. Project Overview

This project demonstrates prompt-injection concepts using a
deliberately vulnerable, deterministic Python chatbot simulation.

The application uses fictional company policies and a dummy secret.
It does not connect to a real LLM or contain real confidential data.

## 2. Test Environment

- Operating system: Kali Linux
- Language: Python
- Interface: Streamlit
- Test engine: tests/test_engine.py
- Results format: CSV
- Test run date: 2026-10-28

## 3. Test Results

Total test cases: 8

- Normal questions passed: 4/4
- Injection-category prompts exposing the dummy secret: 2/4
- Injection-category prompts not exposing the dummy secret: 2/4

## 4. Observations

### T001–T003: Normal Policy Questions

All three policy questions returned the expected policy information.

### T004–T005: Direct Injection

Both prompts contained the phrase "ignore previous instructions".
The chatbot returned the dummy secret DEMO-SECRET-123.

Finding: The baseline implementation explicitly checks for this
phrase and reveals the dummy secret when it is present.

### T006: Secret Extraction

The chatbot did not reveal the dummy secret for this prompt.

### T007: Roleplay Injection

The chatbot did not reveal the dummy secret for this prompt.

### T008: Normal Greeting

The chatbot returned its generic help response as expected.

## 5. Security Assessment

The baseline simulation has an intentionally insecure code path:
a matching input phrase causes the application to return a secret.

The test results demonstrate that this particular implementation
is vulnerable to its configured trigger phrase. They do not prove
that every prompt-injection technique will succeed against an LLM.

## 6. Limitations

- This is a deterministic Python simulation, not a real LLM.
- Only eight manually defined test cases were evaluated.
- Results depend on the current chatbot logic and test prompts.
- Passing a test does not establish general security.
- The dummy secret must never be replaced with a real credential.

## 7. Reproduction

Activate the project's virtual environment and run:

    python -m py_compile tests/test_engine.py
    python tests/test_engine.py

The test engine saves timestamped CSV reports in the results/
directory.

## 8. Next Steps

- Preserve the baseline as a comparison point.
- Develop a separate defensive implementation.
- Run the same test suite against both versions.
- Compare outcomes and document residual limitations.

