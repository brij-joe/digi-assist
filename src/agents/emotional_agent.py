import logging

import google.genai as genai

from app_constants import GEMINI_MODEL, EMOTIONAL_AGENT_PROMPT, GEMINI_API_KEY

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class EmotionalAgent:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'initialized'):
            logger.info("Initializing Emotional Agent")
            self.initialized = True
            self.client = genai.Client()
            logger.info("Initialized Emotional Agent")

    def chat(self, user_query: str) -> str:
        """
        Generates an emotional, empathetic response to the user's query using Gemini LLM.
        """
        emotional_prompt = EMOTIONAL_AGENT_PROMPT.format(user_query=user_query)

        # Generate response using the LLM
        response = self.client.models.generate_content(
            model=GEMINI_MODEL,
            contents=emotional_prompt
        )
        return response.text
