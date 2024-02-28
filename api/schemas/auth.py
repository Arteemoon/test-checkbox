from pydantic import BaseModel


class UserAccessTokenRequestSchema(BaseModel):
    username: str
    password: str


class AccessTokenResponseSchema(BaseModel):
    access_token: str
    token_type: str