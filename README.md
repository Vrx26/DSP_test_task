# DSP_test_task

Разработать Бота в Телеграме, который умеет :


1. Сохранять аудиосообщения из диалогов в базу данных (СУБД или на диск) по идентификаторам пользователей.
2. Конвертирует все аудиосообщения в формат wav с частотой дискретизации 16kHz
Формат записи: uid —> [audio_message_0, audio_message_1, ..., audio_message_N].
3. Определяет есть ли лицо на отправляемых фотографиях или нет, сохраняет только те, где оно есть

## Развернутый бот: @DSP_task_bot

## Как развернуть самому(Ubuntu):
1. Установить ffmpeg - apt install ffmpeg
2. Установить требуемые библиотеки - pip install requirements.txt
3. Запустить - python bot.py
