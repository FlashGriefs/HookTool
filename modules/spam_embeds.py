import requests
import colorama
import configparser
import json
import time
from modules import menu, clear

blue = colorama.Fore.BLUE
grey = colorama.Fore.LIGHTBLACK_EX
green = colorama.Fore.GREEN
white = colorama.Fore.WHITE
red = colorama.Fore.RED

def spam_embed():
    try:
        message = input(f"{grey}[{green}Text (Leave blank for none){grey}] {blue}>>> {white}")
        message = None if message == '' else message
        embed_title = input(f"{grey}[{green}Embed Title{grey}] {blue}>>> {white}")
        embed_description = input(f"{grey}[{green}Embed Description{grey}] {blue}>>> {white}")
        spam_cooldown = float(input(f"{grey}[{green}Time Between Messages (in seconds){grey}]{white} "))
        config = configparser.ConfigParser()
        config.read('config.ini')
        webhook = config['MAIN']['webhook']
        webhook_name = config['MAIN']['webhook_name']
        webhook_avatar_bool = config['MAIN']['webhook_avatar_bool']
        webhook_avatar = config['MAIN']['webhook_avatar']
        data = {
                "username": f"{webhook_name}",
                "embeds": [{
                    "title": embed_title,
                    "description": embed_description,
                }],
                "username": webhook_name,
        }
        if webhook_avatar_bool == 'True':
                data["avatar_url"] = webhook_avatar
        if message:
            data["content"] = message
        while True:
            response = requests.post(webhook, json=data)
            if response.ok:
                print(f"{grey}[{green}Success{grey}] {white}Sent {message} to webhook.")
            else:
                print(f"{grey}[{red}Error{grey}] {white}{response.status_code}")
            time.sleep(spam_cooldown)
    except KeyboardInterrupt:
        return