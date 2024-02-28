from tortoise.contrib.pydantic import pydantic_model_creator

from models.products import Product


CheckProductCreateSchema = pydantic_model_creator(
    Product, exclude=("id", "total"), name="CheckProductCreateSchema"
)
