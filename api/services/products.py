from services.base import BaseModelService
from models.products import Product


class ProductService(BaseModelService):
    model = Product


product_service = ProductService()
