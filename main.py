import logging

from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters

from handlers import start_bot
from misc import get_config

# Configure logging to display information messages and above
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


def main():
    # Build the Telegram bot application
    application = ApplicationBuilder().token(get_config('config.ini')).build()

    # Register a handler for the `/start` command
    application.add_handler(CommandHandler('start', start_bot))

    # Start the bot and run it in polling mode
    application.run_polling()


if __name__ == '__main__':
    main()
