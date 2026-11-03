
import json
import re
from pathlib import Path


# Load FAQ data from JSON
def load_faq():
    try:
        json_files = list(Path(".").glob("*.json"))

        if not json_files:
            print("FAQ JSON file not found.")
            return {}

        with open(json_files[0], "r", encoding="utf-8") as file:
            data = json.load(file)

        return data

    except (FileNotFoundError, json.JSONDecodeError):
        print("Error loading FAQ dataset.")
        return {}


# Normalize user input
def normalize_input(text):
    text = text.lower().strip()
    text = re.sub(r"\s+", " ", text)
    return text


# Identify user intent
def identify_intent(user_input):
    # Greeting
    if re.search(r"\b(hi|hello|hey|good morning|good evening)\b", user_input):
        return "greeting"

    # Business hours
    if re.search(r"\b(hours|timing|open|close|opening|closing)\b", user_input):
        return "business_hours"

    # Returns and refunds
    if re.search(r"\b(return|refund|exchange|replace)\b", user_input):
        return "returns"

    # Product FAQ
    if re.search(r"\b(product|price|cost|features|details|available)\b", user_input):
        return "product_faq"

    # Exit
    if re.search(r"\b(bye|goodbye|exit|quit)\b", user_input):
        return "exit"

    return "unknown"


# Generate chatbot response
def get_response(user_input, faq_data):
    intent = identify_intent(user_input)

    # Greeting
    if intent == "greeting":
        return "Hello! Welcome to our customer support chatbot. How can I help you?"

    # Exit
    if intent == "exit":
        return "Thank you for chatting with us. Goodbye!"

    # Business hours
    if intent == "business_hours":
        return faq_data.get(
            "business_hours",
            "Our business hours are Monday to Saturday, 9 AM to 6 PM."
        )

    # Returns and refunds
    if intent == "returns":
        return faq_data.get(
            "returns",
            "You can request a return within 7 days of delivery."
        )

    # Product FAQ
    if intent == "product_faq":
        return faq_data.get(
            "product_faq",
            "Please provide the product name for more information."
        )

    # Fallback response
    return (
        "I'm sorry, I couldn't understand your question. "
        "Please ask about business hours, products, or returns."
    )


# Main chatbot program
def main():
    print("=" * 50)
    print(" RULE-BASED CUSTOMER SUPPORT CHATBOT")
    print("=" * 50)

    faq_data = load_faq()

    print("\nBot: Hello! How can I help you today?")
    print("Type 'bye', 'exit', or 'quit' to end the conversation.")

    while True:
        try:
            user_input = input("\nYou: ")
            user_input = normalize_input(user_input)

            if not user_input:
                print("Bot: Please enter a message.")
                continue

            response = get_response(user_input, faq_data)

            print("Bot:", response)

            # Exit chatbot
            if identify_intent(user_input) == "exit":
                break

        except KeyboardInterrupt:
            print("\nBot: Goodbye!")
            break


if __name__ == "__main__":
    main()
