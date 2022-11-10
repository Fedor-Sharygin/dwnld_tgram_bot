import sys
import os
import configparser

import telebot
import youtube_dl


#define bot
API_KEY = os.getenv("API_KEY")
if API_KEY == None:
    envConfig = configparser.ConfigParser()
    envConfig.read('.env')
    API_KEY = envConfig["DEFAULT"]["API_KEY"]
bot = telebot.TeleBot(API_KEY)
#endef


#define video loading

ydl_default_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    # unnecessary params as of now
    #'logger': MyLogger(),
    #'progress_hooks': [my_hook],
}


def download_video(url, ydl_opts = ydl_default_opts):
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


#endef


#bot commands and messages
@bot.message_handler()
async def default(message):
    pass
#encom

bot.infinity_polling()
