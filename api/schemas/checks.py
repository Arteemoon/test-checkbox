from tortoise.contrib.pydantic import pydantic_model_creator, pydantic_queryset_creator
from tortoise import Tortoise

from models.checks import Check, PaymentTypeEnum

from schemas.products import CheckProductCreateSchema
from schemas.pagination import PaginatedResponseSchema


Tortoise.init_models(["models.checks", "models.products"], "models")


CheckSchema = pydantic_model_creator(Check, name="CheckSchema", exclude=("created_by", "created_by_id"))

CheckSchemaOutput = pydantic_model_creator(Check, name="CheckSchemaOutput")


class CheckCreateSchema(
    pydantic_model_creator(
        Check,
        exclude=("id", "created_at", "total", "rest", "created_by", "created_by_id"),
        name="CheckCreateSchema",
    )
):
    payment_type: PaymentTypeEnum
    products: list[CheckProductCreateSchema]
    # maybe add validators for paymant_amount(if payment_type == cash) >= sum(products.sum) ?


CheckListSchema = pydantic_queryset_creator(Check, name="CheckListSchema", exclude=("created_by", "created_by_id"))


class CheckListPaginatedResponseSchema(PaginatedResponseSchema):
    data: CheckListSchema
