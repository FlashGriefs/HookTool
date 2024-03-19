import colorama
import requests
import configparser
from modules import clear, menu

blue = colorama.Fore.BLUE
grey = colorama.Fore.LIGHTBLACK_EX
green = colorama.Fore.GREEN
white = colorama.Fore.WHITE
red = colorama.Fore.RED

def send_messages():
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
            message = input(f"{blue}>>> {white}")
            if webhook_avatar_bool == 'False':
                response = requests.post(webhook, {"content": f"{message}", "username": f"{webhook_name}"})
            elif webhook_avatar_bool == 'True':
                response = requests.post(webhook, {"content": f"{message}", "username": f"{webhook_name}", "avatar_url": f"{webhook_avatar}"})
            if response.ok:
                print(f"{grey}[{green}Success{grey}] {white}Sent {message} to webhook.")
            else:
                print(f"{grey}[{red}Error{grey}] {white}{response.status_code}")
    except KeyboardInterrupt:
        return