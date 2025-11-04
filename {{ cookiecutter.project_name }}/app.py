import asyncio
import datetime

from colorama import Fore, Style

from handlers import user, admin, core
from loader import *


async def on_startup():
    bot_info = await dp.get("bot").get_me()
    print(
        f"{Style.BRIGHT}{Fore.CYAN}https://t.me/{bot_info.username} запущен успешно! "
        f"({datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')})",
        Style.RESET_ALL
    )


async def main():
    try:
        {% if cookiecutter.bot_mode == "webhook" %}
        from loader import WEBHOOK_URL, WEBHOOK_BOT_PATH
        await bot.set_webhook(url=f"{WEBHOOK_URL}{WEBHOOK_BOT_PATH}")
        {% endif %}
        from handlers import dp
        await on_startup()
        from utils.is_status import AdminMiddleware
        dp.message.middleware(AdminMiddleware())
        dp.callback_query.middleware(AdminMiddleware())

        dp.include_routers(
            user.user_main.router,

            admin.admin_main.router,
            admin.mailing.router,

            core.core.router,
        )
        {% if cookiecutter.bot_mode == "longpoll" %}
        await bot.delete_webhook()
        await dp.start_polling(bot)
        {% endif %}
    finally:
        {% if cookiecutter.bot_mode == "longpoll" %}
        await bot.session.close()
        {% endif %}


if __name__ == '__main__':
    asyncio.run(main())
