import logging
from logging.handlers import RotatingFileHandler

# Bot Configuration
LOG_FILE_NAME = "bot.log"
PORT = '5010'
OWNER_ID = 1718481517

MSG_EFFECT = 5046509860389126442

SHORT_URL = "gplinks.com" # shortner url 
SHORT_API = "fe8aa2557a758e856f79187ee1994a88da5dbd43" 
SHORT_TUT = "https://t.me/How_to_Download_7x/26"

# Bot Configuration
SESSION = "yato"
TOKEN = "7622241172:AAHjInldlbjFXAADnL6FS97NV4_IuGzF-kM"
API_ID = "27693340"
API_HASH = "1056193e68c138ee16edc02578c559e1"
WORKERS = 5

DB_URI = "svrznzr.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
DB_NAME = "Cluster0"

FSUBS = [[-1003016571084, True, 10]] # Force Subscription Channels [channel_id, request_enabled, timer_in_minutes]
# Database Channel (Primary)
DB_CHANNEL = "-1002413997036"
# Multiple Database Channels (can be set via bot settings)
# DB_CHANNELS = {
#     "-1003162938547": {"name": "Primary DB", "is_primary": True, "is_active": True},
#     "-1002849677750": {"name": "Secondary DB", "is_primary": False, "is_active": True}
# }
# Auto Delete Timer (seconds)
AUTO_DEL = 300
# Admin IDs
ADMINS = []
# Bot Settings
DISABLE_BTN = True
PROTECT = True

# Messages Configuration
MESSAGES = {
    "START": """<b>⚡ Hᴇʏ, {mention} ~

<blockquote expandable>I ᴀᴍ ᴀɴ ᴀᴅᴠᴀɴᴄᴇ ғɪʟᴇ sʜᴀʀᴇ ʙᴏᴛ V3!\nTʜᴇ ʙᴇsᴛ ᴘᴀʀᴛ ɪs ɪ ᴀᴍ ᴀʟsᴏ sᴜᴘᴘᴏʀᴛ ʀᴇǫᴜᴇsᴛ ғᴏʀᴄᴇsᴜʙ ғᴇᴀᴛᴜʀᴇ, Tᴏ ᴋɴᴏᴡ ᴅᴇᴛᴀɪʟᴇᴅ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴄʟɪᴄᴋ ᴀʙᴏᴜᴛ ᴍᴇ ʙᴜᴛᴛᴏɴ ᴛᴏ ᴋɴᴏᴡ ᴍʏ ᴀʟʟ ᴀᴅᴠᴀɴᴄᴇ ғᴇᴀᴛᴜʀᴇs!.</blockquote></b>"""
    
    "FSUB": "<b><blockquote>›› ʜᴇʏ ×</blockquote>\n  ʏᴏᴜʀ ғɪʟᴇ ɪs ʀᴇᴀᴅʏ ‼️ ʟᴏᴏᴋs ʟɪᴋᴇ ʏᴏᴜ ʜᴀᴠᴇɴ'ᴛ sᴜʙsᴄʀɪʙᴇᴅ ᴛᴏ ᴏᴜʀ ᴄʜᴀɴɴᴇʟs ʏᴇᴛ, sᴜʙsᴄʀɪʙᴇ ɴᴏᴡ ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ғɪʟᴇs</b>",
    "ABOUT": "<b>››🤖 ᴍʏ ɴᴀᴍᴇ: {MILKY BOT}
    \n <blockquote expandable>›› ᴄʀᴇᴀᴛᴏʀ: <a href=https://t.me/Black_walker_id>Bʟᴀᴄᴋ Wᴀʟᴋᴇʀ 🜲</a>\n» ᴏᴜʀ ᴄᴏᴍᴍᴜɴɪᴛʏ : <a href=https://t.me/play_tamil_dubbed_series>ᴘʟᴀʏ ᴄᴏᴍᴍᴜɴɪᴛʏ</a>\n» ᴀᴅᴠᴀɴᴄᴇ ғᴇᴀᴛᴜʀᴇs : <a href=https://telegra.ph/BOT-FEATURES-11-09-28>Cʟɪᴄᴋ ʜᴇʀᴇ </a>\n» ʟᴀɴɢᴜᴀɢᴇ : <a href=https://docs.python.org/3/>Pʏᴛʜᴏɴ 3</a>\n» ʟɪʙʀᴀʀʏ : <a href=https://docs.pyrogram.org/>Pʏʀᴏɢʀᴀᴍ ᴠ2</a>\n» ᴅᴇᴠᴇʟᴏᴘᴇʀ : <a href=https://t.me/searchingshiv>ᴜɴᴋɴᴏᴡɴ</a></b></blockquote>"""
    "SHORT_MSG": "<b>📊 ʜᴇʏ {first}, \n\n‼️ ɢᴇᴛ ᴀʟʟ ꜰɪʟᴇꜱ ɪɴ ᴀ ꜱɪɴɢʟᴇ ʟɪɴᴋ ‼️\n\n ⌯ ʏᴏᴜʀ ʟɪɴᴋ ɪꜱ ʀᴇᴀᴅʏ, ᴋɪɴᴅʟʏ ᴄʟɪᴄᴋ ᴏɴ ᴏᴘᴇɴ ʟɪɴᴋ ʙᴜᴛᴛᴏɴ..</b>",
    "START_PHOTO": "https://graph.org/file/510affa3d4b6c911c12e3.jpg",
    "FSUB_PHOTO": "https://telegra.ph/file/7a16ef7abae23bd238c82-b8fbdcb05422d71974.jpg",
    "SHORT_PIC": "https://telegra.ph/file/7a16ef7abae23bd238c82-b8fbdcb05422d71974.jpg",
    "SHORT": "https://telegra.ph/file/8aaf4df8c138c6685dcee-05d3b183d4978ec347.jpg"
}

def LOGGER(name: str, client_name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    formatter = logging.Formatter(
        f"[%(asctime)s - %(levelname)s] - {client_name} - %(name)s - %(message)s",
        datefmt='%d-%b-%y %H:%M:%S'
    )
    file_handler = RotatingFileHandler(LOG_FILE_NAME, maxBytes=50_000_000, backupCount=10)
    file_handler.setFormatter(formatter)
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.setLevel(logging.INFO)
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    return logger
