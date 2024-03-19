import colorama
import subprocess
import time
import os

blue = colorama.Fore.BLUE
grey = colorama.Fore.LIGHTBLACK_EX
green = colorama.Fore.GREEN
white = colorama.Fore.WHITE
red = colorama.Fore.RED

def menu():
    print (f"""{blue}
                                     _  _               _     _____               _ 
                                    | || |  ___   ___  | |__ |_   _|  ___   ___  | |
                                    | __ | / _ \ / _ \ | / /   | |   / _ \ / _ \ | |
                                    |_||_| \___/ \___/ |_\_\   |_|   \___/ \___/ |_|
                                                 
           """)
    

def clear():
    if os.name == "nt":
        subprocess.Popen("cls", shell=True)
        time.sleep(0.1)
    else:
        print("\033c")
        time.sleep(0.1)