from .agents import fit_node, preparer_node, search_node, supervisor_node
from .state import AgentState

from langgraph.graph import START, END, StateGraph


def build_graph(checkpointer):
    graph = StateGraph(AgentState)

    graph.add_node("supervisor", supervisor_node)
    graph.add_node("agent_search", search_node)
    graph.add_node("agent_fit", fit_node)
    graph.add_node("agent_preparer", preparer_node)

    graph.add_edge(START, "supervisor")
    graph.add_conditional_edges(
        "supervisor",
        get_next_decision,
        {
            "agent_search": "agent_search",
            "agent_fit": "agent_fit",
            "agent_preparer": "agent_preparer",
            "END": END
        }
    )
    graph.add_edge("agent_search", "supervisor")
    graph.add_edge("agent_fit", "supervisor")
    graph.add_edge("agent_preparer", "supervisor")

    return graph.compile(checkpointer=checkpointer)


def get_next_decision(state: AgentState) -> str:
    """ Get next decision to router """
    return state["next_decision"]
