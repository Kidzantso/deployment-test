import os
from dataclasses import dataclass

from dotenv import load_dotenv
from google import genai


@dataclass
class LLMChatbot:
    """Small wrapper around an LLM chat API."""

    model: str = "gemini-2.5-flash"
    system_prompt: str = "You are a helpful, concise assistant."

    def __post_init__(self) -> None:
        load_dotenv()
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key or api_key == "your_gemini_api_key_here":
            raise ValueError(
                "GEMINI_API_KEY is missing. Add it to a local .env file before running the app."
            )

        self.client = genai.Client(api_key=api_key)

    def get_response(self, user_input: str) -> str:
        if not user_input or not user_input.strip():
            return "Please enter a message first."

        response = self.client.models.generate_content(
            model=self.model,
            contents=f"{self.system_prompt}\n\nUser: {user_input.strip()}",
        )

        return response.text or "I could not generate a response."
