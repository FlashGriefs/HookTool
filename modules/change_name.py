import colorama
import requests
import configparser

blue = colorama.Fore.BLUE
grey = colorama.Fore.LIGHTBLACK_EX
green = colorama.Fore.GREEN
white = colorama.Fore.WHITE
red = colorama.Fore.RED

def change_webhook_name():
    try:
        new_webhook_name = input(f"{grey}[{green}New Webhook Name{grey}]{white} ")
        config = configparser.ConfigParser()
        config.read('config.ini')
        webhook = config['MAIN']['webhook']
        response = requests.patch(webhook, headers={'Content-Type': 'application/json'}, json={'name': new_webhook_name})
        if response.ok:
            print (f"{grey}[{green}Success{grey}]{white} Changed webhook's name to {new_webhook_name}")
            print ("Press enter to continue...")
            input()
        else:
            print (f"{grey}[{red}Error {response.status_code}{grey}]{white} Failed to change name of webhook {webhook}.")
            print ("Press enter to continue...")
            input()
    except KeyboardInterrupt:
        return