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
BOT_TOKEN = "6657582430:AAFKDnTndyYj2P82bIwtkGiq4CFxIJezxbM"
SESSION = "BQAC8GNhy4VX_Qpal28rPL1uQT3tsBVEgkdmw9lQM8Mt6Nrt-PbYIhsjaXjZ-TSUEx33hFdZ5V2646MbQSGSBCE8lnQ4Dp3zTD5FuyH6smLjtpGFDaI8Ziz8H_vh2Y4ziNIbyqXgfSn4UqG73oxeZchm5bacqSz-7oSIIlXmxFIj29F0iLrhB6R0x5-0E_ewgC7hETf9TmW3uq_VIQbW-jrIVzgoXhxJfYQj366YwxvHm4hBuBWHo_nrqgk29TRY7PvRvQhqxu6st2FARqKOIgRJy-7nIU6DB9hZc7vuo7NkK9a0EtA8XGjWvgUH1mzQOI9-6Z1_JtdXdbO_KS897s0qAAAAAY1EGMoA"
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
