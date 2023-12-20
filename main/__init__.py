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
SESSION = "BQAeo2HYz5Fw8y-LmdJupal09gw-wGVlXEleg1JJ7wf5JGN27xgmhLkIGi02nCgbtP10GGnW8xrIxTCE5cbI8UbE6_zmhC_bYKtyMAgj7KdNvo3uptDr24JoFrYey6Zdi2KaNRXO_IlBEbbw6zba3CCZ3XPxLSKHfLaUhH2cxsycWQNnLwCHnieYpagQFNG_QrDsEhWFyfSmc86CzCMhISk8hFk5PfvzbR1Qbagpwx-OdZrZgfRB1GjcNRNiXck-rWMRDShqUtV6NVRJ1qk5DflVAwdNpkaKhaZok_omcNAFowN1HCKZSQjzw3M6dgrdy3xq_KiMByIRuT_bHwBIy-ZmAAAAAY1EGMoA"
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
