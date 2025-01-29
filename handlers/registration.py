import database
from vkbottle.bot import BotLabeler, Message

bl = BotLabeler()

@bl.private_message(payload={'cmd': "register"})
async def register_handler(message: Message):
    user_id = message.from_id
    
    # Проверка на существование пользователя в базе данных
    existing_user = await database.cur.execute("SELECT * FROM users WHERE vk_id = ?", (user_id,))
    
    if existing_user:
        await message.answer("Вы уже зарегистрированы!")
        return
    
    # Запрос имени у пользователя
    await message.answer("Введите ваше имя:")
    
    @bl.private_message()
    async def set_name_handler(name_message: Message):
        name = name_message.text
        
        # Регистрация нового пользователя
        await database.cur.execute("INSERT INTO users (vk_id, name) VALUES (?, ?)", (user_id, name))
        await database.base.commit()
        
        await name_message.answer("Вы успешно зарегистрированы!")
        bl.labeler.unload(set_name_handler)  # Убираем обработчик после использования
