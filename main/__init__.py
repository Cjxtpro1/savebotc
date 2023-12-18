#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 23147177
API_HASH = "6c1b34bf3c56b9957aab7da8a0dd3482"
BOT_TOKEN = "6790061721:AAGwP3F_8c6qWzOL1s8IChZ8eQ9P2odw46g"
SESSION = "BQAtKoH9Uf2vsGz-7SQQubDZbsbvRrtlQHEG6PDOP7qIlpzwDjn77MPVoPNFQ1h8l9fP6qR6sAKpXgsfLzUAdy8XLCGM-psc-y6JKE73OabYl0IQyjLtDlALlK_YEAgAPSXU0YQUswgUYbLdMlr68KzhQ2M9OhTzxBZUQ5WmPHJIYYscGYbMqhp1AZzGMrdeYdI2tprEI23ttrgPn9aDSoZHNiBdzmmM0zwc2ip9Q0EPYDYYPfEHUa2E-pSId9GyGZ1aon_XQwgtWXp8fSIBtDlNXbMioWA-wcNK6B2wY9IMwVxS_Bj7KruKrdG_Y-UFhdeWJx5VrkWYfjXI3DA65se4AAAAAY1EGMoA"
FORCESUB = "botlogod"
AUTH = 6665017546

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
