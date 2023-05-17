import telebot
from auth_token import token

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    mess = f"Привет, <b>{message.from_user.first_name} <u>{message.from_user.last_name}</u></b> "
    bot.send_message(message.chat.id, mess, parse_mode='html')


@bot.message_handler()
def get_user_txt(message):
    if message.text == 'Hello':
        bot.send_message(message.chat.id, "Hello YOu too!", parse_mode='html')
    elif message.text == 'id':
        bot.send_message(message.chat.id, f"Your ID: {message.from_user.id}", parse_mode='html')
    elif message.text == "photo":
        photo = open('Antonio.png', 'rb')
        bot.send_photo(message.chat.id, photo)
    else:
        bot.send_message(message.chat.id, "GOVORITE PO RUSSKI", parse_mode='html')



bot.polling(non_stop=True)
