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
BOT_TOKEN = "6548950876:AAHNOrnrodvniHVpKB9rfbQrB-0bhX4eOkQ"
SESSION = "BQAcnHL4z53W5wmF1OriudohzXhTJ3DK-Iy22SNwXyFf-t68ybIREEF8Dr3QYY7-8p-wgPKXFceGQ7Lx8KCecUQ9x1TEOwwDKGczrLxzXwMXy6N4ewf3XB6nqP4YN6o8INQNr65Pprhqckg99_Kz33WbaSq2wpP80YSjlOwtHBBtivMSj7uCdlJ-dhrxojA3xgtpClZRsW6LhR3T8uH9XZl-r5a3yMQt02rr2T9v68CvSG7gOfYYM9nfKfk2VX-18yznrd-QPmPlONQ06Wo_e7S-btGbPgH4rd4uCYMPZRR1Kn5VWdRKCPEGtQqEDYLJT2TaiK6z58O1Ohn1paO8tCoAAAAAAZTVflsA"
FORCESUB = "bottgod"
AUTH = 6791986779

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
