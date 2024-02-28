from datetime import timedelta

from pydantic import BaseModel


class AuthSettings(BaseModel):
    JWT_SECRET_KEY: str = 'tmH_lPZppj23tqlAl675k-j28Tjarjkq8xN6nE8Be7Y'
    JWT_LIFETIME: timedelta = timedelta(minutes=60)
    JWT_ALGORITHM: str = 'HS256'