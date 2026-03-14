import logging
import os

from langchain_core.runnables import RunnableConfig
from langgraph.graph import START, END, StateGraph

from agents.classifier_agent import ClassifierAgent
from agents.emotional_agent import EmotionalAgent
from agents.logical_agent import LogicalAgent
from utils.state import State

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def classifier_agent(state: State, config: RunnableConfig) -> State:
    logger.info("Classifier Agent ...")
    agent = ClassifierAgent()
    agent = ClassifierAgent()
    classification = agent.classify_query(state['user_query'])
    logger.info(f"Received classification agent response:\n {classification}")
    new_state: State = {'user_query': state.get('user_query'), 'classification': classification, 'response': None}  # OK
    return new_state


def logical_agent(state: State, config: RunnableConfig) -> State:
    logger.info("Logical Agent ...")
    agent = LogicalAgent()
    response = agent.chat(state['user_query'])
    new_state: State = {'user_query': state.get('user_query'), 'classification': state.get('classification'), 'response': response}  # OK
    return new_state


def emotional_agent(state: State, config: RunnableConfig) -> State:
    logger.info("Emotional Agent ...")
    agent = EmotionalAgent()
    response = agent.chat(state['user_query'])
    new_state: State = {'user_query': state.get('user_query'), 'classification': state.get('classification'), 'response': response}  # OK
    return new_state


def build_graph():
    builder = StateGraph(State)
    builder.add_node("classifier", classifier_agent)
    builder.add_node("logical", logical_agent)
    builder.add_node("emotional", emotional_agent)
    builder.add_edge(START, "classifier")
    builder.add_conditional_edges("classifier", lambda state: state["classification"], {"logical": "logical", "emotional": "emotional"})
    builder.add_edge("logical", END)
    builder.add_edge("emotional", END)
    graph = builder.compile()
    return graph


if __name__ == "__main__":
    mygraph = build_graph()
    # Run the graph with some test inputs
    test_inputs = [
        "Why sky is blue?",
        "I had a terrible day and I just want to cry.",
        "Can you explain quantum mechanics in simple terms?",
        "I'm feeling really anxious about my upcoming exams."
    ]

    for user_input in test_inputs:
        state: State = {'user_query': user_input, 'classification': None, 'response': None}  # OK
        result = mygraph.invoke(state)
        print(f"\nInput: {result['user_query']}")
        print(f"Classification: {result['classification']}")
        print(f"Response: {result['response']}")
