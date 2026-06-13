

from os import environ

API_ID = int(environ.get("API_ID", "32056256"))
API_HASH = environ.get("15f09e0725bd0eb718ca22bce581cb38", "")
BOT_TOKEN = environ.get("BOT_TOKEN", "8556613615:AAHUeVQctgm3ROT63mDxzwSTXEwXwBTUEZA")

# Force Subscribe Configuration
FORCE_SUB_CHANNEL = environ.get("FORCE_SUB_CHANNEL", "bhaveshbhai_bot1")  # Channel username without @, 
FORCE_SUB_CHANNEL_LINK = environ.get("FORCE_SUB_CHANNEL_LINK", "https://t.me/+gEDFgi0ENI1hOGM1")  # Channel link

# Admin Configuration
ADMINS = list(map(int, environ.get("ADMINS", "8902900224").split()))

# Optional: Bot Owner ID
OWNER_ID = int(environ.get("OWNER_ID", "8902900224"))

# Database URL (if you want to add database support later)
DATABASE_URL = environ.get("DATABASE_URL", "")




