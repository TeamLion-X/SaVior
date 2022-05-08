import asyncio
import random
import re
import time
from datetime import datetime
from platform import python_version

from telethon import version
from telethon.errors.rpcerrorlist import (
    MediaEmptyError,
    WebpageCurlFailedError,
    WebpageMediaEmptyError,
)
from telethon.events import CallbackQuery

from userbot import StartTime, savior, saviorversion

from ..Config import Config
from ..funcs.managers import eor
from ..helpers.functions import check_data_base_heal_th, get_readable_time, savioralive
from ..helpers.utils import reply_id
from ..sql_helper.globals import gvarstatus
from . import mention

menu_category = "utils"


@savior.savior_cmd(
    pattern="alive$",
    command=("alive", menu_category),
    info={
        "header": "To check bot's alive status",
        "options": "To show media in this cmd you need to set ALIVE_PIC with media link, get this by replying the media by .tgm",
        "usage": [
            "{tr}alive",
        ],
    },
)
async def amireallyalive(event):
    "A kind of showing bot details"
    reply_to_id = await reply_id(event)
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    saviorevent = await eor(event, "`Checking...`")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    _, check_sgnirts = check_data_base_heal_th()
    ALIVE_TEXT = gvarstatus("ALIVE_TEXT")
    EMOJI = gvarstatus("ALIVE_EMOJI") or "✥"
    lal = list(EMOJI.split())
    EMOTES = random.choice(lal)
    redeye_caption = (
        "**⚜ SaVior Is Online ⚜**\n\n" + f"{gvarstatus('ALIVE_TEMPLATE')}"
    )
    caption = redeye_caption.format(
        ALIVE_TEXT=ALIVE_TEXT,
        EMOTES=EMOTES,
        mention=mention,
        uptime=uptime,
        telever=version.__version__,
        saviorver=saviorversion,
        pyver=python_version(),
        dbhealth=check_sgnirts,
        ping=ms,
    )
    try:
        results = await event.client.inline_query(Config.BOT_USERNAME, caption)
        await results[0].click(event.chat_id, reply_to=reply_to_id, hide_via=True)
        await event.delete()
    except (WebpageMediaEmptyError, MediaEmptyError, WebpageCurlFailedError):
        return await eor(
            saviorevent,
            f"**Media Value Error!!**\n__Change the link by __`.setdv`\n\n**__Can't get media from this link :-**__ `{SAVIOR_IMG}`",
        )


"""
temp = {ALIVE_TEXT}
**{EMOTES} Master:** {mention}
**{EMOTES} Uptime :** `{uptime}`
**{EMOTES} Telethon Version :** `{telever}`
**{EMOTES} SaViorX Version :** `{saviorver}`
**{EMOTES} Python Version :** `{pyver}`
**{EMOTES} Database :** `{dbhealth}`
"""


@savior.savior_cmd(
    pattern="savior$",
    command=("savior", menu_category),
    info={
        "header": "To check bot's alive status via inline mode",
        "options": "To show media in this cmd you need to set ALIVE_PIC with media link, get this by replying the media by .tgm",
        "usage": [
            "{tr}savior",
        ],
    },
)
async def amireallyalive(event):
    "A kind of showing bot details by your inline bot"
    reply_to_id = await reply_id(event)
    uptime = await get_readable_time((time.time() - StartTime))
    a = gvarstatus("ALIVE_EMOJI") or "🔹"
    kiss = list(a.split())
    EMOJI = random.choice(kiss)
    savior_caption = "**SaVior Is Online**\n\n"
    savior_caption += f"**{EMOJI} Telethon version :** `{version.__version__}\n`"
    savior_caption += f"**{EMOJI} SaViorX Version :** `{saviorversion}`\n"
    savior_caption += f"**{EMOJI} Python Version :** `{python_version()}\n`"
    savior_caption += f"**{EMOJI} Uptime :** {uptime}\n"
    savior_caption += f"**{EMOJI} Master:** {mention}\n"
    results = await event.client.inline_query(Config.BOT_USERNAME, savior_caption)
    await results[0].click(event.chat_id, reply_to=reply_to_id, hide_via=True)
    await event.delete()

@savior.tgbot.on(CallbackQuery(data=re.compile(b"stats")))
async def on_plug_in_callback_query_handler(event):
    statstext = await savioralive(StartTime)
    await event.answer(statstext, cache_time=0, alert=True)
