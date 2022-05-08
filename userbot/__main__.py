import sys

import userbot
from userbot import BOTLOG_CHATID, PM_LOGGER_GROUP_ID

from .Config import Config
from .funcs.logger import logging
from .funcs.session import savior
from .start import killer, saviors
from .utils import (
    add_bot_to_logger_group,
    hekp,
    load_plugins,
    setup_bot,
    spams,
    startupmessage,
    verifyLoggerGroup,
)

LOGS = logging.getLogger("SaViorX")

print(userbot.__copyright__)
print("Licensed under the terms of the " + userbot.__license__)

cmdhr = Config.HANDLER


try:
    LOGS.info("Starting Userbot")
    savior.loop.run_until_complete(setup_bot())
    LOGS.info("TG Bot Startup Completed")
except Exception as e:
    LOGS.error(f"{e}")
    sys.exit()


async def startup_process():
    await verifyLoggerGroup()
    await load_plugins("plugins")
    await load_plugins("assistant")
    await killer()
    # await scammer("Godmrunal")
    await spams()
    print("----------------")
    print("Starting Bot Mode!")
    print("⚜ SaVior Has Been Deployed Successfully ⚜")
    print("OWNER - @SaViorXBoy")
    print("Group - @TheSaVior")
    print("----------------")
    await verifyLoggerGroup()
    await add_bot_to_logger_group(BOTLOG_CHATID)
    if PM_LOGGER_GROUP_ID != -100:
        await add_bot_to_logger_group(PM_LOGGER_GROUP_ID)
    await startupmessage()
    await saviors()
    return


savior.loop.run_until_complete(startup_process())
savior.loop.create_task(hekp())

if len(sys.argv) in (1, 3, 4):
    try:
        savior.run_until_disconnected()
    except ConnectionError:
        pass
else:
    savior.disconnect()
