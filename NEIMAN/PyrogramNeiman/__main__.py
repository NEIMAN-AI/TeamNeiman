import glob
import os
import sys
from pathlib import Path

from NeimanConfig import Config

from PyrogramNeiman.clients.logger import LOGGER as LOGS
from PyrogramNeiman.clients.session import H2, H3, H4, H5, Neiman, NeimanBot
from PyrogramNeiman.utils.plug import load_module, plug_channel
from PyrogramNeiman.utils.startup import (join_it, logger_check, start_msg,
                                        update_sudo)
from PyrogramNeiman.version import __Neimanver__


NEIMAN_PIC = "https://te.legra.ph/file/824d87ea204e4bf78619c.jpg"


# Client Starter
async def Neimans(session=None, client=None, session_name="Main"):
    num = 0
    if session:
        LOGS.info(f"••• Starting Client [{session_name}] •••")
        try:
            await client.start()
            num = 1
        except:
            LOGS.error(f"Error in {session_name}!! Check & try again!")
    return num


async def plug_load(path):
    files = glob.glob(path)
    for name in files:
        with open(name) as Neiman:
            path1 = Path(Neiman.name)
            shortname = path1.stem
            if shortname.replace(".py", "") in Config.UNLOAD:
                os.remove(Path(f"PyrogramNeiman/plugins/{shortname}.py"))
            else:
                load_module(shortname.replace(".py", ""))


# Final checks after startup
async def Neiman_is_on(total):
    await update_sudo()
    await logger_check(Neiman)
    await start_msg(NeimanBot, NEIMAN_PIC, __Neiamnver__, total)
    await join_it(Neiman)
    await join_it(H2)
    await join_it(H3)
    await join_it(H4)
    await join_it(H5)


# Hellbot starter...
async def start_Neimanbot():
    try:
        tbot_id = await NeimanBot.get_me()
        Config.BOT_USERNAME = f"@{tbot_id.username}"
        Neiman.tgbot = NeimanBot
        LOGS.info("••• Starting NeimanBot (PYROGRAM) •••")
        C1 = await Neimans(Config.SESSION, Neiman, "SESSION")
        C2 = await Neimans(Config.SESSION_2, H2, "SESSION_2")
        C3 = await Neimans(Config.SESSION_3, H3, "SESSION_3")
        C4 = await Neimans(Config.SESSION_4, H4, "SESSION_4")
        C5 = await Neimans(Config.SESSION_5, H5, "SESSION_5")
        await NeimanBot.start()
        total = C1 + C2 + C3 + C4 + C5
        LOGS.info("••• NeimanBot Startup Completed •••")
        LOGS.info("••• Starting to load Plugins •••")
        await plug_load("PyrogramNeiman/plugins/*.py")
        await plug_channel(Hell, Config.PLUGIN_CHANNEL)
        LOGS.info("🔥 Your NeimanBot Is Now Working 🔥")
        LOGS.info("join to @TeamNeiman for Updates.")
        LOGS.info(f"» Total Clients = {str(total)} «")
        await Neiman_is_on(total)
    except Exception as e:
        LOGS.error(f"{str(e)}")
        sys.exit()


Neiman.loop.run_until_complete(start_Neimanbot())

if len(sys.argv) not in (1, 3, 4):
    Neiman.disconnect()
else:
    try:
        Neiman.run_until_disconnected()
    except ConnectionError:
        pass
