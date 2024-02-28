from services.base import BaseModelService

from models.users import User


class UserService(BaseModelService):
    model = User

    async def create(self, **data: dict) -> User:
        data["password"] = User.hash_password(data["password"])
        return await super().create(**data)


user_service = UserService()
