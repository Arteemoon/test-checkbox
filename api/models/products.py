from tortoise import models, fields

from models.checks import Check


class Product(models.Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=30)
    price = fields.DecimalField(max_digits=10, decimal_places=2)
    quantity = fields.IntField()
    total = fields.DecimalField(max_digits=10, decimal_places=2)
    associated_check: fields.ForeignKeyRelation[Check] = fields.ForeignKeyField(
        "models.Check", null=False, related_name="products"
    )  #  The field name "associated_check" was only used to work around an error in the Tortoise-ORM library itself
