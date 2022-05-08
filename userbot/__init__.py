import signal
import time

import heroku3

from .Config import Config
from .funcs.logger import logging
from .funcs.session import savior
from .helpers.utils.utils import runasync
from .sql_helper.globals import addgvar, delgvar, gvarstatus

__version__ = "S • 0.1"
__license__ = "GNU Affero General Public License v3.0"
__author__ = "SaVior <https://github.com/TheSaVior/SAVIOR>"
__copyright__ = f"SaVior Copyright (C) 2022 - 2023  { __author__}"

savior.version = __version__
savior.tgbot.version = __version__
LOGS = logging.getLogger("SaViorX")
bot = savior


StartTime = time.time()
saviorversion = "S • 0.1"


def close_connection(*_):
    print("Closing Userbot connection.")
    runasync(savior.disconnect())
    sys.exit(143)


signal.signal(signal.SIGTERM, close_connection)


if Config.UPSTREAM_REPO == "pro":
    UPSTREAM_REPO_URL = "https://github.com/TheSaVior/SAVIOR"
elif Config.UPSTREAM_REPO == "multi":
    UPSTREAM_REPO_URL = "https://github.com/TheSaVior/SaViorX"
else:
    UPSTREAM_REPO_URL = Config.UPSTREAM_REPO

if Config.PRIVATE_GROUP_BOT_API_ID == 0:
    if gvarstatus("PRIVATE_GROUP_BOT_API_ID") is None:
        Config.BOTLOG = False
        Config.BOTLOG_CHATID = "me"
    else:
        Config.BOTLOG_CHATID = int(gvarstatus("PRIVATE_GROUP_BOT_API_ID"))
        Config.PRIVATE_GROUP_BOT_API_ID = int(gvarstatus("PRIVATE_GROUP_BOT_API_ID"))
        Config.BOTLOG = True
else:
    if str(Config.PRIVATE_GROUP_BOT_API_ID)[0] != "-":
        Config.BOTLOG_CHATID = int("-" + str(Config.PRIVATE_GROUP_BOT_API_ID))
    else:
        Config.BOTLOG_CHATID = Config.PRIVATE_GROUP_BOT_API_ID
    Config.BOTLOG = True

if Config.PM_LOGGER_GROUP_ID == 0:
    if gvarstatus("PM_LOGGER_GROUP_ID") is None:
        Config.PM_LOGGER_GROUP_ID = -100
    else:
        Config.PM_LOGGER_GROUP_ID = int(gvarstatus("PM_LOGGER_GROUP_ID"))
elif str(Config.PM_LOGGER_GROUP_ID)[0] != "-":
    Config.PM_LOGGER_GROUP_ID = int(f"-{str(Config.PM_LOGGER_GROUP_ID)}")

try:
    if Config.API_KEY is not None or Config.APP_NAME is not None:
        HEROKU_APP = heroku3.from_key(Config.API_KEY).apps()[Config.APP_NAME]
    else:
        HEROKU_APP = None
except Exception:
    HEROKU_APP = None


# Global Configiables
COUNT_MSG = 0
USERS = {}
COUNT_PM = {}
LASTMSG = {}
CMD_HELP = {}
ISAFK = False
AFKREASON = None
CMD_LIST = {}
SUDO_LIST = {}
# for later purposes
INT_PLUG = ""
LOAD_PLUG = {}

# Variables
BOTLOG = Config.BOTLOG
BOTLOG_CHATID = Config.BOTLOG_CHATID
PM_LOGGER_GROUP_ID = Config.PM_LOGGER_GROUP_ID
