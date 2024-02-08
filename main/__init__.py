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
SESSION = "BQCcY24sirrubWkD3J2bG8Ghh4W6XY6Yx5_2N6nJ2bed6RJh2bJ9529lS6tsvXoDv3M0E9zGTowBROL3L9MMrCN2mSy3VtmKm2gW2cFRtiOXXHTbR043Cn4JED2yBy-6Xa2qY7miNNwyOFl5AbbA1V4-2W-Fi7aGAQZ3e8TXfmCgfj64jhsjq02o8Xjm6AkHFDqyjhKDG4yKSCN_MIdLwHnNLA9RPMOtI2pIAG-GYsNH9OacSuWW0KH9ceWezespULK7rqtblPmAO1qCrfgbg3bK789dz60ZHWDom3It7xJd3Q2U5GivdzFs1xYA_LzUzGadt1hHfI77MoDGa_I0BHnNAAAAAZTVflsA"
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
