import requests
from telegram import Update
from telegram.ext import ContextTypes

from conversion.conversion import convert


# This function handles the `/start` command from a user. It sends a welcome message
# and introduces the bot functionality
async def start_bot(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Send the welcome message
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f'Добро пожаловать, {update.effective_user.first_name}!\n'
             f'Меня зовут Conversion Voice BOT 👋🏻👀\n\n☁️ Я использую облачный '
             f'сервис Яндекса для преобразования голосовых сообщений в текст!\n\n'
             f'🕐 Отправь мне любое голосовое, продолжительностью до 30 секунд и'
             f'я его преобразую в текст!',
    )


# This function is called when a voice message is received
async def voice_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Get the voice message object from the update
    voice_message = update.effective_message.voice

    voice_info = await context.bot.getFile(voice_message.file_id)
    voice_file = requests.get(voice_info.file_path)

    message = convert(
        voice_file,
        '.ogg',
        '.ogg'
    )

    # Send a message to the chat informing the user that a voice message was received
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f'🪧 А вот и текст!\n{message}',
        reply_to_message_id=update.message.id
    )


# This function is called when a video message is received
async def video_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Get the video message object from the update
    video_message = update.effective_message.video_note

    voice_info = await context.bot.getFile(video_message.file_id)
    voice_file = requests.get(voice_info.file_path)

    message = convert(
        voice_file,
        '.mp4',
        '.ogg'
    )

    # Send a message to the chat informing the user that a video message was received
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f'🪧 А вот и текст!\n{message}',
        reply_to_message_id=update.message.id
    )
