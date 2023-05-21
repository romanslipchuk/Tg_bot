import telebot
from telebot import types
import requests
from bs4 import BeautifulSoup
from logs.auth_token import token

bot = telebot.TeleBot(token)

"""
TODO:
0. Add vendors buttons
1. Add request to Wates site
2. Add parsing respond
2-a Create docker image to run on server
3. Add server in amazon
"""


@bot.message_handler(commands=['start'])
def start(message):
    mess = "Please select your HPLC vendor"
    bot.send_message(message.chat.id, mess)
    markup = types.InlineKeyboardMarkup(row_width=2)
    waters = types.InlineKeyboardButton('Waters', callback_data='Waters')
    agilent = types.InlineKeyboardButton("Agilent")
    thermo = types.InlineKeyboardButton("Thermo")
    shimadzu = types.InlineKeyboardButton("Shimadzu")
    markup.add(waters, agilent, thermo, shimadzu)
    bot.send_message(message.chat.id, "Or visit google!", reply_markup=markup)

@bot.callback_query_handler(func=lambda call:True)
def callback(call):
    if call.message:
        if call.data == 'Waters':
            bot.send_message(call.message.chat.id, "Enter your error message:")

# @bot.message_handler(content_types=['text'])
# def get_user_txt(message):
#     bot.send_message(message.chat.id, f"Using {message.text} database")


# @bot.message_handler(commands=["Waters"])
# def website(message):
#     bot.send_message(message.chat.id, "Enter your error message:")



bot.polling(non_stop=True)
