from typing import TypedDict


class State(TypedDict):
    user_query: str
    classification: str | None
    response: str | None
