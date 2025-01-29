from vkbottle.bot import BotLabeler, Message
import database

bl = BotLabeler()

@bl.private_message(payload={'cmd': "admin"})
async def admin_handler(message: Message):
    if not is_admin(message.from_id):
        await message.answer("У вас нет прав доступа к административным функциям.")
        return

    await message.answer("Вы находитесь в административном меню.")
    

@bl.private_message(payload={'cmd': "set_rank"})
async def set_rank_handler(message: Message):
    if not is_admin(message.from_id):
        await message.answer("У вас нет прав доступа.")
        return

    user_id = message.payload.get("user_id")
    rank = message.payload.get("rank")

    await database.cur.execute("UPDATE users SET rank = ? WHERE vk_id = ?", (rank, user_id))
    await database.base.commit()
    
    await message.answer(f"Ранг пользователя {user_id} установлен на {rank}.")

def is_admin(user_id):
    # Проверка, является ли пользователь администратором (можно использовать базу данных)
    return user_id in [12345678]  # Замените на реальные ID администраторов
