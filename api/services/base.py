from tortoise.models import Model


class BaseModelService:
    model: Model

    async def get(self, **filters):
        return await self.model.get(**filters)

    async def create(self, **data: dict):
        return await self.model.create(**data)

    async def update(self, update_data: dict, **filters):
        return await self.model.filter(**filters).update(**update_data)

    async def delete(self, **filters):
        return await self.model.filter(**filters).delete()

    async def exists(self, **filters) -> bool:
        return await self.model.filter(**filters).exists()
