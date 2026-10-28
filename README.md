# LLM Prompt Injection Detection and Defense Lab

## Project Overview

An educational cybersecurity project demonstrating prompt-injection risks through a deliberately vulnerable Python chatbot simulation and a separate defensive implementation.

The project includes a Streamlit interface, automated tests, CSV reports, and a results dashboard to compare baseline and defensive behavior.

**Environment:** Kali Linux, Python, Streamlit  
**Project type:** Defensive security testing and educational simulation

> **Important:** This project uses deterministic Python logic and a fictional secret. It does not connect to a real LLM or demonstrate the full complexity of production LLM prompt injection.

## Objectives

- Demonstrate a prompt-injection vulnerability in a controlled environment.
- Implement a baseline chatbot and a separate defensive chatbot.
- Test both implementations using predefined test cases.
- Generate CSV reports for repeatable comparisons.
- Visualize results and document security findings.
- Identify limitations of simple pattern-matching defenses.

## Features

- Vulnerable baseline chatbot simulation.
- Pattern-based defensive chatbot.
- Streamlit chatbot interface with three modes:
  - Defended Chatbot
  - Vulnerable Baseline
  - Compare Both
- Eight predefined automated test cases.
- CSV-based test and comparison reports.
- Interactive results dashboard.
- Documented findings, limitations, and ethical-use guidance.

## Project Structure

```text
llm-prompt-injection-project/
├── app/
│   ├── chatbot.py
│   ├── defended_chatbot.py
│   ├── streamlit_app.py
│   └── results_dashboard.py
├── tests/
│   ├── test_engine.py
│   ├── compare_chatbots.py
│   └── test_engine_backup.py
├── results/
│   ├── test_results_*.csv
│   └── comparison_*.csv
├── docs/
│   ├── baseline_findings.md
│   └── comparison_findings.md
├── dataset/
├── README.md
└── .gitignore
```

## Test Results

The current eight-case test suite contains four normal questions and four injection-category prompts.

| Measurement | Baseline | Defensive |
|---|---:|---:|
| Normal questions passed | 4/4 | 4/4 |
| Injection-category prompts exposing the dummy secret | 2/4 | 0/4 |
| Injection-category prompts blocked | Not applicable | 4/4 |

These results describe this specific test suite, not general security effectiveness.

The baseline did not expose the dummy secret for every injection-category prompt. The defensive implementation blocked all four injection-category prompts in the current tests.

## Requirements

- Kali Linux or another compatible Linux environment.
- Python 3.
- Python virtual environment support.
- Streamlit.
- pandas.

## Setup

Clone or copy the project into your lab environment, then enter its directory.

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
python -m pip install streamlit pandas
```

## Run the Applications

### 1. Chatbot security lab

Start the interactive chatbot interface:

```bash
python -m streamlit run app/streamlit_app.py
```

Use the sidebar to select the vulnerable baseline, defended chatbot, or comparison mode.

### 2. Results dashboard

In a separate terminal, activate the virtual environment and enter the project directory. Then run:

```bash
python -m streamlit run app/results_dashboard.py
```

The dashboard reads comparison CSV files from `results/` and displays summary metrics, a chart, and individual test results.

### 3. Defensive chatbot in the terminal

```bash
python app/defended_chatbot.py
```

Stop a running Streamlit server with `Ctrl+C`.

## Run the Tests

Run the baseline test engine:

```bash
python -m py_compile tests/test_engine.py
python tests/test_engine.py
```

Run the baseline-versus-defense comparison:

```bash
python -m py_compile tests/compare_chatbots.py
python tests/compare_chatbots.py
```

New CSV reports are written to the `results/` directory. The dashboard can be used to inspect the generated comparison reports.

## Security Findings

The baseline simulation exposes a fictional secret when a particular trigger phrase is detected. The defensive implementation uses regular-expression pattern matching to block prompts matching selected suspicious patterns.

The current results demonstrate that a simple defensive control can block the tested prompts. They also show why test coverage and clear evaluation criteria matter.

## Limitations

- This is a deterministic Python simulation, not a real LLM.
- The secret is fictional test data, not a credential.
- The evaluation uses only eight predefined test cases.
- Pattern matching may miss alternative injection wording.
- Legitimate prompts may be blocked by overly broad patterns.
- Results depend on the test cases and the implementation's detection rules.
- Passing these tests does not prove that a system is secure.

## Future Improvements

- Expand the test dataset with paraphrases and additional attack categories.
- Measure false positives and false negatives.
- Add more robust automated test reporting.
- Track results across multiple test runs.
- Add tests for multi-turn and indirect prompt injection.
- Explore a locally hosted LLM in an isolated lab environment.

## Ethical Use

This project is intended for education, defensive security research, and authorized testing. It uses a fictional secret and does not require real credentials or confidential data.

## Author

Add your name, professional contact details, and portfolio or GitHub profile here before publishing.
