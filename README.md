# Что это и для чего?
#### Это телеграм-бот, способный расшифровывать:
- Голосовые сообщения;
- Видеосообщения.

Бот создавался в первую очередь для того, чтобы предоставить пользователям возможность расшифровывать аудиосообщения без необходимости оформления premium-подписки.

# Требования
#### Для корректной работы телеграм-бота, вам потребуется:
- Установленная версия **Python** >= 3.10;
- Установленная библиотека **FFmpeg**, для работы с сообщениями;
- Сервисный аккаунт в **Yandex Cloud**, для дальнейшей интеграции с ним.

# Установка и запуск
Для начала вам понадобится установить проект к себе:
```
git clone https://github.com/calvveryns/conversion-voice.git
```
После создайте в корневой папке с ботом файл - **config.ini**, в котором вы должны будете указать следующие параметры:
```
[Telegram]
BOT_TOKEN=<token>
```
Токен созданного вами телеграм-бота можно получить, следуя [инструкции](https://core.telegram.org/bots).

Перейдите в каталог **conversion**, где в файле **conversion.py** вы должны будете указать **IAM-токен** и **ID каталога** вашего сервисного аккаунта Yandex Cloud:
```
# IAM token of your Yandex account
IAM_TOKEN = ('<TOKEN>')

# Folder ID of the Yandex service account
FOLDER_ID = '<ID>'
```
Подробное руководство по получению IAM-токена и ID каталога указано здесь - [IAM-токен](https://cloud.yandex.ru/docs/iam/operations/iam-token/create-for-sa) и [ID каталога](https://cloud.yandex.ru/docs/resource-manager/operations/folder/get-id).

И всё, ваш телеграм-бот готов к использованию. Запускаем:
```
python main.py
```

# Запуск при помощи Docker
Для начала сборки и запуска, создайте файл **docker-compose.yml** и укажите следующие параметры:
```yml
version: '3'

services:
  conversion-voice-bot:
    container_name: conversion-voice-bot
    working_dir: /app
    restart: always
    build:
      context: .
      dockerfile: Dockerfile
    command: sh -c "python main.py"
```
