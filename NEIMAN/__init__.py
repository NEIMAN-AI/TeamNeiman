from pyrogram import Client
from config import API_ID, API_HASH, SUDO_USERS, OWNER_ID, BOT_TOKEN, SESSION
from datetime import datetime
import time
from aiohttp import ClientSession

StartTime = time.time()
START_TIME = datetime.now()
CMD_HELP = {}
SUDO_USER = SUDO_USERS
clients = []
ids = []

SUDO_USERS.append(OWNER_ID)
aiosession = ClientSession()

if API_ID:
   API_ID = API_ID
else:
   print("WARNING: API ID NOT FOUND USING RADHA API ⚡")
   API_ID = "27995073"

if API_HASH:
   API_HASH = API_HASH
else:
   print("WARNING: API HASH NOT FOUND USING RADHA API ⚡")   
   API_HASH = "f57594c795197deecde36a56cc9623a6"

if not BOT_TOKEN:
   print("WARNING: BOT TOKEN NOT FOUND PLZ ADD ⚡")   

app = Client(
    name="app",
    API_ID=API_ID,
    API_HASH=API_HASH,
    BOT_TOKEN=BOT_TOKEN,
    plugins=dict(root="NEIMAN/modules/bot"),
    in_memory=True,
)

if SESSION:
   print("Client1: Found.. Starting..⚡")
   client1 = Client(name="one", API_ID=API_ID, API_HASH=API_HASH, SESSION=SESSION, plugins=dict(root="NEIMAN/modules"))
   clients.append(client)
