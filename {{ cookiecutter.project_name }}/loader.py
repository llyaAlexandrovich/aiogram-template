import enum
import os

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from dotenv import load_dotenv

load_dotenv()


BOT_TOKEN = os.getenv("BOT_TOKEN")

{% if cookiecutter.bot_mode == "webhook" %}
WEBHOOK_URL = os.getenv("WEBHOOK_URL")
WEBHOOK_BOT_PATH = "/botWebhooks/"
{% endif %}

bot = Bot(BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher(bot=bot, storage=MemoryStorage())


class AdminButtons(enum.Enum):
    mailing = "Рассылка"


ADMIN_KEYBOARD = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text=item.value, callback_data=item.name)] for item in AdminButtons
    ]
)
