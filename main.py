import datetime
import telebot
import os

bot =  telebot.TeleBot(os.environ["TOKEN"])

print("Bot is running: ", bot.get_me())

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Hello! I am a bot")

@bot.message_handler(commands=['time'])
def time(message):
    bot.reply_to(message, "Time is: " + str(datetime.datetime.now()))

# @bot.message_handler(func=lambda message: True)
# def echo_all(message):
#     bot.reply_to(message, message.text)
#     print("On message: ", message.text)


bot.infinity_polling()