import telebot

TOKEN = "8375049997:AAHd8vq0JwB6QB3uHdSDYfy6cjAc5TxIZV4"
bot = telebot.TeleBot(TOKEN)

savol = [
    {"savol": "1. 25 + 37 =", "variant": ["A) 52", "B) 62", "C) 64"], "javob": "C"},
    {"savol": "2. 80 - 45 =", "variant": ["A) 25", "B) 35", "C) 40"], "javob": "B"},
    {"savol": "3. 9 * 8 =", "variant": ["A) 81", "B) 72", "C) 64"], "javob": "B"},
    {"savol": "4. 56 / 7 =", "variant": ["A) 8", "B) 9", "C) 7"], "javob": "A"},
    {"savol": "5. 1 metr necha santimetrga teng?", "variant": ["A) 10", "B) 100", "C) 1000"], "javob": "B"},
    {"savol": "6. 1000 gramm necha kilogramm?", "variant": ["A) 10", "B) 1", "C) 0.1"], "javob": "B"},
    {"savol": "7. 1/4 ning o'nli kasr ko'rinishi qaysi?", "variant": ["A) 0.5", "B) 0.25", "C) 0.75"], "javob": "B"},
    {"savol": "8. 3 sonining kvadrati =", "variant": ["A) 6", "B) 9", "C) 12"], "javob": "B"},
    {"savol": "9. 120 ning 1/2 qismi =", "variant": ["A) 60", "B) 50", "C) 40"], "javob": "A"},
    {"savol": "10. Eng kichik juft son qaysi?", "variant": ["A) 0", "B) 1", "C) 2"], "javob": "A"}
]

user_data = {}

@bot.message_handler(commands=['start'])
def start_test(message):
    user_id = message.chat.id
    user_data[user_id] = {"shu_q": 0, "togri": 0}
    bot.send_message(user_id, "👋 Salom! 5-sinf matematika testiga xush kelibsiz!\nBoshlaymiz👇")
    send_savol(user_id)

def send_savol(user_id):
    data = user_data[user_id]
    q_index = data["shu_q"]
    if q_index < len(savol):
        q = savol[q_index]
        text = f"{q['savol']}\n"
        for opt in q["variant"]:
            text += f"{opt}\n"
        bot.send_message(user_id, text)
    else:
        savollar = len(savol)
        togri = data["togri"]
        percent = round((togri / savollar) * 100, 2)
        bot.send_message(
            user_id,
            f"✅ Test yakunlandi!\nTo'g'ri javoblar soni: {togri}/{savollar}\nFoiz: {percent}%"
        )

@bot.message_handler(func=lambda message: True)
def handle_javob(message):
    user_id = message.chat.id
    if user_id not in user_data:
        bot.send_message(user_id, "Testni /start buyrug'i bilan boshlang.")
        return
    data = user_data[user_id]
    q_index = data["shu_q"]
    if q_index < len(savol):
        togri_javob = savol[q_index]["javob"].upper()
        user_javob = message.text.strip().upper()
        if user_javob == togri_javob:
            data["togri"] += 1
            bot.send_message(user_id, "✅ To'g'ri!")
        else:
            bot.send_message(user_id, f"❌ Noto'g'ri. To'g'ri javob: {togri_javob}")
        data["shu_q"] += 1
        send_savol(user_id)

bot.polling(non_stop=True)
