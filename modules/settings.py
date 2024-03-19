import colorama
import configparser
import tkinter
from tkinter import messagebox
import sys
from modules import menu, clear

blue = colorama.Fore.BLUE
grey = colorama.Fore.LIGHTBLACK_EX
green = colorama.Fore.GREEN
white = colorama.Fore.WHITE
red = colorama.Fore.RED

def read_config():
    config = configparser.ConfigParser()
    config.read('config.ini')
    print (f"{grey}[{green}Webhook{grey}]{white}", config['MAIN']['webhook'])
    print (f"{grey}[{green}Webhook Name{grey}]{white}", config['MAIN']['webhook_name'])
    print (f"{grey}[{green}Custom Webhook Avatar Enabled{grey}]{white}", config['MAIN']['webhook_avatar_bool'])
    print (f"{grey}[{green}Webhook Avatar URL{grey}]{white}", config['MAIN']['webhook_avatar'])

def change_webhook_name():
    config = configparser.ConfigParser()
    config.read('config.ini')
    print (f"{grey}[{green}Webhook Name{grey}]{white}", config['MAIN']['webhook_name'])
    new_webhook_name = input(f"{grey}[{green}New Webhook Name{grey}] {white}")
    config['MAIN']['webhook_name'] = new_webhook_name
    with open('config.ini', 'w') as configfile:
        config.write(configfile)
    config.read('config.ini')
    print(f"{grey}[{green}Success{grey}] {white}Changed webhook name to", config['MAIN']['webhook_name'])

def change_webhook():
    config = configparser.ConfigParser()
    config.read('config.ini')
    print (f"{grey}[{green}Webhook{grey}{white}]", config['MAIN']['webhook'])
    new_webhook = input(f"{grey}[{green}New Webhook{grey}] {white}")
    config['MAIN']['webhook'] = new_webhook
    with open('config.ini', 'w') as configfile:
        config.write(configfile)
    config.read('config.ini')
    print(f"{grey}[{green}Success{grey}] {white}Changed webhook to", config['MAIN']['webhook'])

def change_webhook_avatar():
    config = configparser.ConfigParser()
    config.read('config.ini')
    use_custom_avatar = input(f"{grey}[{green}Use Custom Avatar? (Y/N){grey}]{white} ")
    if use_custom_avatar.strip().lower() == 'y':
        config['MAIN']['webhook_avatar_bool'] = 'True'
        print (f"{grey}[{green}Webhook Avatar URL{grey}]", config['MAIN']['webhook_avatar'])
        new_webhook_avatar = input(f"{grey}[{green}New Webhook Avatar URL{grey}] {white}")
        config['MAIN']['webhook_avatar'] = new_webhook_avatar
        with open('config.ini', 'w') as configfile:
            config.write(configfile)
        config.read('config.ini')
        print(f"{grey}[{green}Success{grey}] {white}Changed webhook avatar to", config['MAIN']['webhook_avatar'])
    elif use_custom_avatar.strip().lower() == 'n':
        config['MAIN']['webhook_avatar_bool'] = 'False'
        with open('config.ini', 'w') as configfile:
            config.write(configfile)
        print (f"{grey}[{green}Success{grey}]{white} Disabled Custom Webhook Avatar")
    else:
        root = tkinter.Tk()
        root.withdraw()
        root.attributes('-topmost', 1)
        messagebox.showerror("BRUH", "I asked you a simple Y/N question.")
        messagebox.showerror("BRUH", "And you give me this shit?")
        messagebox.showerror("BRUH", f"Like wtf is \"{use_custom_avatar}\"")
        messagebox.showerror("BRUH", "Nah im out.")
        sys.exit(0)

options = {
    1: read_config,
    2: change_webhook,
    3: change_webhook_name,
    4: change_webhook_avatar,
}

def settings():
    clear()
    menu()
    print (f"""           {grey}[{green}1{grey}]{white} Read Config
           {grey}[{green}2{grey}]{white} Webhook
           {grey}[{green}3{grey}]{white} Webhook Name
           {grey}[{green}4{grey}]{white} Webhook Avatar URL
           """)
    settings_options()

def settings_options():
    try:
        option = int(input(f"{grey}[{green}Choice{grey}] {white}"))
        if option in options:
            options[option]()
            settings_options()
        else:
            print(f"{grey}[{red}Error{grey}] {white}Invalid Option")
    except ValueError:
        print(f"{grey}[{red}Error{grey}] {white}Invalid Option")
    except KeyboardInterrupt:
        return