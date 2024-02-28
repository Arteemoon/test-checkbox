from contextlib import asynccontextmanager

from tortoise import Tortoise
from fastapi import FastAPI

from settings import TORTOISE_ORM_CONF


@asynccontextmanager
async def lifespan(app: FastAPI):
    await Tortoise.init(config=TORTOISE_ORM_CONF)
    yield
    await Tortoise.close_connections()
