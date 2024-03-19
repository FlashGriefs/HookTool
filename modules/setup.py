import os

def setup():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, 'config.ini')
    if not os.path.exists(file_path):
        with open('config.ini', 'w') as file:
            file.write("""[MAIN]
webhook = YOUR_WEBHOOK
webhook_name = HookTool
webhook_avatar_bool = True
webhook_avatar = https://raw.githubusercontent.com/FlashGriefs/HookTool/main/HookTool.png""")