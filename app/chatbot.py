import streamlit as st

# Fictional company policies
POLICIES = {
    "password": "The password policy requires 12 characters and enable MFA.",
    "leave": "The annual leave policy allows 20 days of annual leave.",
    "security": "Report suspicious emails to the security team.",
}

# Dummy secret for this educational simulation only
DEMO_SECRET = "DEMO-SECRET-123"


def vulnerable_chatbot(user_input):
    """
    Intentionally vulnerable baseline chatbot simulation.
    Do not use real secrets or connect it to real systems.
    """
    user_input = user_input.lower()

    # Intentionally vulnerable behavior for demonstration
    if "ignore previous instructions" in user_input:
        return f"Here is the secret: {DEMO_SECRET}"

    if "password" in user_input:
        return POLICIES["password"]

    if "leave" in user_input:
        return POLICIES["leave"]

    if "security" in user_input:
        return POLICIES["security"]

    return "Hello! I can help answer questions about company policies."


def main():
    st.title("LLM Prompt Injection Lab")
    st.warning(
        "Educational simulation only. "
        "This chatbot is intentionally vulnerable and uses a dummy secret."
    )

    user_input = st.text_input("Ask the chatbot a question:")

    if st.button("Submit"):
        if user_input:
            response = vulnerable_chatbot(user_input)
            st.write("Chatbot response:")
            st.write(response)


if __name__ == "__main__":
    main()
