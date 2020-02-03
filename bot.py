import telebot
import os_utils
from db_wrapper import conn
bot = telebot.TeleBot('1078143420:AAGI37Uu6KkJQE-o-wDQOA3a6pfL6cSwFzg')


@bot.message_handler(content_types=['voice'])
def process_audio(message):
    voice_id = message.voice.file_id
    os_utils.save_file(bot, voice_id, 'audio')
    bot.reply_to(message, 'audio saved')


@bot.message_handler(content_types=['photo'])
def process_photo(message):
    photo_id = message.photo[2].file_id
    os_utils.save_file(bot, photo_id, 'photo')
    bot.reply_to(message, 'photo saved')


bot.polling()