import colorama
import requests
import configparser
import base64
from modules import menu, clear

blue = colorama.Fore.BLUE
grey = colorama.Fore.LIGHTBLACK_EX
green = colorama.Fore.GREEN
white = colorama.Fore.WHITE
red = colorama.Fore.RED

def change_webhook_avatar():
    try:
        clear()
        menu()
        print (f"""           {grey}[{green}1{grey}]{white} Use URL in settings
           {grey}[{green}2{grey}]{white} Input file path
           """)
        option = int(input(f"{grey}[{green}Choice{grey}] {white}"))
        config = configparser.ConfigParser()
        config.read('config.ini')
        webhook = config['MAIN']['webhook']
        if option == 1:
            image_url = config['MAIN']['webhook_avatar']
            response = requests.get(image_url)
            if response.ok:
                image = response.content
                avatar = base64.b64encode(image).decode('utf-8')
                response = requests.patch(webhook, headers={'Content-Type': 'application/json'}, json={'avatar': f"data:image/png;base64,{avatar}"})
                if response.ok:
                    print (f"{grey}[{green}Success{grey}]{white} Changed webhook's avatar to {image_url}")
                    print ("Press enter to continue...")
                    input()
                else:
                    print (f"{grey}[{red}Error {response.status_code}{grey}]{white} Failed to change avatar of webhook {webhook}.")
                    print ("Press enter to continue...")
                    input()
            else:
                print (f"{grey}[{red}Error {response.status_code}{grey}]{white} Failed to fetch image from url {image_url}.")
                print ("Press enter to continue...")
                input()
        if option == 2:
            file_path = input(f"{grey}[{green}Input File Path{grey}]{white} ")
            with open(file_path, 'rb') as image_file:
                avatar = base64.b64encode(image_file.read()).decode('utf-8')
            response = requests.patch(webhook, headers={'Content-Type': 'application/json'}, json={'avatar': f"data:image/png;base64,{avatar}"})
            if response.ok:
                print (f"{grey}[{green}Success{grey}]{white} Changed webhook's avatar to {file_path}")
                print ("Press enter to continue...")
                input()
            else:
                print (f"{grey}[{red}Error {response.status_code}{grey}]{white} Failed to change avatar of webhook {webhook}.")
                print ("Press enter to continue...")
                input()
    except KeyboardInterrupt:
        return