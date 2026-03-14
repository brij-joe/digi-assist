import logging

import google.genai as genai

from app_constants import GEMINI_API_KEY, GEMINI_MODEL, LOGICAL_AGENT_PROMPT

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class LogicalAgent:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'initialized'):
            self.initialized = True
            self.client = genai.Client()
            logger.info("Initialized Logical Agent")

    def chat(self, user_query: str) -> str:
        """
        Generates a logical, factual response to the user's query using Gemini LLM.
        """
        logical_prompt = LOGICAL_AGENT_PROMPT.format(user_query=user_query)

        # Generate response using the LLM
        response = self.client.models.generate_content(
            model=GEMINI_MODEL,
            contents=logical_prompt
        )
        return response.text
