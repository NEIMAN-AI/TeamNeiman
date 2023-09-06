import sys

from pyrogram import TelegramClient
from pyrogram.network.connection.tcpabridged import ConnectionTcpAbridged
from pyrogram.sessions import StringSession

from NeimanConfig import Config


def validate_session(session):
    if "==Neiman" and "bot==" in session.lower():
        new_session = session[6:-5]
        return str(new_session)
    else:
        print(f"SESSION - Wrong session string!")
        sys.exit()


if Config.SESSION:
    session = StringSession(validate_session(Config.SESSION))
else:
    session = "Neimanbot"

try:
    Neiman = TelegramClient(
        session=session,
        api_id=Config.APP_ID,
        api_hash=Config.API_HASH,
        connection=ConnectionTcpAbridged,
        auto_reconnect=True,
        connection_retries=None,
    )
except Exception as e:
    print(f"SESSION - {e}")
    sys.exit()


if Config.SESSION_2:
    session2 = StringSession(validate_session(Config.SESSION_2))
    H2 = TelegramClient(
        session=session2,
        api_id=Config.APP_ID,
        api_hash=Config.API_HASH,
        connection=ConnectionTcpAbridged,
        auto_reconnect=True,
        connection_retries=None,
    )
else:
    H2 = None


if Config.SESSION_3:
    session3 = StringSession(validate_session(Config.SESSION_3))
    H3 = TelegramClient(
        session=session3,
        api_id=Config.APP_ID,
        api_hash=Config.API_HASH,
        connection=ConnectionTcpAbridged,
        auto_reconnect=True,
        connection_retries=None,
    )
else:
    H3 = None


if Config.SESSION_4:
    session4 = StringSession(validate_session(Config.SESSION_4))
    H4 = TelegramClient(
        session=session4,
        api_id=Config.APP_ID,
        api_hash=Config.API_HASH,
        connection=ConnectionTcpAbridged,
        auto_reconnect=True,
        connection_retries=None,
    )
else:
    H4 = None


if Config.SESSION_5:
    session5 = StringSession(validate_session(Config.SESSION_5))
    H5 = TelegramClient(
        session=session5,
        api_id=Config.APP_ID,
        api_hash=Config.API_HASH,
        connection=ConnectionTcpAbridged,
        auto_reconnect=True,
        connection_retries=None,
    )
else:
    H5 = None


NeimanBot = TelegramClient(
    session="Neiman-TBot",
    api_id=Config.APP_ID,
    api_hash=Config.API_HASH,
    connection=ConnectionTcpAbridged,
    auto_reconnect=True,
    connection_retries=None,
).start(bot_token=Config.BOT_TOKEN)
