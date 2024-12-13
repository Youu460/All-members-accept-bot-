from os import environ

API_ID = int(environ.get("API_ID", "11824466"))
API_HASH = environ.get("API_HASH", "5afd3ea9d0018ed654ae39a87aee62c7")
BOT_TOKEN = environ.get("BOT_TOKEN", "7996187231:AAEHIG9wrKslRHibf26_ptU-NZw9yEO7UTA")
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1002499036398"))
ADMINS = int(environ.get("ADMINS", "5130458445"))
DB_URI = environ.get("DB_URI", "mongodb+srv://autofilterbotm123:autofilterbotm123@cluster0.nkukt.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = environ.get("DB_NAME", "Cluster0")
