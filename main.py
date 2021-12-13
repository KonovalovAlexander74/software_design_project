import telebot
from telebot import types
import codecs

bot = telebot.TeleBot("TOKEN")

signs = ["Овен", "Телец", "Близнецы", "Рак", "Лев", "Дева", "Весы", "Скорпион", "Стрелец", "Козерог", "Водолей", "Рыбы"]
functions = ["Описание", "Гороскоп", "Совместимость","Назад"]

class User:
    def __init__(self, telegramId, sign):
        self.telegramId = telegramId
        self.sign = sign

users = {}

def get_markup():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, one_time_keyboard=True)
    for i in range(0, len(signs), 3):
        button1 = types.KeyboardButton(signs[i])
        button2 = types.KeyboardButton(signs[i + 1])
        button3 = types.KeyboardButton(signs[i + 2])
        markup.row(button1, button2, button3)
    return markup

def get_functions_markup():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
    for f in functions:
        button = types.KeyboardButton(f)
        markup.add(button)
    return markup

@bot.message_handler(commands=['start'])
def start_message(msg):
    bot.send_message(msg.chat.id, "Выберете свой Знак зодиака", reply_markup=get_markup())

@bot.message_handler(regexp='Как дела?')
def how_are_you_message(msg):
    bot.send_message(msg.chat.id, "Отлично, давайте смотреть гороскопы!", reply_markup=get_markup())

@bot.message_handler(regexp='Описание')
def description_message(msg):
    bot.send_message(msg.chat.id, "Характеристика", reply_markup=get_functions_markup())
    file = open("signs/"+str(users[msg.chat.id].sign)+".txt", encoding='utf-8')
    if file:
        bot.send_message(msg.chat.id, file.readline(), reply_markup=get_functions_markup())

    file.close()

def get_compatibility(msg):
    bot.send_message(msg.chat.id, "Ваш знак:  " + users[msg.chat.id].sign + "\nПроверка cовместимости с:  " + msg.text, reply_markup=get_functions_markup())

@bot.message_handler(regexp='Совместимость')
def description_message(msg):
    bot.send_message(msg.chat.id, "Выберите знак для проверки совместимости ", reply_markup=get_markup())
    bot.register_next_step_handler(msg, get_compatibility)


@bot.message_handler(regexp='Назад')
def back_message(msg):
    start_message(msg)



@bot.message_handler(content_types=['text'])
def text_message(msg):
    isSign = False
    for s in signs:
        if msg.text == s:
            isSign = True
            bot.send_message(msg.chat.id, "Вы выбрали знак:  " + s, reply_markup=get_functions_markup())
            users[msg.chat.id] = User(msg.chat.id, str(s))
            print(users[msg.chat.id].sign)
            break




    if not isSign:
        bot.send_message(msg.chat.id, "Вы что-то написали...", reply_markup=get_markup())





bot.polling(none_stop=True)
