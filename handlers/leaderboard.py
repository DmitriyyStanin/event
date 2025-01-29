from vkbottle.bot import BotLabeler, Message
import database

bl = BotLabeler()

@bl.private_message(payload={'cmd': "leaderboard"})
async def leaderboard_handler(message: Message):
    data = await database.cur.execute("SELECT vk_id, points FROM users ORDER BY points DESC LIMIT 10")
    leaderboard_data = await data.fetchall()
    
    leaderboard_text = "Таблица лидеров:\n"
    for idx, (vk_id, points) in enumerate(leaderboard_data):
        leaderboard_text += f"{idx + 1}. Пользователь {vk_id}: {points} очков\n"

    await message.answer(leaderboard_text)
