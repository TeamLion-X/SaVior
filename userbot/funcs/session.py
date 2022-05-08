import sys

from telethon.network.connection.tcpabridged import ConnectionTcpAbridged
from telethon.sessions import StringSession

from ..Config import Config
from .client import SaViorClient

__version__ = "1.10.6"

loop = None

if Config.SAVIOR_STRING:
    session = StringSession(str(Config.SAVIOR_STRING))
else:
    session = "SaViorX"

try:
    savior = SaViorClient(
        session=session,
        api_id=Config.APP_ID,
        api_hash=Config.API_HASH,
        loop=loop,
        app_version=__version__,
        connection=ConnectionTcpAbridged,
        auto_reconnect=True,
        connection_retries=None,
    )
except Exception as e:
    print(f"SAVIOR_STRING - {e}")
    sys.exit()

savior.tgbot = tgbot = SaViorClient(
    session="SaViorTgbot",
    api_id=Config.APP_ID,
    api_hash=Config.API_HASH,
    loop=loop,
    app_version=__version__,
    connection=ConnectionTcpAbridged,
    auto_reconnect=True,
    connection_retries=None,
).start(bot_token=Config.BOT_TOKEN)
