from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordRequestForm

from schemas.users import UserRegistrationSchema, UserRegistrationSuccessSchema
from schemas.auth import AccessTokenResponseSchema
from schemas.exceptions import BadRequestSchema

from services.users import user_service

from utils.auth import get_access_token

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post(
    "/registration",
    status_code=status.HTTP_201_CREATED,
    response_model=UserRegistrationSuccessSchema,
    responses={
        status.HTTP_201_CREATED: {"model": UserRegistrationSuccessSchema},
        status.HTTP_400_BAD_REQUEST: {"model": BadRequestSchema},
    },
)
async def registration(user_data: UserRegistrationSchema):
    if await user_service.exists(username=user_data.username):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="This user is already registered. Please log in using your credentials or reset your password if you've forgotten it",
        )

    user = await user_service.create(**user_data.model_dump())

    return user


@router.post(
    "/token",
    response_model=AccessTokenResponseSchema,
    responses={status.HTTP_401_UNAUTHORIZED: {"model": BadRequestSchema}},
)
async def access_token(user_data: OAuth2PasswordRequestForm = Depends()):
    token = await get_access_token(user_data)
    return {"access_token": token, "token_type": "bearer"}
