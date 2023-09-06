from NeimanConfig.config import Config


class Development(Config):
    
    APP_ID = 666666  # 666666 is a placeholder. Fill your 6 digit api id
    API_HASH = "eb06d4abfb49dc3eeb1aeb98ae0f581e"  # replace this with your api hash
    BOT_TOKEN = "Your value"  # Create a bot from @BotFather and paste the token here
    BOT_LIBRARY = "pyrogram"  # fill 'pyrogram' if you want pyrogram version of bot else leave it as it is.
    DATABASE_URL = "Your value"  # A postgresql database url from elephantsql
    SESSION = "Your value"  # telethon or pyrogram string according to BOT_LIBRARY
    HANDLER = "."  # Custom Command Handler
    SUDO_HANDLER = "!"  # Custom Command Handler for sudo users.


