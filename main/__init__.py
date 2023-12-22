#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 22789024
API_HASH = "05dd73c56053828044cb71216cdfd0cc"
BOT_TOKEN = "6264659307:AAGdnlY-dsH8MlSZxYwUZI1nRBb6_wXoIy0"
SESSION = "BQCs0pQI9dgvv3VYhaBqWVwm61uulqAo9vskX5LWqjei7fOgsuMrXU636w5IzT8aJ0_LXa0v5b-7hY6XJWoX5JJlkjyNYnM-_P8ZhDs318UHruJTlB03JgzNY8DODqKgQrZ0Jlow_r6dNK0cXmcvb5QdMNWGtiiY95qcUnVAJKuc4rmec7c4Loxh6PQfnJpQShoZXXhraw2lbQGjz1ij637i0HfR1bwA7A1_Sv5QIVfcQhpZdENAlw4ucU87oLa9BsSLPXa0JxcODfQL4E0v9rdPXEPj85LK7jqfTHRb0vr2oHUFnRKGFJXcnedi44sbzD-Q1dfdAeX4spfEhMLsY6G7AAAAAZjIa14A"
FORCESUB = "bot01test"
AUTH = 6858238814

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
