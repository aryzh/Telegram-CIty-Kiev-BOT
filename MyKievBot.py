# -*- coding: utf-8 -*
# main file for Telegram BOT. For DevOps Team only.  If you are admin user kindly check config.py

import telebot
import config
import func
import os
import random
import re
from telebot import types
import Hide.tokenPrivate

# create a new Telegram Bot object
bot = telebot.TeleBot(Hide.tokenPrivate.tokenhide)

############################### COMMANDS INPUTS  #######################################################################
#Block of BOT main commands. For Example /start / help /USD
@bot.message_handler(commands=["start", "help"])
def start(message):
#create keyboard for fast user input
    markup = types.ReplyKeyboardMarkup(row_width=2)
    itembtn0 = types.KeyboardButton('курс')
    itembtn1 = types.KeyboardButton('погода')
    itembtn2 = types.KeyboardButton('справка')
    itembtn3 = types.KeyboardButton('шутка')
    markup.add(itembtn0, itembtn1, itembtn2, itembtn3)

#sending to User HELLO message
    bot.send_message(message.chat.id, random.choice(config.helloMessage), reply_markup = markup)
#sending to user help infromation
@bot.message_handler(commands=["справка", "help", "h", "c"])
def start(message):
    bot.send_message(message.chat.id, "Бот понимает несколько тысяч запросов. Например: девушки, гороскоп, транспорт, метро, шутка, погода, курс и т.д. Или напишите слово:  все ")

##################################  TEXT INPUT #########################################################################
#Starting BLOCK to response for users TEXT
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
        #bot.send_message(message.chat.id, func.UkrSibBankFinance())
        bot.send_message(message.chat.id, func.nationalBankFinance())

    elif (message.text + "\n") in config.taxiInputText:
        bot.send_message(message.chat.id, "Uber - самый лучший сервис заказа такси онлайн! Шаровая поездка при использовании ссылки https://www.uber.com/invite/uberandrii")

    elif (message.text + "\n") in config.girlsInputText:
        photoRandomGirl = open(os.path.join(config.pathGirls, random.choice(os.listdir(config.pathGirls))), "rb")
        bot.send_photo(message.chat.id, photoRandomGirl)
        bot.send_message(message.chat.id, "Как тебе наши девушки?")

    elif (message.text + "\n") in config.weatherInputText:
        bot.send_message(message.chat.id, func.weather())

    elif (message.text + "\n") in config.funnyInputText:
        bot.send_message(message.chat.id, random.choice(config.funnyOutput))

    elif (message.text + "\n") in config.deputyInputText:
        bot.send_message(message.chat.id, random.choice(config.deputyOutput))

    elif (message.text + "\n") in config.kievPhotoInputText:
        photoRandomCity = open(os.path.join(config.pathKievPhoto, random.choice(os.listdir(config.pathKievPhoto))), "rb")
        bot.send_photo(message.chat.id, photoRandomCity)

    elif message.text in (func.file_to_int_dict(config.astroInputText)).keys():
        bot.send_message(message.chat.id, func.astro(func.file_to_int_dict(config.astroInputText)[message.text]))

    elif (message.text + "\n") in                                                                                                                                                                                                                                                                             config.metroInputText:
        bot.send_message(message.chat.id, "Напиши мс для списка станций метро потом м11 или м87 номер твоей станции, а также м11м71 для рассчета времени на дорогу")
    elif (message.text in {"мсписок", "мс", 'м'}):
        bot.send_message(message.chat.id, config.metroOutput1)
        bot.send_message(message.chat.id, config.metroOutput2)
        bot.send_message(message.chat.id, config.metroOutput3)

    elif message.text[:3]+ "\n" in config.mlist and message.text[3:6]+ "\n" in config.mlist:
        bot.send_message(message.chat.id, "на метро доедете за минут так ...")
        bot.send_message(message.chat.id, func.time_to_station(int(message.text[1:3]), int(message.text[4:6])))

    elif message.text in (func.file_to_dict(config.metroHelpInput)).keys():
        bot.send_message(message.chat.id, func.file_to_dict(config.metroHelpInput)[message.text])

    elif (message.text + "\n") in config.tagInputText:
        bot.send_message(message.chat.id, func.random_tag())

    elif (message.text + "01") in func.random_person_tag():
        bot.send_message(message.chat.id, func.random_tag())

    elif (message.text + "\n") in config.iqInputText:
        bot.send_message(message.chat.id, random.choice(config.iqOutput))

          #please send message again as template was not found
    else:
        bot.send_message(message.chat.id, random.choice(config.askmeOutput))


########################################## AUDIO DOC PHOTO INPUT #######################################################
#Response if sending non text or command
@bot.message_handler(func=lambda message: True, content_types=['audio', 'document', 'photo', 'video', 'voice', 'new_chat_participant', 'new_chat_photo'])
def echo_nontext(message):
    bot.send_message(message.chat.id, "Вау! Это всё мне? :) Спасибо!")
@bot.message_handler(func=lambda message: True, content_types=['sticker', 'location', 'contact'])
def echo_sticker(message):
    bot.send_sticker(message.chat.id, "не пытайся заигрывать :) я Всё равно круче")

#BOT STARTS
if __name__ == '__main__':
    bot.polling(none_stop=True)