#! /usr/bin/python

import constants as keys
from telegram.ext import *

# Marking the beginning of the converstation 
print ("Bot session has begun")

# Adding a start command so users and start a converstation
def start_command(update, context):

    # Replying to the start command, with a simple string
    update.message.reply_text('Welcome to the Selendrian Blockchain Bot')

# Creating a help command 
def help_command(update, context):

    # Displaying all useful commands
    update.message.reply_text('Here is a list of helpful commands: \n "/start" has been done!')

# creating the main function
def main():
    
    # Stats checking for user input
    updater = Updater(keys.API_KEY, use_context=True)
    # variable for output disbatching
    dp = updater.dispatcher

    # Linking /start to the start_command
    dp.add_handler(CommandHandler("start", start_command))
    # linking /help to the help_command
    dp.add_handler(CommandHandler("help", help_command))

    # setting the update refresh 'null' speed, to define the frequency in which the bot searches for user input (0 refresh = update ever 0.01 seconds)
    updater.start_polling()
    # Setting 'null' timeout so the bot is always active
    updater.idle()

# Calling the main function
main()












