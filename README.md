# LLM Prompt Injection Detection and Defense Lab

## Project Overview

This educational cybersecurity project demonstrates prompt-injection concepts using a deliberately vulnerable Python chatbot simulation and a separate defensive implementation.

The project compares both implementations using an automated suite of eight predefined test cases.

**Environment:** Kali Linux, Python, Streamlit  
**Project type:** Defensive security testing and educational simulation

## Objectives

- Demonstrate a prompt-injection vulnerability in a controlled environment.
- Build an automated test engine.
- Implement a basic pattern-matching defense.
- Compare baseline and defensive behavior.
- Generate CSV results and document findings.

## Project Structure

```text
llm-prompt-injection-project/
├── app/
│   ├── chatbot.py
│   └── defended_chatbot.py
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
└── test_python.py
```

## Features

- Vulnerable baseline chatbot simulation
- Separate defensive chatbot
- Eight automated test cases
- CSV result generation
- Baseline-versus-defense comparison
- Markdown findings reports

## Test Results

| Measurement | Baseline | Defensive |
|---|---:|---:|
| Normal tests passed | 4/4 | 4/4 |
| Injection-category prompts exposing the dummy secret | 2/4 | 0/4 |
| Injection-category prompts blocked | Not applicable | 4/4 |

These results apply only to the eight predefined prompts in this simulation.

## Setup

Clone or copy the project to your Kali Linux environment, then enter the project directory.

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the required packages:

```bash
pip install streamlit pandas
```

## Run the Applications

Launch the baseline web interface:

```bash
streamlit run app/chatbot.py
```

Run the defensive chatbot in the terminal:

```bash
python app/defended_chatbot.py
```

## Run the Tests

Check and run the baseline test engine:

```bash
python -m py_compile tests/test_engine.py
python tests/test_engine.py
```

Compare the baseline and defensive implementations:

```bash
python -m py_compile tests/compare_chatbots.py
python tests/compare_chatbots.py
```

CSV reports are written to the `results/` directory.

## Security Findings

The baseline simulation exposes its fictional secret when a prompt contains a specific trigger phrase. The defensive implementation uses simple pattern matching to block the injection-category prompts in the current test suite.

This demonstrates a basic security control, not a complete solution to prompt injection.

## Limitations

- This is a deterministic Python simulation, not a real LLM.
- The secret is fictional test data.
- The test suite contains only eight predefined prompts.
- Pattern matching can miss variations and may block harmless requests.
- Passing these tests does not prove that a system is secure.

## Future Improvements

- Expand the test dataset with more prompt variations.
- Add false-positive and false-negative analysis.
- Improve structured test reporting.
- Add visualizations of comparison results.
- Explore testing against a locally hosted LLM in an isolated lab.

## Ethical Use

This project is intended for education and authorized security testing. It does not require real credentials or confidential data.

## Author

Add your name and professional contact details here if you want to publish this project in your portfolio.
