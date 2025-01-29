from vkbottle import Keyboard, Text, KeyboardButtonColor

def main_keyboard():
    keyboard = Keyboard()
    keyboard.add(Text("🎄 Новый год с Kasper ❄️", {'cmd': "events"}))
    keyboard.row()
    keyboard.add(Text("📚 Функции"), KeyboardButtonColor.POSITIVE)
    keyboard.add(Text("📌 Профиль"), KeyboardButtonColor.PRIMARY)
    keyboard.row()
    keyboard.add(Text("ℹ️ Информация"), KeyboardButtonColor.POSITIVE)
    keyboard.add(Text("☎️ Поддержка"), KeyboardButtonColor.PRIMARY)

    return keyboard.get_json()
