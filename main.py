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
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    waters = types.KeyboardButton("Waters")
    agilent = types.KeyboardButton("Agilent")
    thermo = types.KeyboardButton("Thermo")
    shimadzu = types.KeyboardButton("Shimadzu")
    markup.add(waters, agilent, thermo, shimadzu)
    bot.send_message(message.chat.id, "Or visit google!", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_user_txt(message):
    bot.send_message(message.chat.id, f"Using {message.text} database")


@bot.message_handler(commands=["website"])
def website(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    website = types.KeyboardButton("WebSite")
    start = types.KeyboardButton('Start')
    stop = types.KeyboardButton('Stop')

    markup.add(website, start, stop)
    bot.send_message(message.chat.id, "Visit google!", reply_markup=markup)



bot.polling(non_stop=True)
