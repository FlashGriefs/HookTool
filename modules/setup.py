import os

def setup():
    if not os.path.exists('config.ini'):
        with open('config.ini', 'w') as file:
            file.write("""[MAIN]
webhook = YOUR_WEBHOOK
webhook_name = HookTool
webhook_avatar_bool = True
webhook_avatar = https://raw.githubusercontent.com/FlashGriefs/HookTool/main/HookTool.png""")