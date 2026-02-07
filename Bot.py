import telebot
import requests

TOKEN = '8001893058:AAFn3l_qFeFjUqIMbdlo-s24nDWW1NnJmNs'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(m):
    bot.send_message(m.chat.id, "<b>ΣΩ-PRIME: CLOUD-ACTIVE</b>\n/draw [текст] - фото\n/video [текст] - видео", parse_mode='HTML')

@bot.message_handler(commands=['draw'])
def draw(m):
    p = m.text.replace('/draw', '').strip().replace(' ', '%20')
    if p: bot.send_message(m.chat.id, f"🎨 Результат:\nhttps://image.pollinations.ai/{p}")

@bot.message_handler(commands=['video'])
def video(m):
    p = m.text.replace('/video', '').strip().replace(' ', '%20')
    if p: bot.send_message(m.chat.id, f"🎬 Видео генерируется:\nhttps://image.pollinations.ai/{p}?model=video")

bot.polling(none_stop=True)
