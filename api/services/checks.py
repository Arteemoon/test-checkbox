from decimal import Decimal

from tortoise.transactions import in_transaction
from tortoise.queryset import QuerySet

from services.base import BaseModelService
from models.checks import Check, PaymentTypeEnum
from models.products import Product
from models.users import User


class CheckService(BaseModelService):
    model = Check

    async def create(self, **check_data: dict) -> Check:
        async with in_transaction():
            products = [
                Product(**product, total=product["price"] * product["quantity"])
                for product in check_data.pop("products")
            ]
            total_product_price = sum([product.total for product in products])
            check_data["total"] = total_product_price

            if check_data["payment_type"] == PaymentTypeEnum.CASH.value:
                check_data["rest"] = (
                    Decimal(check_data["payment_amount"]) - total_product_price
                )

            check: Check = await super().create(**check_data)
            for product in products:
                product.associated_check = check
            await Product.bulk_create(products)
            return check

    def filter_by_created_by(self, user: User) -> QuerySet:
        return self.model.filter(created_by=user)


check_service = CheckService()
