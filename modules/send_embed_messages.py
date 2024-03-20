import colorama
import requests
import configparser
import json
from modules import clear, menu

blue = colorama.Fore.BLUE
grey = colorama.Fore.LIGHTBLACK_EX
green = colorama.Fore.GREEN
white = colorama.Fore.WHITE
red = colorama.Fore.RED

def send_embeds():
    try:
        clear()
        menu()
        config = configparser.ConfigParser()
        config.read('config.ini')
        webhook = config['MAIN']['webhook']
        webhook_name = config['MAIN']['webhook_name']
        webhook_avatar_bool = config['MAIN']['webhook_avatar_bool']
        webhook_avatar = config['MAIN']['webhook_avatar']
        while True:
            message = input(f"{grey}[{green}Text (Leave blank for none){grey}] {blue}>>> {white}")
            message = None if message == '' else message
            embed_title = input(f"{grey}[{green}Embed Title{grey}] {blue}>>> {white}")
            embed_description = input(f"{grey}[{green}Embed Description{grey}] {blue}>>> {white}")
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
            response = requests.post(webhook, json=data)
            if response.ok:
                print(f"{grey}[{green}Success{grey}] {white}Sent embed to webhook.")
            else:
                print(f"{grey}[{red}Error{grey}] {white}{response.text}")
    except KeyboardInterrupt:
        return