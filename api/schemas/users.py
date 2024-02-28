from pydantic import BaseModel, Field, field_validator

from tortoise.contrib.pydantic import pydantic_model_creator

from models.users import User


class UserRegistrationSchema(BaseModel):
    name: str = Field(..., max_length=50)
    username: str = Field(..., max_length=30)
    password: str = Field(..., max_length=20)

    @field_validator("password")
    def check_password(cls, value):
        # convert the password to a string if it is not already
        value = str(value)
        # check that the password has at least 8 characters, one uppercase letter, one lowercase letter, and one digit
        if len(value) < 8:
            raise ValueError("Password must have at least 8 characters")
        if not any(c.isupper() for c in value):
            raise ValueError("Password must have at least one uppercase letter")
        if not any(c.islower() for c in value):
            raise ValueError("Password must have at least one lowercase letter")
        if not any(c.isdigit() for c in value):
            raise ValueError("Password must have at least one digit")
        return value


UserRegistrationSuccessSchema = pydantic_model_creator(User, exclude=("password",))
