# This file is a part of TG-FileStreamBot
# Coding : Jyothis Jayanth [@EverythingSuckz]

from os import environ
from dotenv import load_dotenv

load_dotenv()


class Var(object):
    MULTI_CLIENT = False
    API_ID = int(environ.get("API_ID"))
    API_HASH = str(environ.get("API_HASH"))
    BOT_TOKEN = str(environ.get("BOT_TOKEN"))
    SLEEP_THRESHOLD = int(environ.get("SLEEP_THRESHOLD", "60"))  # 1 minte
    WORKERS = int(environ.get("WORKERS", "6"))  # 6 workers = 6 commands at once
    BIN_CHANNEL = int(
        environ.get("BIN_CHANNEL", None)
    )  # you NEED to use a CHANNEL when you're using MULTI_CLIENT
    BIN_CHANNEL_WITHOUT_MINUS = int(
        environ.get("BIN_CHANNEL_WITHOUT_MINUS", None)
    )  # you NEED to use a CHANNEL when you're using MULTI_CLIENT
    PORT = int(environ.get("PORT", 8080))
    BIND_ADDRESS = str(environ.get("WEB_SERVER_BIND_ADDRESS", "0.0.0.0"))
    PING_INTERVAL = int(environ.get("PING_INTERVAL", "120"))  # 2 minutes
    #HAS_SSL = environ.get("HAS_SSL", False)
    HAS_SSL = True #if str(HAS_SSL).lower() == "true" else False
    #NO_PORT = environ.get("NO_PORT", False)
    NO_PORT = True #if str(NO_PORT).lower() == "true" else False
    DOMAIN = str(environ.get("PROJECT_DOMAIN"))
    FQDN = (
        str(environ.get("FQDN", BIND_ADDRESS))
        if not True or environ.get("FQDN")
        else DOMAIN + ".glitch.me"
    )
    URL = f"https://{FQDN}/"
