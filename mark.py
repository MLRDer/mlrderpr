import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from bs4 import BeautifulSoup
import urllib3
import requests
import json
import re
import time
import random

TELEGRAM_TOKEN = '1172177922:AAF87tcFWGCVYsrcvHD8umuy2vT39n4fYKk'

bot = telebot.TeleBot(TELEGRAM_TOKEN)


def gen_markup(channel, message):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text='☘️ Taklif / Invite ☘️', url='https://telegram.me/share/url?url=https://t.me/{}'.format(channel)))
    markup.add(InlineKeyboardButton(text='🍀 Ulashish / Share 🍀', url='https://telegram.me/share/url?url=https://t.me/{}/{}'.format(channel, message)))

    return markup



@bot.channel_post_handler(content_types = ['text', 'photo', 'video'])
def hey(message):
    if message.chat.type == 'channel':
        bot.edit_message_reply_markup(chat_id = message.chat.id, message_id = message.message_id, reply_markup = gen_markup(message.chat.username, message.message_id))


bot.polling()