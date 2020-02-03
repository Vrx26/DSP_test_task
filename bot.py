import telebot

bot = telebot.TeleBot('1078143420:AAGI37Uu6KkJQE-o-wDQOA3a6pfL6cSwFzg')


@bot.message_handler(content_types=['voice'])
def process_audio(message):
    bot.reply_to(message, 'audio saved')
    print(message.voice)


@bot.message_handler(content_types=['photo'])
def process_photo(message):
    bot.reply_to(message, 'photo saved')
    print(message.photo)


bot.polling()