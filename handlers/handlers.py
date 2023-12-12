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
