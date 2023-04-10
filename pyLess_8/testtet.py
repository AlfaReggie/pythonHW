import telebot
from pyLess_8 import task_1

bot = telebot.TeleBot('6239166068:AAFY6cEvAp5pvqcd2W9j893GVrwug2YOJtw')

@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Я на связи. Напиши мне что-нибудь )')
    task_1.main()

bot.polling(none_stop=True, interval=0)
