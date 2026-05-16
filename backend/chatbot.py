import os
from dataclasses import dataclass

from dotenv import load_dotenv
from openai import OpenAI


@dataclass
class LLMChatbot:
    """Small wrapper around an LLM chat API."""

    model: str = "gpt-4.1-mini"
    system_prompt: str = "You are a helpful, concise assistant."

    def __post_init__(self) -> None:
        load_dotenv()
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError(
                "OPENAI_API_KEY is missing. Add it to a local .env file before running the app."
            )

        self.client = OpenAI(api_key=api_key)

    def get_response(self, user_input: str) -> str:
        if not user_input or not user_input.strip():
            return "Please enter a message first."

        response = self.client.responses.create(
            model=self.model,
            input=[
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": user_input.strip()},
            ],
        )

        return response.output_text
