import telebot
import os
import os_utils
from db_wrapper import session, Voice, Photo, get_or_create_user
bot = telebot.TeleBot('TOKEN')

# initial setup
if not (os.path.isdir(os.path.join('audio'))):
    os.mkdir(os.path.join('audio'))
if not (os.path.isdir(os.path.join('photo'))):
    os.mkdir(os.path.join('photo'))


@bot.message_handler(content_types=['voice'])
def process_audio(message):
    voice_id = message.voice.file_id
    user_id, username = message.from_user.id, message.from_user.username

    get_or_create_user(session, user_id, username)
    path = os_utils.save_file(bot, voice_id, 'audio', str(user_id))

    session.add(Voice(id=voice_id, path=path, user_id=user_id))
    session.commit()
    bot.reply_to(message, 'audio saved')


@bot.message_handler(content_types=['photo'])
def process_photo(message):
    photo_id = message.photo[2].file_id  # [2] for 1280*720
    user_id, username = message.from_user.id, message.from_user.username

    get_or_create_user(session, user_id, username)
    path = os_utils.save_file(bot, photo_id, 'photo', str(user_id))

    session.add(Photo(id=photo_id, path=path, user_id=user_id))
    session.commit()
    bot.reply_to(message, 'photo saved')


bot.polling()