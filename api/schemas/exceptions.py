from pydantic import BaseModel


class BadRequestSchema(BaseModel):
    detail: str
