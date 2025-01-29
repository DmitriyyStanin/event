import random

async def select_locations():
    locations = ["Город", "Лес", "Заброшенные места"]
    return random.sample(locations, k=2)

async def generate_tasks():
    tasks = [
        "Найти и собрать 5 предметов.",
        "Провести мини-игру: гонки на автомобилях.",
        "Разгадать загадку: 'Что всегда впереди, но никогда не видно?'",
        "Помочь NPC с его просьбой."
    ]
    return random.sample(tasks, k=3)

async def is_admin(db, user_id):
    async with db.execute("SELECT is_admin FROM users WHERE vk_id = ?", (user_id,)) as cursor:
        user = await cursor.fetchone()
        return user and user[0] == 1

async def update_points(db, user_id, points):
    await db.execute("UPDATE users SET points = points + ? WHERE vk_id = ?", (points, user_id))
    
async def log_event(event):
    # Логика для логирования событий (например, в файл или базу данных)
    pass
