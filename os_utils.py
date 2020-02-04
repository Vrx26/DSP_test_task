import os


def save_file(bot, file_id, type, user_id):
    file_link = bot.get_file(file_id)
    file_id, file_path = file_link.file_id, file_link.file_path
    file = bot.download_file(file_path)

    if not (os.path.isdir(os.path.join(type, user_id))):
        os.mkdir(os.path.join(type, user_id))

    save_path = f'{os.path.join(type, user_id, file_id)}'
    with open(save_path, 'wb') as write_path:
        write_path.write(file)
    return save_path
