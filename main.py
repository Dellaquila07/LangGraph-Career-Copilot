from fastapi import FastAPI, Request
from contextlib import asynccontextmanager

from pydantic import BaseModel

from app.graph.build import build_graph
from app.graph.checkpointer import get_checkpointer

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with get_checkpointer() as checkpointer:
        app.state.compiled_graph = build_graph(checkpointer)
        yield


app = FastAPI(lifespan=lifespan)


class MessageRequest(BaseModel):
    message: str
    session_id: str

@app.post("/agent/message")
async def post(req: MessageRequest, request: Request):
    config = { "configurable": { "thread_id": req.session_id } }

    result = await request.app.state.compiled_graph.ainvoke(
        {"messages": [{"role": "user", "content": req.message }]},
        config=config
    )
 
    return { "response": result["messages"][-1].content }
