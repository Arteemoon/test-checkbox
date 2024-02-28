from datetime import datetime
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from jose import JWTError, jwt

from models.users import User
from schemas.auth import UserAccessTokenRequestSchema
from settings import auth_settings


OAUTH_SCHEME = OAuth2PasswordBearer(tokenUrl="auth/token")


CREDENTIALS_EXCEPTION = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Could not validate credentials",
    headers={"WWW-Authenticate": "Bearer"},
)


async def get_current_user(token: str = Depends(OAUTH_SCHEME)):
    try:
        payload = jwt.decode(
            token,
            auth_settings.JWT_SECRET_KEY,
            algorithms=[auth_settings.JWT_ALGORITHM],
        )
        username: str = payload.get("sub")
        if username is None:
            raise CREDENTIALS_EXCEPTION
    except JWTError:
        raise CREDENTIALS_EXCEPTION

    user = await User.get_or_none(username=username)
    if user is None:
        raise CREDENTIALS_EXCEPTION

    return user


async def get_access_token(user_data: UserAccessTokenRequestSchema) -> str:
    user = await User.get_or_none(username=user_data.username)
    if user is None or not user.verify_password(user_data.password):
        raise CREDENTIALS_EXCEPTION

    token_data = {
        "sub": user.username,
        "exp": datetime.utcnow() + auth_settings.JWT_LIFETIME,
    }
    token = jwt.encode(token_data, auth_settings.JWT_SECRET_KEY, algorithm=auth_settings.JWT_ALGORITHM)

    return token
