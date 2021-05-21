#!/usr/bin/python

from datetime import datetime
from long_str import *

def main_listener(input_text):
    
    # Taking user input
    user_message = str(input_text).lower()
    # takes the first char's of the user_message to verify bot tagged T / F
    # tag = user_message[0:14]
    # Saves the str after char 14 for the user query to the bot
    # user_query = user_message[14:65]
    
    #what is
    if "what" in user_message:
        if "is" in user_message:
            if "selendra" in user_message:
                return "Selendra is a multi-sharding Blockchain network focus on empowering developers to build real world Apps/Dapps for Web 3.0."
    
    # Price & Listing queries
    if "price" in user_message:
        if "what" in user_message:
            return "We don't encourage conversation about price in the community, howver we do have a chat specifically for Selendra price discussion. 'https://t.me/seltrade' "
    else: pass
    
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
    if "received" in user_message:
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
            return "0x288d3A87a87C284Ed685E0490E5C4cC0883a060a"
        else:
            pass     
    if "sc" in user_message:
        if "what" in user_message:
            if "is" in user_message:
                return "Here is the secure contract address: 0x288d3A87a87C284Ed685E0490E5C4cC0883a060a"
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
    else:
        pass
    if "when" in user_message:
        if "listed" in user_message: 
            return "Token won't be listed on any exchange until around late Ausgust or worst Nov 2021. The reason is that we more p[eople to b e able to claimn SEL Airdrop. If this is too long for anyone to wait, feel free to brn your SEL :) \n \n$SEL will be on #Pancakeswap, #BitrielSwap, #LAToken, and #Binance. We will work with a small number of exchanges."
    else:
        pass
    
    # Forgot password
    if "password" in user_message:
        if "forgot" in user_message:
            return "Once you have lost your 12 word passphrase in bitriel, you won't be able to recover your account afterwards."
        else: 
            pass
        
    # Airdrop query
    if "airdrop" in user_message: 
        if "when" in user_message: 
            return "We will conduct 3 airdrops, each drop will have 6 sessions of 31,415,927 SEL tokens over the span of 4.5 years. Each session will last as long as 3 months. Use '/distribution' to see active airdrops, use '/airdrop' for more info on airdrops."
        
    # withdraw messages
    if "how" in user_message:
        if "withdraw" in user_message:
            return "$SEL does not currently support withdrawls, in the mean time you can:\n\n- Invite your friends to join the community. Tell them to go claim SEL on airdrop.selendra.org\n- Discuss ideas and think of way to build dapps on Selendra by using docs.selendra.org, if you are a developer."
        else: 
            pass   
    
    # Random messages
    if "when" in user_message:
        if "moon" in user_message:
            return "Ladies and gentlman please fasten your seatbelts and siten your caps, we're just starting our engines, take off in 3... 2..."  
    else: 
        pass
    
    #transaction info
    if "transaction" in user_message:
        if "fee" in user_message:
            return trans_fee
    
    if "left" in user_message:
        return "Group_Message has been logged."
    else:
        pass

# Notes for future integration
# > Add link denial | if the link doesn't come from admin, delete it

    # what
    if "what" in user_message:
        if "total" in user_message:
            if "supply" in user_message:
                return benefits
        if "tokens" in user_message:
            if "distribution" in user_message:
                if "model" in user_message:
                    return benefits
        if "benefits" in user_message:
            if "from" in user_message:
                if "project" in user_message:
                    return benefits
        if "algorithm" in user_message:
            if "blockchain" in user_message:
                if "use" in user_message:
                    return algorithm_text
            if "selendra" in user_message:
                if "use" in user_message:
                    return algorithm_text
        if "transaction" in user_message:
            if "fees" in user_message:
                return trans_fee
        if "transaction" in user_message:
            if "fee" in user_message:
                return trans_fee
        if "consensus" in user_message:
            if "roles" in user_message:
                return consensus
            if "role" in user_message:
                return consensus
        if "governance" in user_message:
            if "roles" in user_message:
                return governance
            if "role" in user_message:
                return governance
    else:
        pass
    
    # how
    if "how" in user_message:
        if "does" in user_message:
            if "reward" in user_message:
                return benefits
        if "do" in user_message:
            if "reward" in user_message:
                return benefits
        if "tokens" in user_message:
            if "distributed" in user_message:
                return benefits
    else:
        pass
    
    # Where 
    if "where" in user_message:
        if "find" in user_message:
            if "info" in user_message:
                return more_info
            if "information" in user_message:
                return more_info
    else:
        pass
    
