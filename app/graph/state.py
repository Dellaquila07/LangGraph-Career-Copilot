from typing import Annotated, Literal, Optional, TypedDict
from langgraph.graph import add_messages


DECISION_OPTIONS = Literal["agent_search", "agent_fit", "agent_preparer"]

class AgentState(TypedDict):
    messages: Annotated[list, add_messages]
    next_decision: Optional[DECISION_OPTIONS]
