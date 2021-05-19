#!/usr/bin/python

from datetime import datetime

def main_listener(input_text):
    
    # Taking user input
    user_message = str(input_text).lower()
    # takes the first char's of the user_message to verify bot tagged T / F
    # tag = user_message[0:14]
    # Saves the str after char 14 for the user query to the bot
    # user_query = user_message[14:65]

    # Greetings
    if "hello" in user_message:
        return "Hi welcome to the Selendra Blockchain community if you need help try '/help'"
    if "hi" in user_message:
        return "Hi welcome to the Selendra Blockchain community if you need help try '/help'"
    # Price & Listing queries
    if "not" in user_message:
        if "listing" in user_message:
            pass
        
    # Sell request
    if "anyone" in user_message:
        if "buy" in user_message:
            if "my" in user_message:
                return "we recommend holding onto your SEL for now"
    else:
        pass 
    
    # Recieved no airdrop
    if "receive" in user_message:
        if "nothing" in user_message:
            return "Hello, there could be a number of reasons why you haven't received your airdrop yet.\n \n1. Make sure you have filled in all of your information correctly when applying for the airdrop. (You can re-do the form if you have input false information.)\n \n2. Airdrops distribution may still be running use '/distro' to see the active distribution status."
        else:
            pass
    if "airdrop" in user_message:
        if "still" in user_message:
            return "Hello there, you can use this command '/distro' to see if there is an airdrop currently running"
        else:
            pass
    
    # Bitriel bugs
    if "wallet" in user_message:
        if "stuck" in user_message:
            return ""
    
    # SC query
    if "sc" in user_message:
        if "please" in user_message:
            return ""
        else:
            pass     
    
    # Exchange the token
    if "exchange" in user_message:
        if "token" in user_message:
            return "Token won't be listed on any exchange until around late Ausgust or worst Nov 2021. The reason is that we more p[eople to b e able to claimn SEL Airdrop. If this is too long for anyone to wait, feel free to brn your SEL :) \n \n$SEL will be on #Pancakeswap, #BitrielSwap, #LAToken, and #Binance. We will work with a small number of exchanges."
        else:
            pass
    if "officially" in user_message:
        if "listed" in user_message: 
            return "Token won't be listed on any exchange until around late Ausgust or worst Nov 2021. The reason is that we more p[eople to b e able to claimn SEL Airdrop. If this is too long for anyone to wait, feel free to brn your SEL :) \n \n$SEL will be on #Pancakeswap, #BitrielSwap, #LAToken, and #Binance. We will work with a small number of exchanges."
    
    # Forgot password
    if "password" in user_message:
        if "forgot" in user_message:
            return "Once you have lost your 12 word passphrase in bitriel, you won't be able to recover your account afterwards."
        else: 
            pass
        
    if "left" in user_message:
        return "Group_Message has been logged."
    else:
        pass

# Notes for future integration
# > Add link denial | if the link doesn't come from admin, delete it