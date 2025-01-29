# user_profile.py

from database import get_user_data  # Импортируйте функцию для получения данных о пользователе

async def get_user_profile(user_id):
    user_data = await get_user_data(user_id)  # Получаем данные пользователя из БД

    # Предполагаем, что user_data возвращает словарь с нужными полями
    if not user_data:
        return "Пользователь не найден."

    profile_info = f"👤 Профиль пользователя:\n"
    profile_info += f"ID: {user_data['id']}\n"
    profile_info += f"Имя: {user_data['name']}\n"
    profile_info += f"Возраст: {user_data['age']}\n"
    profile_info += f"Локация: {user_data['location']}\n"
    profile_info += f"Звезды: {user_data['stars']}\n"  # Добавим информацию о звездах

    return profile_info

async def get_event_info():
    event_data = {
        'event_name': 'Название события',
        'date': '01.01.2023',
        'location': 'Место проведения',
        'description': 'Описание события',
    }

    event_info = f"📅 Информация о событии:\n"
    event_info += f"Название: {event_data['event_name']}\n"
    event_info += f"Дата: {event_data['date']}\n"
    event_info += f"Место: {event_data['location']}\n"
    event_info += f"Описание: {event_data['description']}\n"

    return event_info
