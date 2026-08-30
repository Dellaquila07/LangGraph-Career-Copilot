from .prompts import SUPERVISOR_PROMPT
from .state import AgentState, DECISION_OPTIONS

from langchain.chat_models import init_chat_model
from pydantic import BaseModel, Field


class Routing(BaseModel):
    next_decision: DECISION_OPTIONS = Field(
        description="Agente especialista mais adequado para tratar a solicitação"
    )


from dotenv import load_dotenv

load_dotenv()

model = init_chat_model("groq:openai/gpt-oss-20b")
supervisor_model = model.with_structured_output(Routing)


def supervisor_node(state: AgentState) -> dict:
    """ Supervisor node """
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
