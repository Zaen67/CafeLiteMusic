from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "4110592"))
API_HASH = getenv("API_HASH", "aa7c849566922168031b95212860ede0")
BOT_TOKEN = getenv("BOT_TOKEN", None)
BOT_NAME = getenv("BOT_NAME","CafeLiteMusic")
BOT_USERNAME = getenv("BOT_USERNAME", "CafeLiteMusicBot")
OWNER_USERNAME = getenv("OWNER_USERNAME", "Mafia_TobaTz")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "CafeLiteMusic")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))
START_IMG = getenv("START_IMG", "https://telegra.ph/file/5a1452003850ffbd1c125.jpg")
PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/5a1452003850ffbd1c125.jpg")
AUD_IMG = getenv("AUD_IMG", "https://telegra.ph/file/73e10ed6e2bd32b478de6.png")
QUE_IMG = getenv("QUE_IMG", "https://telegra.ph/file/b95c13eef1ebd14dbb458.png")
SESSION_NAME = getenv("SESSION_NAME", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "? ~ + • / ! ^ .").split())
PMPERMIT = getenv("PMPERMIT", "ENABLE")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "2010825200").split()))
