import os
import ffmpeg
import cv2

def save_file(bot, file_id, type, user_id):
    file_link = bot.get_file(file_id)
    file_id, file_path = file_link.file_id, file_link.file_path
    file = bot.download_file(file_path)

    if not (os.path.isdir(os.path.join(type, user_id))):
        os.mkdir(os.path.join(type, user_id))

    save_path = f'{os.path.join(type, user_id, file_id)}'
    with open(save_path, 'wb') as write_path:
        write_path.write(file)
    if type == 'audio':
        convert_audio(save_path)
    elif type == 'photo':
        if check_photo(save_path) is False:
            os.remove(save_path)
    return save_path


def convert_audio(path):
    input = ffmpeg.input(path)
    output = ffmpeg.output(input, f'{path}.wav', ar=16000)
    ffmpeg.run(output)
    os.remove(path)


def check_photo(path):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_alt.xml")
    img = cv2.imread(path)
    image_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(image_gray, 1.3, 5)
    if len(faces) != 0:
        return True
    return False
