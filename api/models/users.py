from passlib.context import CryptContext

from tortoise import models, fields


CRYPTO_CONTEXT = CryptContext(schemes=["bcrypt"], deprecated="auto")


class User(models.Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=50)
    username = fields.CharField(max_length=30, unique=True)
    password = fields.CharField(max_length=60)

    @classmethod
    def hash_password(cls, password: str) -> str:
        return CRYPTO_CONTEXT.hash(password)

    def verify_password(self, password: str) -> bool:
        return CRYPTO_CONTEXT.verify(password, self.password)
