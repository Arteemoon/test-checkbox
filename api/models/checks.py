from enum import Enum
from tortoise import models, fields

from models.users import User


class PaymentTypeEnum(str, Enum):
    CASH = "cash"
    CASHLESS = "cashless"


class Check(models.Model):
    id = fields.IntField(pk=True)
    created_by: fields.ForeignKeyRelation[User] = fields.ForeignKeyField(
        "models.User", null=False
    )
    payment_type = fields.CharEnumField(enum_type=PaymentTypeEnum)
    payment_amount = fields.DecimalField(max_digits=10, decimal_places=2)
    total = fields.DecimalField(max_digits=10, decimal_places=2)
    rest = fields.DecimalField(max_digits=10, decimal_places=2, null=True)
    created_at = fields.DatetimeField(auto_now_add=True)
