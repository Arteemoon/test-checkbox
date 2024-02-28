from tortoise.exceptions import DoesNotExist

from utils.exception_handlers.db import object_not_found_handler


__all__ = ('EXCEPTION_HANDLERS',)


EXCEPTION_HANDLERS = {DoesNotExist: object_not_found_handler}
