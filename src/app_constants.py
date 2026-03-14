from dotenv import load_dotenv
import os

load_dotenv(dotenv_path="c:/temp/.env", verbose=True)
# GEMINI_MODEL = "gemini-3-flash-preview"
GEMINI_MODEL = "gemini-3.1-flash-lite-preview"
# API Key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Prompts
LOGICAL_AGENT_PROMPT = "You are a logical assistant AI. Respond factually, analytically, and logically to the following user query:\n\n {user_query}"
EMOTIONAL_AGENT_PROMPT = "You are an emotional support AI. Respond empathetically, supportively, and kindly to the following user query:\n\n {user_query}"
CLASSIFIER_PROMPT = "Classify the following user input as either 'logical' or 'emotional'. Respond with only one word: logical or emotional. User input:\n\n {user_query}"
