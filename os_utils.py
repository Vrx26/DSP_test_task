import os


def save_file(bot, file_id, type):
    file_link = bot.get_file(file_id)
    file_id, file_path = file_link.file_id, file_link.file_path
    file = bot.download_file(file_path)
    save_path = f'{os.path.join(type, file_id)}.jpg'
    with open(save_path, 'wb') as write_path:
        write_path.write(file)
    return save_path
