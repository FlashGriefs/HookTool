import colorama
import sys
import os
from modules import menu
from modules import clear
from modules import settings
from modules import send_messages
from modules import spam_message
from modules import delete_webhook
from modules import change_webhook_name
from modules import change_webhook_avatar
from modules import setup

blue = colorama.Fore.BLUE
grey = colorama.Fore.LIGHTBLACK_EX
green = colorama.Fore.GREEN
white = colorama.Fore.WHITE
red = colorama.Fore.RED

options = {
    1: settings,
    2: send_messages,
    3: spam_message,
    4: delete_webhook,
    5: change_webhook_name,
    6: change_webhook_avatar,
}

def main():
    try:
        print(f"""            {grey}[{green}1{grey}]{white} Settings
            {grey}[{green}2{grey}]{white} Send Messages
            {grey}[{green}3{grey}]{white} Spam Message
            {grey}[{green}4{grey}]{white} Delete Webhook
            {grey}[{green}5{grey}]{white} Change Webhook's Name
            {grey}[{green}6{grey}]{white} Change Webhook's Avatar
            """)
        option = int(input(f"{grey}[{green}Choice{grey}] {white}"))
        if option in options:
            options[option]()
            clear()
            menu()
            main()
        else:
            print(f"{grey}[{red}Error{grey}] {white}Invalid Option")
    except ValueError:
        print(f"{grey}[{red}Error{grey}] {white}Invalid Option")
    except KeyboardInterrupt:
        print(f"\n{grey}[{green}Success{grey}]{red} Exiting.")
        sys.exit(0)

if os.name == 'nt':
    os.system('title HookTool')
else:
    sys.stdout.write(f"\033]0;HookTool\007")
    sys.stdout.flush()
setup()
clear()
menu()
main()