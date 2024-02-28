from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);
CREATE TABLE IF NOT EXISTS "user" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(50) NOT NULL,
    "username" VARCHAR(30) NOT NULL UNIQUE,
    "password" VARCHAR(60) NOT NULL
);
CREATE TABLE IF NOT EXISTS "check" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "payment_type" VARCHAR(8) NOT NULL,
    "payment_amount" DECIMAL(10,2) NOT NULL,
    "total" DECIMAL(10,2) NOT NULL,
    "rest" DECIMAL(10,2),
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "created_by_id" INT NOT NULL REFERENCES "user" ("id") ON DELETE CASCADE
);
COMMENT ON COLUMN "check"."payment_type" IS 'CASH: cash\nCASHLESS: cashless';
CREATE TABLE IF NOT EXISTS "product" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(30) NOT NULL,
    "price" DECIMAL(10,2) NOT NULL,
    "quantity" INT NOT NULL,
    "total" DECIMAL(10,2) NOT NULL,
    "associated_check_id" INT NOT NULL REFERENCES "check" ("id") ON DELETE CASCADE
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
