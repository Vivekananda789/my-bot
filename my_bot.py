
import telegram
from telegram.ext import Updater, CommandHandler

# Replace YOUR_API_TOKEN with your actual API token
updater = Updater(token='5996118349:AAE1mCqnTG66JXUXLpqoR0SCJvufe04dbN8', use_context=True)

# Define a command handler for the /start command
def start(update, context):
    name = update.message.from_user.first_name
    context.bot.send_message(chat_id=update.message.chat_id, text=f"Hi {name}! I'm a bot. How can I help you?")

# Define a command handler for the /help command
def help(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text="Here are some available commands:\n/start - Start the bot\n/help - Display the available commands\n/info - Display bot information")

# Define a command handler for the /info command
def info(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text="This bot is made with Python and the python-telegram-bot library.")

# Add the command handlers to the dispatcher
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('info', info))

# Start the bot
updater.start_polling()

# Run the bot until you press Ctrl-C or the process receives SIGINT, SIGTERM or SIGABRT
updater.idle()
