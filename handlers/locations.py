import random
from vkbottle.bot import Message

locations = ["Город", "Лес", "Заброшенные места"]

async def location_handler(message: Message):
    selected_locations = random.sample(locations, k=2)
    await message.answer(f"Вы выбрали локации: {', '.join(selected_locations)}.")
