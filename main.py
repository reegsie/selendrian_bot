#! /usr/bin/python

import constants as keys
import responses as R
from telegram.ext import *

# Marking the beginning of the converstation 
print ("Bot session has begun")

# Adding a start command so users and start a converstation
def distro_command(update, context):

    # Replying to the distro command, with a simple string
    update.message.reply_text('Currently there are no active airdrops on my Radar! \n\nYou can visit "airdrop.selendra.org" for more information')

# Creating a help command 
def help_command(update, context):

    # Displaying all useful commands
    update.message.reply_text('Here is a list of helpful commands: \n\n -/airdrop Up to date info on airdrops\n-/distro Airdrop disrobution status\n')

def airdrop_command(update, context):
    update.message.reply_text('Hey there watch your head, selendra airdrops are inbound. To chek on the airdrop disrobution status "/distro" to get any more information about the airdrop "aridrop.selendra.org".')

def handle_message(update, context):
    text = str(update.message.text).lower()
    response = R.main_listener(text)

    update.message.reply_text(response)

def error(update, context):

    print(f"Update {update} caused error {context.error}")

# creating the main function
def main():
    
    # Stats checking for user input
    updater = Updater(keys.API_KEY, use_context=True)
    # variable for output disbatching
    dp = updater.dispatcher
    
    # linking /help to the help_command
    dp.add_handler(CommandHandler("help", help_command))
    # linking /distro to the help_command
    dp.add_handler(CommandHandler("distro", distro_command))
    # linking /airdrop to the help_command
    dp.add_handler(CommandHandler("airdrop", airdrop_command))

    dp.add_handler(MessageHandler(Filters.text, handle_message))

    dp.add_error_handler(error)

    # setting the update refresh 'null' speed, to define the frequency in which the bot searches for user input (0 refresh = update ever 0.01 seconds)
    updater.start_polling()
    # Setting 'null' timeout so the bot is always active
    updater.idle()

# Calling the main function
main()












