#(©)CodeXBotz
#Recoded By @Its_Tartaglia_Childe



import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7324516511:AAGgJW9ZPO1ZOvZEmAE-UMq6U2JAm0biPFo")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "23871733"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "afab08a473c8ae7312d91f97d1208b5c")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002420032418"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "7580618380"))

#Port
PORT = os.environ.get("PORT", "7000")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://botmaker9675208:botmaker9675208@cluster0.sc9mq8b.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DATABASE_NAME", "botmaker9675208")

#force sub channel id, if you want enable force sub
FORCESUB_CHANNEL = int(os.environ.get("FORCESUB_CHANNEL", "-1001497637176"))
FORCESUB_CHANNEL2 = int(os.environ.get("FORCESUB_CHANNEL2", "-1002330606324"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "3"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "<b> Kᴏɴɴɪᴄʜɪᴡᴀ {first} 👋 </b>\n\nI ᴀᴍ ᴀ ғɪʟᴇ sᴛᴏʀᴇ ʙᴏᴛ ᴍᴀᴅᴇ ʙʏ @AniXtream")
try:
    ADMINS=[]
    for x in (os.environ.get("7013604559,6149361523,7580618380").split(",")):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "〒Hi! \nPlease Join our channel First then Download by tapping on ʀᴇʟᴏᴀᴅ  \nThank You✦")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "​🚫Pʟᴇᴀꜱᴇ ᴅᴏɴ'ᴛ ᴍᴇꜱꜱᴀɢᴇ ᴍᴇ ᴅɪʀᴇᴄᴛʟʏ ɪ ᴏɴʟʏ ᴡᴏʀᴋ ꜰᴏʀ​ - @AniXtream"

ADMINS.append(OWNER_ID)
ADMINS.append(5090651635)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
