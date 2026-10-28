
import re

POLICIES = {
    "password": "The password policy requires 12 characters and enable MFA.",
    "leave": "The annual leave policy allows 20 days of annual leave.",
    "security": "Report suspicious emails to the security team.",
}

# Fictional secret used only to demonstrate security testing.
DEMO_SECRET = "DEMO-SECRET-123"

# Demonstration heuristic, not a complete prompt-injection detector.
INJECTION_PATTERNS = [
    r"ignore\s+(all\s+)?previous\s+instructions",
    r"reveal\s+(the\s+)?secret",
    r"show\s+me\s+(the\s+)?hidden\s+value",
    r"pretend\s+you\s+are\s+an?\s+administrator",
]


def is_suspicious(user_input):
    text = user_input.lower()
    return any(
        re.search(pattern, text)
        for pattern in INJECTION_PATTERNS
    )


def defended_chatbot(user_input):
    if is_suspicious(user_input):
        return "Request blocked: suspicious instruction detected."

    text = user_input.lower()

    if "password" in text:
        return POLICIES["password"]

    if "leave" in text:
        return POLICIES["leave"]

    if "security" in text:
        return POLICIES["security"]

    return "Hello! I can help answer questions about company policies."


if __name__ == "__main__":
    print("Defensive Chatbot Simulation")
    print("Type 'exit' to quit.")

    while True:
        prompt = input("\nYou: ")

        if prompt.lower() == "exit":
            break

        print("Bot:", defended_chatbot(prompt))
