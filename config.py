# (c) ՏIᒪᗴᑎT ᘜᕼOՏT ⚡️ # Dont Remove Credit

import re
from os import environ

id_pattern = re.compile(r'^.\d+$')

DS_API_ID = int(environ.get("DS_API_ID", ""))
DS_API_HASH = environ.get("DS_API_HASH", "")
DS_BOT_TOKEN = environ.get("DS_BOT_TOKEN", "")
DS_BOT_USERNAME = environ.get("DS_BOT_USERNAME", "") # bot username without @
DS_LOG_CHANNEL = int(environ.get("DS_LOG_CHANNEL", ""))
DS_STICKER = environ.get("DS_STICKER", "")
DS_PIC = environ.get('DS_PIC', 'https://envs.sh/k-.jpg/HGBOTZ.jpg')

# Database Channel For Text Or Caption Store 
DS_DESI_FILE_CHANNEL = int(environ.get("DS_DESI_FILE_CHANNEL", ""))
DS_VIDESI_FILE_CHANNEL = int(environ.get("DS_VIDESI_FILE_CHANNEL", ""))
FREE_LIMIT_DESI = 10
FREE_LIMIT_VIDESI = 3
PREMIUM_LIMIT_DESI = 40
PREMIUM_LIMIT_VIDESI = 15

# Bot Admins
try:
    DS_ADMINS=[]
    for x in (environ.get("DS_ADMINS", "1562935405").split()):
        DS_ADMINS.append(int(x))
except ValueError:
      raise Exception("Your Admins list does not contain valid integers.")
    
# Mongodb Database 
DS_DB_URI = environ.get("DS_DB_URI", "")
DS_DB_NAME = environ.get("DS_DB_NAME", "")

# Force subscribe channel 
DS_AUTH_CHANNEL = int(environ.get('DS_AUTH_CHANNEL', '')) # give your force subscribe channel id here else leave it blank

# Verification Variables
DS_API = environ.get("DS_API", "") # shortlink api
DS_URL = environ.get("DS_URL", "") # shortlink domain without https://
DS_VERIFY_TUTORIAL = environ.get("DS_VERIFY_TUTORIAL", "") # how to open link 
DS_VERIFICATION = bool(environ.get("DS_VERIFICATION", True)) # set True Or False and make sure spelling is correct and first letter capital.

# (c) ՏIᒪᗴᑎT ᘜᕼOՏT ⚡️ # Dont Remove Credit
