import telebot
from telebot import types

bot = telebot.TeleBot("TOKEN")

signs = ["Овен", "Телец", "Близнецы", "Рак", "Лев", "Дева", "Весы", "Скорпион", "Стрелец", "Козерог", "Водолей", "Рыбы"]

def get_markup():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3, one_time_keyboard=True)
    for s in signs:
        button = types.KeyboardButton(s)
        markup.add(button)
    return markup


@bot.message_handler(commands=['start'])
def start_message(msg):
    bot.send_message(msg.chat.id, "Выберете свой Знак Зодиака.", reply_markup=get_markup())

@bot.message_handler(regexp='Как дела?')
def start_message(msg):
    bot.send_message(msg.chat.id, "Отлично, давайте смотреть гороскопы!", reply_markup=get_markup())

@bot.message_handler(content_types=['text'])
def text_message(msg):
    isSign = False
    for s in signs:
        if msg.text == s:
            isSign = True
            bot.send_message(msg.chat.id, "Вы выбрали знак:  " + s, reply_markup=None)
    if not isSign:
        bot.send_message(msg.chat.id, "Вы что-то написали...", reply_markup=get_markup())
















@bot.message_handler(content_types=['text'])
def start_message(msg):
    bot.send_message(msg.chat.id, "Вы что-то написали...")


bot.polling(none_stop=True)

