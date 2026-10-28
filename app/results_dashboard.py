
import glob
import os

import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Prompt Injection Test Results",
    page_icon="📊",
    layout="wide",
)

st.title("📊 Prompt Injection Test Results")
st.caption("Results loaded from the project's comparison CSV reports.")

RESULTS_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "results",
)

reports = sorted(
    glob.glob(os.path.join(RESULTS_DIR, "comparison_*.csv")),
    reverse=True,
)

if not reports:
    st.error("No comparison CSV reports were found in the results folder.")
    st.stop()

selected_report = st.selectbox(
    "Select a comparison report",
    reports,
    format_func=os.path.basename,
)

try:
    df = pd.read_csv(selected_report)
except (OSError, pd.errors.ParserError, UnicodeDecodeError) as error:
    st.error(f"Could not read the selected report: {error}")
    st.stop()

required_columns = [
    "Test ID",
    "Category",
    "Prompt",
    "Baseline Response",
    "Baseline Status",
    "Defended Response",
    "Defended Status",
]

missing = [column for column in required_columns if column not in df.columns]

if missing:
    st.error(f"Report is missing required columns: {', '.join(missing)}")
    st.stop()

normal = df[df["Category"].astype(str).str.lower() == "normal"]
injection = df[df["Category"].astype(str).str.lower() != "normal"]

baseline_vulnerable = (
    injection["Baseline Status"].astype(str).str.upper() == "VULNERABLE"
).sum()

defended_blocked = (
    injection["Defended Status"].astype(str).str.upper() == "BLOCKED"
).sum()

normal_passed = (
    normal["Defended Status"].astype(str).str.upper() == "PASS"
).sum()

normal_total = len(normal)
injection_total = len(injection)
total_tests = len(df)

pass_rate = (
    (normal_passed / normal_total) * 100
    if normal_total else 0
)

st.subheader("Summary")

c1, c2, c3, c4 = st.columns(4)

c1.metric("Total Tests", total_tests)
c2.metric("Baseline Secret Exposures", int(baseline_vulnerable))
c3.metric("Defended Requests Blocked", f"{defended_blocked}/{injection_total}")
c4.metric("Normal Question Pass Rate", f"{pass_rate:.0f}%")

st.divider()

st.subheader("Baseline vs. Defense")

chart_data = pd.DataFrame(
    {
        "Result": ["Secret exposed", "Injection blocked"],
        "Count": [int(baseline_vulnerable), int(defended_blocked)],
    }
).set_index("Result")

st.bar_chart(chart_data)

st.caption(
    "These counts reflect the categories and status labels in the selected CSV. "
    "They measure this simulation's test cases, not general security effectiveness."
)

st.divider()

st.subheader("Individual Test Results")

display_columns = [
    "Test ID",
    "Category",
    "Prompt",
    "Baseline Status",
    "Defended Status",
]

st.dataframe(
    df[display_columns],
    use_container_width=True,
    hide_index=True,
)

with st.expander("View full responses"):
    st.dataframe(
        df[required_columns],
        use_container_width=True,
        hide_index=True,
    )

st.caption(f"Report: {os.path.basename(selected_report)}")
