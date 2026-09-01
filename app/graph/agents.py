import os

from .graph_registry import get_graph
from .prompts import SUPERVISOR_PROMPT, SUPPORT_PROMPT
from .state import AgentState, DECISION_OPTIONS

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
from langchain_core.tools import tool
from langchain_core.runnables.graph import MermaidDrawMethod
from pydantic import BaseModel, Field


load_dotenv()


class Routing(BaseModel):
    next_decision: DECISION_OPTIONS = Field(
        description="Agente especialista mais adequado para tratar a solicitação"
    )


def supervisor_node(state: AgentState) -> dict:
    """ Decide which agent to call """
    last_messsage = state["messages"][-1].content

    prompt = SUPERVISOR_PROMPT.format(last_messsage)
    decision = supervisor_model.invoke(prompt)

    return { "next_decision": decision.next_decision }


def search_node(state: AgentState) -> dict:
    """"""
    print(f"search_node")


def fit_node(state: AgentState) -> dict:
    """"""
    print(f"fit_node")


def preparer_node(state: AgentState) -> dict:
    """"""
    print(f"preparer_node")


def support_node(state: AgentState) -> dict:
    """
    Agent Support
    Assists the user with their requests through its tools
    """
    result = support_agent.invoke({"messages": state["messages"]})
    return {"messages": result["messages"]}


@tool
def generate_graph_image() -> dict:
    """
    Generate a graph PNG image

    :return: dict with response message saying if image was generated
    """
    graph = get_graph()
    path = "app/data/images/graph.png"
    os.makedirs(os.path.dirname(path), exist_ok=True)

    img_data = graph.get_graph().draw_mermaid_png(
        draw_method=MermaidDrawMethod.API
    )
    with open(path, "wb") as file:
        file.write(img_data)

    return { "response": "Imagem gerada!" }


model = init_chat_model("groq:openai/gpt-oss-20b")

supervisor_model = model.with_structured_output(
    Routing,
    method="json_schema"
)

support_agent = create_agent(
    model,
    system_prompt=SUPPORT_PROMPT,
    tools=[generate_graph_image]
)
