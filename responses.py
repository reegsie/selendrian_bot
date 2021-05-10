#!/usr/bin/python

from datetime import datetime

def main_listener(input_text):
    
    # Taking user input
    user_message = str(input_text).lower()
    # takes the first char's of the user_message to verify bot tagged T / F
    # tag = user_message[0:14]
    # Saves the str after char 14 for the user query to the bot
    # user_query = user_message[14:65]

    # Price & Listing queries
    if "not" in user_message:
        pass
    if "aren't" in user_message:
        pass
    else:
        if "list" in user_message:
            return "Token won't be listed on any exchange until around late August or worst Nov 2021. The reason is that we more people to be able to claim SEL Airdrop. If this is too long for anyone to wait, feel free to burn your SEL :)\n \n$SEL will be on #Pancakeswap, #BitrielSwap, #LAToken, and #Binance. We will work with a small number of exchanges."
        if "price" in user_message:
            return "On behalf Selendra team, we would like to present the whitepaper with roadmaps around the 15th of May. There have been some delayed.\n \nToken won't be listed on any exchange until around late August or worst Nov 2021. The reason is that we more people to be able to claim SEL Airdrop. If this is too long for anyone to wait, feel free to burn your SEL :)\n \n$SEL will be on #Pancakeswap, #BitrielSwap, #LAToken, and #Binance. We will work with a small number of exchanges. "
        if "listed" in user_message:
            return "Token won't be listed on any exchange until around late August or worst Nov 2021. The reason is that we more people to be able to claim SEL Airdrop. If this is too long for anyone to wait, feel free to burn your SEL :)\n \n$SEL will be on #Pancakeswap, #BitrielSwap, #LAToken, and #Binance. We will work with a small number of exchanges."
        if "listing" in user_message:
            return "Token won't be listed on any exchange until around late August or worst Nov 2021. The reason is that we more people to be able to claim SEL Airdrop. If this is too long for anyone to wait, feel free to burn your SEL :)\n \n$SEL will be on #Pancakeswap, #BitrielSwap, #LAToken, and #Binance. We will work with a small number of exchanges."
        else:
            pass
