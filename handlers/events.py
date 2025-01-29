from vkbottle.bot import BotLabeler, Message
import database

bl = BotLabeler()

@bl.private_message(payload={'cmd': "create_event"})
async def create_event_handler(message: Message):
    if not is_admin(message.from_id):
        await message.answer("У вас нет прав доступа.")
        return
    
    event_name = message.payload.get("name")
    description = message.payload.get("description")
    
    await database.cur.execute("INSERT INTO events (name, description) VALUES (?, ?)", (event_name, description))
    await database.base.commit()
    
    await message.answer(f"Событие '{event_name}' успешно создано!")

@bl.private_message(payload={'cmd': "join_event"})
async def join_event_handler(message: Message):
    user_id = message.from_id
    
    event_data = await database.cur.execute("SELECT * FROM events WHERE status='active'")
    event_data = await event_data.fetchall()

    if not event_data:
        await message.answer("На данный момент нет активных событий.")
        return

    user_participated = any(str(user_id) in event[4].split(',') for event in event_data)

    if user_participated:
        await message.answer("Похоже, ты уже участвуешь в событиях. Приходи завтра!")
        return

    event_data = event_data[0]  # Получаем первое событие для примера

    # Добавление пользователя в участников события
    await database.cur.execute("UPDATE events SET participants = participants || ? WHERE id = ?", (f"{user_id},", event_data[0]))
    await database.cur.execute("UPDATE users SET points = points + ? WHERE vk_id = ?", (event_data[5], user_id))
    await database.base.commit()

    text = f"Ты зарегистрирован на событие: {event_data[1]}!\nОписание: {event_data[2]}"
    await message.answer(text)

def is_admin(user_id):
    return user_id in [35]  # Замените на реальные ID администраторов
