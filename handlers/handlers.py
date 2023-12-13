from telegram import Update
from telegram.ext import ContextTypes


# This function handles the `/start` command from a user. It sends a welcome message
# and introduces the bot functionality
async def start_bot(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Send the welcome message
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f'Hello, {update.effective_user.first_name}! I am Conversion Voice BOT \n'
             f'I use cloud service to convert your audio messages into text!'
    )


# This function is called when a voice message is received
async def voice_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Get the voice message object from the update
    voice_message = update.effective_message.voice
    # Send a message to the chat informing the user that a voice message was received
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f'Voice message received! {voice_message.file_id}'
    )


# This function is called when a video message is received
async def video_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Get the video message object from the update
    video_message = update.effective_message.video_note
    # Send a message to the chat informing the user that a video message was received
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f'Video message received! {video_message.file_id}'
    )
