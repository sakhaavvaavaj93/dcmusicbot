from dotenv import load_dotenv
from os import path, getenv


if path.exists("local.env"):
    load_dotenv("local.env")
else:
    load_dotenv()


class Config:
    API_ID = int(getenv("API_ID", "0"))
    API_HASH = getenv("API_HASH", "abc123")
    BOT_TOKEN = getenv("BOT_TOKEN", "1234:abcd")
    SESSION = getenv("SESSION", "session")
    OWNER_ID = int(getenv("OWNER_ID", "5683104617"))
    SUPPORT = getenv("SUPPORT", "https://t.me/DC_Kurukshethra")
    CHANNEL = getenv("CHANNEL", "https://t.me/DC_LOGS")
    UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/sakhaavvaavaj93/dcmusicbot")


config = Config()
