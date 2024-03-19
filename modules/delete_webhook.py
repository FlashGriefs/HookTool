import colorama
import requests
import configparser

blue = colorama.Fore.BLUE
grey = colorama.Fore.LIGHTBLACK_EX
green = colorama.Fore.GREEN
white = colorama.Fore.WHITE
red = colorama.Fore.RED

def delete_webhook():
    try:
        confirm = input(f"{grey}[{green}Are you sure you want to delete the webhook? (Y/N){grey}]{white} ")
        if confirm.strip().lower() == 'y':
            config = configparser.ConfigParser()
            config.read('config.ini')
            webhook = config['MAIN']['webhook']
            response = requests.delete(webhook)
            if response.ok:
                print (f"{grey}[{green}Success{grey}]{white} Deleted webhook {webhook}")
                print ("Press enter to continue...")
                input()
            else:
                print (f"{grey}[{red}Error {response.status_code}{grey}]{white} Failed to delete webhook {webhook}.")
                print ("Press enter to continue...")
                input()
        else:
            return
    except KeyboardInterrupt:
        return