import re
from os import environ
from dotenv import load_dotenv
from Script import script 

load_dotenv("./dynamic.env", override=True, encoding="utf-8")

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

req1 = environ.get('REQ_CHANNEL1', '-1002149382278')
req2 = environ.get('REQ_CHANNEL2', '-1002204112835')

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ.get('API_ID', '26305156'))
API_HASH = environ.get('API_HASH', '9937930c368c669ca905e9a95aa712f0')
BOT_TOKEN = environ.get('BOT_TOKEN', '7228747455:AAEyS9RwFbMA2cFc69KtjJk2Fe3FUXtv7MU')

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', False))
PICS = (environ.get('PICS', 'https://telegra.ph/file/5de2a87af196bcd866b7f.jpg')).split()
NOR_IMG = environ.get("NOR_IMG", "https://telegra.ph/file/5de2a87af196bcd866b7f.jpg")

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '7040444713').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1002157654949').split()]
FORCE_SUB_CHANNEL = environ.get("FORCE_SUB_CHANNEL", "-1002166880535"),
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_grp = environ.get('AUTH_GROUP')
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None

REQ_CHANNEL1 = int(req1) if req1 and id_pattern.search(req1) else None
REQ_CHANNEL2 = int(req2) if req2 and id_pattern.search(req2) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None

# MongoDB information
DATABASE_NAME = environ.get('DATABASE_NAME', "kalki")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://bro:bro@kalki.mklkd.mongodb.net/?retryWrites=true&w=majority&appName=kalki")
DATABASE_URI2 = environ.get('DATABASE_URI2', "mongodb+srv://me:me@kalki2.iabio.mongodb.net/?retryWrites=true&w=majority&appName=kalki2")
DATABASE_URI3 = environ.get('DATABASE_URI3', "mongodb+srv://you:you@kalki3.l4cas.mongodb.net/?retryWrites=true&w=majority&appName=kalki3")
DATABASE_URI4 = environ.get('DATABASE_URI4', "mongodb+srv://pro:prokalki4.rhmc9.mongodb.net/?retryWrites=true&w=majority&appName=kalki4")
DATABASE_URI5 = environ.get('DATABASE_URI5', "mongodb+srv://pls:pls@kalki5.vneogwq.mongodb.net/?retryWrites=true&w=majority&appName=kalki5")
                            
# FSUB
auth_channel = environ.get('-1002170119688')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
# Set to False inside the bracket if you don't want to use Request Channel else set it to Channel ID

REQ_CHANNEL=environ.get("REQ_CHANNEL", "-1002149382278")
REQ_CHANNEL = (int(REQ_CHANNEL) if REQ_CHANNEL and id_pattern.search(REQ_CHANNEL) else False) if REQ_CHANNEL is not None else None
REQ_CHANNEL2=environ.get("REQ_CHANNEL2", "-1002204112835")
REQ_CHANNEL2 = (int(REQ_CHANNEL2) if REQ_CHANNEL2 and id_pattern.search(REQ_CHANNEL2) else False) if REQ_CHANNEL2 is not None else None
JOIN_REQS_DB = environ.get("JOIN_REQS_DB", DATABASE_URI)

# Others
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002208570147'))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'MOVIES_ZILAA')
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', 'False')), False)
IMDB = is_enabled((environ.get('IMDB', 'False')), False)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', 'True')), True)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", f"{script.CUSTOM_FILE_CAPTION}")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", "🏷 𝖳𝗂𝗍𝗅𝖾: <a href={url}>{title}</a> \n🔮 𝖸𝖾𝖺𝗋: {year} \n⭐️ 𝖱𝖺𝗍𝗂𝗇𝗀𝗌: {rating}/ 10 \n🎭 𝖦𝖾𝗇𝖾𝗋𝗌: {genres} \n\n🎊")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "False")), False)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "False")), False)

LOG_STR = "Current Customized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"
