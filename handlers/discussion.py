from vkbottle import Bot
from vkbottle.bot import BotLabeler, Message
from utils.keyboards import main_keyboard

bl = BotLabeler()

async def discuss_results_handler(message: Message):
    await message.answer("Пожалуйста, поделитесь своими впечатлениями и стратегиями по завершению квеста!", keyboard=main_keyboard())
