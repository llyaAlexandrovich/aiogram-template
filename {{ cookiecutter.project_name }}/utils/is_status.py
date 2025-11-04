from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware
from aiogram.dispatcher.event.handler import HandlerObject
from aiogram.types import Update

from tables import async_session
from tables.models import Users


class AdminMiddleware(BaseMiddleware):
    def __init__(self):
        super(AdminMiddleware, self).__init__()

    async def __call__(
        self,
        handler: Callable[[Update, Dict[str, Any]], Awaitable[Any]],
        event: Update,
        data: Dict[str, Any],
    ) -> Any:
        real_handler: HandlerObject = data.get("handler")
        admin_key = real_handler.flags.get("is_admin")
        if admin_key is not None:

            async with async_session() as session:
                __user = await session.get(Users, event.from_user.id)

            if __user and __user.is_admin:
                return await handler(event, data)
            return None
        return await handler(event, data)