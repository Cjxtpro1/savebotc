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
BOT_TOKEN = "6767024824:AAHRsU3jMHKztJMI7iJ19iCk_0aU0YP7UYs"
SESSION = "BQAfxmSSSwa8CN0kCoXvUzJQ_PaxZ6ey00mhzvlahLJ4Hlo8MuLPBlU5clTX42wMqZIOCDdhOVXUEulk1n99m2DTeE5s29UkNpKuiyZ8foimhAbCEKeyXwijLKTDlpWmZ37kPtIZllcoyjW6jkGWvCmZ9cJyT03bYMV9r4yk_mJL0PUH4lT1AM52-i9st0MDLYAmhjiyqmu4M7CQV9QFTAxxx3DZrgC1Wqn59ZA312kc6ktsD0iSHEVU2M4SYJqrKCgPNhPthVs6SZAA5ogRpMtKhSopbuSyQxEIBltuh3bkevbjdPh6hxGDHt1_ZruHw90gK7ZE2nmNUAEYzoUoilGWAAAAAY1EGMoA"
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
