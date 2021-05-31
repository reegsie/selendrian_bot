#!/usr/bin/python

from datetime import datetime
from long_str import *

def main_listener(input_text):
    
    # Taking user input
    user_message = str(input_text).lower()
    
    # who is selendrian
    if "selendrian" in user_message:
        if "who" in user_message:
            return "I am your virtual assistant for all things related to the Selendra Blockchain project :-)"
    
    #what is
    if "what" in user_message:
        if "price" in user_message:
            pass
        else:
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
    
    # Recieved no airdrop
    if "received" in user_message:
        if "nothing" in user_message:
            return "Hello, there could be a number of reasons why you haven't received your airdrop yet.\n \n1. Make sure you have filled in all of your information correctly when applying for the airdrop. (You can re-do the form if you have input false information.)\n \n2. Airdrops Distribution may still be running use '/distro' to see the active distribution status."
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
            return "Token won't be listed on any exchange until around late August or November 2021. The reason is that we need more p[eople to b e able to claim SEL Airdrop. If this is too long for anyone to wait, feel free to burn your SEL :) \n \n$SEL will be on #Pancakeswap, #BitrielSwap, #LAToken, and #Binance. We will work with a small number of exchanges."
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
            return forgot_pass
        else: 
            pass
        
    # Airdrop query
    if "airdrop" in user_message: 
        if "when" in user_message: 
            return "We will conduct 3 airdrops, each drop will have 6 sessions of 31,415,927 SEL tokens over the span of 4.5 years. Each session will last as long as 3 months.\n\nUse '/distribution' to see active airdrops, use '/airdrop' for more info on airdrops."
        else:
            pass
        
    if "completed" in user_message:
        if "form" in user_message:
            if "nothing" in user_message:
                return ad_troubeshoot
    # withdraw messages
    if "how" in user_message:
        if "withdraw" in user_message:
            return "$SEL does not currently support withdrawls, in the mean time you can:\n\n- Invite your friends to join the community. Tell them to go claim SEL on airdrop.selendra.org\n\n- Discuss ideas and think of way to build dapps on Selendra by using docs.selendra.org, if you are a developer."
        else: 
            pass   
    
    # Random messages
    if "when" in user_message:
        if "moon" in user_message:
            return "Ladies and gentlman please fasten your seatbelts and siten your caps, we're just starting our engines, take off in 3... 2..."  
    else: 
        pass
    
    if "anyone" in user_message:
        if "want" in user_message:
            if "buy" in user_message:
                return sell
            
    
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
                return supply
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
        if "presale" in user_message:
            if "going" in user_message:
                if "happen" in user_message:
                    return presale
            if "start" in user_message:
                return presale
        if "is" in user_message:
            if "secure" in user_message:
                if "contract" in user_message:
                    return sc
        
    else:
        pass
    
    # how
    if "how" in user_message:
        if "does" in user_message:
            if "reward" in user_message:
                return rewards
        if "do" in user_message:
            if "reward" in user_message:
                return rewards
        if "tokens" in user_message:
            if "distributed" in user_message:
                return rewards
        if "recieve" in user_message:
            if "token" in user_message:
                return claim_vids
        if "register" in user_message:
            if "for" in user_message:
                if "airdrop" in user_message:
                    return claim_vids
        if "apply" in user_message:
            if "airdrop" in user_message:
                return claim_vids
    else:
        pass
    
    # Where 
    if "where" in user_message:
        if "find" in user_message:
            if "info" in user_message:
                return more_info
            if "information" in user_message:
                return more_info
        if "get" in user_message:
            if "info" in user_message:
                return more_info
            if "information" in user_message:
                return more_info
        if "read" in user_message:
            if "info" in user_message:
                return more_info
            if "information" in user_message:
                return more_info
    else:
        pass
    
    # Who
    if "who" in user_message:
        if "everything" in user_message:
            if "nothing" in user_message:
                return failed
            
    #when
    if "when" in user_message:
        if "presale" in user_message:
            if "going" in user_message:
                if "happen" in user_message:
                    return presale
            if "start" in user_message:
                return presale
    
    # single words
    if len(user_message) <= 6:
        if "price" in user_message:
            return "Hi there, we don't permit 'price' talk in this group, if you want you can go to this channel: https://t.me/seltrade for price talk :-)" 
        if "sc" in user_message:
            return "0x288d3A87a87C284Ed685E0490E5C4cC0883a060a"
    if len(user_message) <= 14:
        if "smartcontract" in user_message:
            return sc
    else:
        pass
    
    if "hello" in user_message:
        return "Hi welcome to the Selendra Blockchain Community, /help if you need help!"
    if len(user_message) <= 2:
        if "hi" in user_message:
            return "Hi welcome to the Selendra Blockchain Community, /help if you need help!"
        
    if "is" in user_message:
        if "selendra" in user_message:
            return "Yes it is, to read more '/whitepaper'"
        if "sel" in user_message:
            return "Yes it is, to read more '/whitepaper'"
        else:
            pass
        
    if len(user_message) <= 5:
        if "help" in user_message:
            return "You can use /help for a list of helpful commands, or ask your question here and I will do my best to answer it."
        
    if len(user_message) <= 11:
        if "consensus" in user_message:
            return consensus
    
    if len(user_message) <= 12:
        if "governence" in user_message:
            return governance