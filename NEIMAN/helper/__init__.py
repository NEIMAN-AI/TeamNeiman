import os
import sys
from pyrogram import Client



def restart():
    os.execvp(sys.executable, [sys.executable, "-m", "NEIMAN"])

async def join(client):
    try:
        await client.join_chat("TeamNeiman")
    except BaseException:
        pass
