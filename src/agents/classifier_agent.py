import logging

import google.genai as genai

from app_constants import GEMINI_MODEL, CLASSIFIER_PROMPT, GEMINI_API_KEY

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class ClassifierAgent:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'initialized'):
            self.initialized = True
            self.client = genai.Client()
            logger.info("Initialized Classifier Agent .....")

    def classify_query(self, user_query: str) -> str:
        """
        Analyzes the sentiment of the user query and provides either a logical or emotional response accordingly.
        """
        # Classify sentiment
        sentiment_prompt = CLASSIFIER_PROMPT.format(user_query=user_query)

        # Generate response using the LLM
        sentiment_response = self.client.models.generate_content(
            model=GEMINI_MODEL,
            contents=sentiment_prompt
        )
        classification = sentiment_response.text.strip().lower()
        # Ensure it's one of the two
        if classification not in ["logical", "emotional"]:
            classification = "logical"  # default
        return classification
