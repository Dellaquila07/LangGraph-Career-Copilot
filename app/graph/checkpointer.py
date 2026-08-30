import os

from contextlib import asynccontextmanager
from langgraph.checkpoint.memory import MemorySaver
from langgraph.checkpoint.postgres.aio import AsyncPostgresSaver


@asynccontextmanager
async def get_checkpointer():
    """ Get the checkpointer based on the enviromental """
    environment = os.getenv("APP_ENV", "dev")
    if environment == "production":
        db_uri = os.environ["POSTGRES_URI"]
        async with AsyncPostgresSaver.fromConnString(db_uri) as checkpointer:
            await checkpointer.setup()
            yield checkpointer
    else:
        yield MemorySaver()
