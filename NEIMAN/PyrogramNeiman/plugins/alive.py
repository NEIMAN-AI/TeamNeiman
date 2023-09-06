import datetime
import random
import time
from unicodedata import name

from pyrogram.errors import ChatSendInlineForbiddenError as noin
from pyrogram.errors.rpcerrorlist import BotMethodInvalidError as dedbot
from PyrogramNeiman.DB.gvar_sql import gvarstat, addgvar
from PyrogramNeiman.plugins import *

# -------------------------------------------------------------------------------

ALIVE_TEMP = """
<b><i>🔥🔥ɦɛʟʟɮօt ɨs օռʟɨռɛ🔥🔥</i></b>
<b><i>↼ Øwñêr ⇀</i></b> : 『 {Neiman_mention} 』
╭──────────────
┣─ <b>» Telethon:</b> <i>{Pyrogram_version}</i>
┣─ <b>» Hêllẞø†:</b> <i>{Neimanbot_version}</i>
┣─ <b>» Sudo:</b> <i>{is_sudo}</i>
┣─ <b>» Uptime:</b> <i>{uptime}</i>
┣─ <b>» Ping:</b> <i>{ping}</i>
╰──────────────
<b><i>»»» <a href='https://t.me/TeamNeiman'>[NeimanBot]</a> «««</i></b>
"""

msg = """{}\n
<b><i>🏅 𝙱𝚘𝚝 𝚂𝚝𝚊𝚝𝚞𝚜 🏅</b></i>
<b>pyrogram ≈</b>  <i>{}</i>
<b>NeimanBot ≈</b>  <i>{}</i>
<b>Uptime ≈</b>  <i>{}</i>
<b>Abuse ≈</b>  <i>{}</i>
<b>Sudo ≈</b>  <i>{}</i>
"""
# -------------------------------------------------------------------------------


@Neiman_cmd(pattern="alivetemp$")
async def set_alive_temp(event):
    Neiman = await eor(event, "`Fetching template ...`")
    reply = await event.get_reply_message()
    if not reply:
        alive_temp = gvarstat("ALIVE_TEMPLATE") or ALIVE_TEMP
        to_reply = await Neiman.edit("Below is your current alive template 👇")
        await event.client.send_message(event.chat_id, alive_temp, parse_mode=None, link_preview=False, reply_to=to_reply)
        return
    addgvar("ALIVE_TEMPLATE", reply.text)
    await hell.edit(f"`ALIVE_TEMPLATE` __changed to:__ \n\n`{reply.text}`")


@Neiman_cmd(pattern="alive$")
async def _(event):
    start = datetime.datetime.now()
    Neimanid, Neiman_user, Neiman_mention = await client_id(event, is_html=True)
    Neiman = await eor(event, "`Building Alive....`")
    reply = await event.get_reply_message()
    uptime = await get_time((time.time() - StartTime))
    name = gvarstat("ALIVE_NAME") or Neiman_user
    alive_temp = gvarstat("ALIVE_TEMPLATE") or ALIVE_TEMP
    a = gvarstat("ALIVE_PIC")
    pic_list = []
    if a:
        b = a.split(" ")
        if len(b) >= 1:
            for c in b:
                pic_list.append(c)
        PIC = random.choice(pic_list)
    else:
        PIC = "https://te.legra.ph/file/ea9e11f7c9db21c1b8d5e.mp4"
    end = datetime.datetime.now()
    ping = (end - start).microseconds / 1000
    alive = alive_temp.format(
        Neiman_mention=Neiman_mention,
        pyrogram_version=pyrogram_version,
        Neimanbot_version=Neimanbot_version,
        is_sudo=is_sudo,
        uptime=uptime,
        ping=ping,
    )
    await event.client.send_file(
        event.chat_id,
        file=PIC,
        caption=alive,
        reply_to=reply,
        parse_mode="HTML",
    )
    await Neiman.delete()


@Neiman_cmd(pattern="Neiman$")
async def hell_a(event):
    userid, _, _ = await client_id(event)
    uptime = await get_time((time.time() - StartTime))
    am = gvarstat("ALIVE_MSG") or "<b>»» NeimanBot ιѕ σиℓιиє ««</b>"
    try:
        Neiman = await event.client.inline_query(Config.BOT_USERNAME, "alive")
        await Neiman[0].click(event.chat_id)
        if event.sender_id == userid:
            await event.delete()
    except (noin, dedbot):
        await eor(
            event,
            msg.format(am, pyrogram_version, Neimanbot_version, uptime, abuse_m, is_sudo),
            parse_mode="HTML",
        )


CmdHelp("alive").add_command(
    "Neiman", None, "Shows the default Alive message."
).add_command(
    "Neiman", None, "Shows inline Alive message."
).add_warning(
    "✅ Harmless Module"
).add()
