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
SESSION = "BQFbu6AABc1jBy4qdVDpfpZfIs9aKxiNDrgfVxUBKLpKPUofpF9oO7oND_cAICzL26UGSdZtw8TuPIcectjEKp40ygWYJpex4WA0PnIGyb9UsZIfHgCsb4Y0VkPhvuCTltGGetgJgkQBm1j-uwuW8BULdvohRWPDQnaliq6lFTxRXVSW-i9h7oAJeSdSC7mBSm5RWQfKMjz1P-ySV_sDakJWPOlwTNf06ICQSiphoWZuf7wr_FlJeNYYUDHWdvc1nx9IhGhdJsMiV7DLyZE2JXyu9OwHfiCkBki8iF857P0FVJCDPdHHZfo238NDdGRMFCTFUi9j9ausFrjxzOUYstP6B8o6_QAAAAGU1X5bAA"
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
