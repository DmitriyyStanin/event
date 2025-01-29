import aiosqlite
import config

async def db_import():
    conn = await aiosqlite.connect(config.DATABASE_PATH)
    cur = await conn.cursor()
    
    # Создание необходимых таблиц, если они не существуют
    await cur.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            vk_id INTEGER UNIQUE,
            points INTEGER DEFAULT 0,
            rank TEXT DEFAULT 'user'
        )
    ''')
    
    await cur.execute('''
        CREATE TABLE IF NOT EXISTS events (
            id INTEGER PRIMARY KEY,
            name TEXT,
            description TEXT,
            location TEXT,
            participants TEXT DEFAULT '',
            points INTEGER DEFAULT 0,
            status TEXT DEFAULT 'active'
        )
    ''')
    
    await cur.execute('''
        CREATE TABLE IF NOT EXISTS admin_ranks (
            id INTEGER PRIMARY KEY,
            name TEXT UNIQUE,
            permissions TEXT
        )
    ''')
    
    await conn.commit()
    return conn, cur

async def close_db(conn):
    await conn.close()
# database.py

async def get_user_data(user_id):
    async with db.acquire() as connection:
        query = "SELECT id, name, age, location, stars FROM users WHERE id = $1"
        user = await connection.fetchrow(query, user_id)
        if user:
            return dict(user)  # Преобразуем результат в словарь
        return None  # Если пользователь не найден
