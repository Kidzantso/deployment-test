from backend.chatbot import LLMChatbot


def main() -> None:
    chatbot = LLMChatbot()
    print("Backend chatbot is ready. Type 'exit' to quit.")

    while True:
        user_input = input("You: ")
        if user_input.lower().strip() in {"exit", "quit"}:
            break

        print(f"Bot: {chatbot.get_response(user_input)}")


if __name__ == "__main__":
    main()
