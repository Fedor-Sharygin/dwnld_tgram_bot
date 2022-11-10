import sys
import os
import configparser

import telebot


API_KEY = os.getenv("API_KEY")

if API_KEY == None:
    envConfig = configparser.ConfigParser()
    envConfig.read('.env')
    API_KEY = envConfig["DEFAULT"]["API_KEY"]


bot = telebot.TeleBot(API_KEY)


@bot.message_handler()
async def default(message):
    pass

bot.infinite_polling()
