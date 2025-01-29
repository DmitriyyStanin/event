import logging
import asyncio
from vkbottle import Bot, Keyboard, KeyboardButtonColor, Text
from vkbottle.bot import BotLabeler, Message
import database
import config
from handlers.user_profile import get_user_profile, get_event_info
   

   


# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Инициализация бота и базы данных
bot = Bot(token=config.VK_TOKEN)  # Используем Bot для LongPoll
bl = BotLabeler()

async def init_db():
    global base, cur
    base, cur = await database.db_import()

# Формат клавиатуры
def main_keyboard():
    keyboard = (
        Keyboard()
        .add(Text("🎄 Профиль", {'cmd': "profile"}))
        .row()
        .add(Text("📚 Функции"), color=KeyboardButtonColor.POSITIVE)
        .add(Text("📌 Информация о событии", {'cmd': "event_info"}), color=KeyboardButtonColor.PRIMARY)
        .row()
        .add(Text("ℹ️ Информация"), color=KeyboardButtonColor.POSITIVE)
        .add(Text("☎️ Поддержка"), color=KeyboardButtonColor.PRIMARY)
    )
    
    # Логирование JSON-клавиатуры
    logging.info(f"Клавиатура: {keyboard.get_json()}")
    
    return keyboard  # Возвращаем объект Keyboard

# Регистрация хендлеров (если необходимо)
from handlers import admin, events, leaderboard, registration, discussion

bl.load(admin.bl)
bl.load(events.bl)
bl.load(leaderboard.bl)
bl.load(registration.bl)
bl.load(discussion.bl)

# Логирование всех сообщений
@bot.on.message()
async def message_handler(message: Message):
    logging.info(f"Получено сообщение: {message.text} от пользователя: {message.from_id}")

    # Проверяем текст сообщения на наличие команд
    if "Продолжить" in message.text.strip():
        await message.answer("Добро пожаловать! Выберите действие:", keyboard=main_keyboard())
    elif message.text.strip() == "🎄 Профиль":  # Проверка на текст кнопки
        user_info = await get_user_profile(message.from_id)  # Получаем информацию о пользователе
        await message.answer(user_info, keyboard=main_keyboard())
    elif message.text.strip() == "📌 Информация о событии":  # Проверка на текст кнопки
        event_info = await get_event_info()  # Получаем информацию о событии
        await message.answer(event_info, keyboard=main_keyboard())
    else:
        await message.answer("Сообщение не распознано.")


async def main():
    await init_db()
    logging.info("База данных инициализирована.")
    print("Бот запущен и готов к работе.")

if __name__ == "__main__":
    try:
        asyncio.run(main())  # Инициализация базы данных
        bot.run_forever()  # Запуск бота
    except Exception as e:
        logging.error("Произошла ошибка при запуске бота: %s", e)
