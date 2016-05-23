 # -*- coding: utf-8 -*
# main file for Telegram BOT. For development team only
import telebot
import config
import func
import os
import random
import re
import codecs
import time
from telebot import types
bot = telebot.TeleBot(config.token)

#BASIC COMMANDS of the BOT
@bot.message_handler(commands=["start", "help"])
def start(message):
#create keyboard
    markup = types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = types.KeyboardButton('/курс')
    itembtn2 = types.KeyboardButton('/погода')
    itembtn3 = types.KeyboardButton('/пробки')
    itembtn4 = types.KeyboardButton("/фото")
    itembtn5 = types.KeyboardButton('/приколы')
    itembtn6 = types.KeyboardButton('/распродажи')
    markup.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5, itembtn6)
# sending HELLO message
    bot.send_message(message.chat.id, config.helloMessage, reply_markup = markup)

# inicialase additional BOT COMMANDS
@bot.message_handler(commands=["USD", "U", "доллар", "курс"])
def start(message):
    bot.send_message(message.chat.id, func.yahooFinance())
    bot.send_message(message.chat.id, func.privatBankFinance())
    bot.send_message(message.chat.id, func.UkrSibBankFinance())
    bot.send_message(message.chat.id, func.nationalBankFinance())
@bot.message_handler(commands=["traf", "t", "tr", "tra",  "traf fic", "траф"  , "т", "траффик", "тр", "тра", "пробки", "aэропорт"])
def start(message):
    bot.send_message(message.chat.id, "Киеве пробки 7 балов")
@bot.message_handler(commands=["погода"])
def start(message):
    bot.send_message(message.chat.id, func.weather())
@bot.message_handler(commands=["фото"])
def start(message):
    photoRandomCity = open(os.path.join(config.path, random.choice(os.listdir(config.path))), "rb")
    bot.send_photo(message.chat.id, photoRandomCity)
@bot.message_handler(commands=["распродажи"])
def start(message):
    bot.send_message(message.chat.id, "Все будет дешево! Но не скоро!")
@bot.message_handler(commands=["приколы"])
def start(message):
    bot.send_message(message.chat.id, random.choice(config.funnyOutput))

#START OF MAIN BLOCK to response for users TEXT
@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_msg(message):
# cheking users inputs. cut first word and filter possible injections from text
    message.text = (message.text.lower().partition(' ')[0]).partition(',')[0]
    message.text = re.sub(r'[\W]', r'', message.text).strip()[:30]

    if message.text is "":
        bot.send_message(message.chat.id, "Детка, ну стесняйся - спроси понятно, словами :)")

    elif (message.text + "\n") in config.exchangeInputText:
        bot.send_message(message.chat.id, func.yahooFinance())
        bot.send_message(message.chat.id, func.privatBankFinance())
        bot.send_message(message.chat.id, func.UkrSibBankFinance())
        bot.send_message(message.chat.id, func.nationalBankFinance())

    elif (message.text + "\n") in config.taxiInputText:
        bot.send_message(message.chat.id, "Уклон - самый лучший сервис заказа такси онлайн!")

    elif (message.text + "\n") in config.girlsInputText:
        photoRandomGirl = open(os.path.join(config.pathGirls, random.choice(os.listdir(config.pathGirls))), "rb")
        bot.send_photo(message.chat.id, photoRandomGirl)
        bot.send_message(message.chat.id, "Как тебе наши девушки?")

    elif (message.text + "\n") in config.weatherInputText:
        bot.send_message(message.chat.id, func.weather())

    elif (message.text + "\n") in config.funnyInputText:
        bot.send_message(message.chat.id, random.choice(config.funnyOutput))

#please send message again as template was not found
    else:
        bot.send_message(message.chat.id, "Крошка, я понимаю 10000 комманд, попробуй еще раз, Заец")

#Response to contect. NTD
@bot.message_handler(func=lambda message: True, content_types=['audio', 'document', 'photo', 'video', 'voice', 'new_chat_participant', 'new_chat_photo'])
def echo_nontext(message):
    bot.send_message(message.chat.id, "Вау! Это всё мне? :) Спасибо!")
@bot.message_handler(func=lambda message: True, content_types=['sticker', 'location', 'contact'])
def echo_sticker(message):
    bot.send_sticker(message.chat.id, "не пытайся заигрывать :) я Всё равно круче")

#BOT STARTS
if __name__ == '__main__':
    bot.polling(none_stop=True)