import string

from telethon.tl.types import Channel, MessageMediaWebPage

from userbot import savior
from userbot.funcs.logger import logging

from ..Config import Config
from ..funcs.managers import eor

menu_category = "extra"

LOGS = logging.getLogger(__name__)


class FPOST:
    def __init__(self) -> None:
        self.GROUPSID = []
        self.MSG_CACHE = {}


FPOST_ = FPOST()


async def all_groups_id(savior):
    saviorgroups = []
    async for dialog in savior.client.iter_dialogs():
        entity = dialog.entity
        if isinstance(entity, Channel) and entity.megagroup:
            saviorgroups.append(entity.id)
    return saviorgroups


@savior.savior_cmd(
    pattern="frwd$",
    command=("frwd", menu_category),
    info={
        "header": "To get view counter for the message. that is will delete old message and send new message where you can see how any people saw your message",
        "usage": "{tr}frwd",
    },
)
async def _(event):
    "To get view counter for the message"
    if Config.PRIVATE_CHANNEL_BOT_API_ID == 0:
        return await eor(
            event,
            "Please set the required environment variable `PRIVATE_CHANNEL_BOT_API_ID` for this plugin to work",
        )
    try:
        e = await event.client.get_entity(Config.PRIVATE_CHANNEL_BOT_API_ID)
    except Exception as e:
        await eor(event, str(e))
    else:
        re_message = await event.get_reply_message()
        # https://t.me/telethonofftopic/78166
        fwd_message = await event.client.forward_messages(e, re_message, silent=True)
        await event.client.forward_messages(event.chat_id, fwd_message)
        try:
            await event.delete()
        except Exception as e:
            LOGS.info(str(e))


@savior.savior_cmd(
    pattern="resend$",
    command=("resend", menu_category),
    info={
        "header": "To resend the message again. Useful to remove forword tag",
        "usage": "{tr}resend",
    },
)
async def _(event):
    "To resend the message again"
    try:
        await event.delete()
    except Exception as e:
        LOGS.info(str(e))
    m = await event.get_reply_message()
    if not m:
        return
    if m.media and not isinstance(m.media, MessageMediaWebPage):
        return await event.client.send_file(event.chat_id, m.media, caption=m.text)
    await event.client.send_message(event.chat_id, m.text)


@savior.savior_cmd(
    pattern="fpost ([\s\S]*)",
    command=("fpost", menu_category),
    info={
        "header": "Split the word and forwards each letter from previous messages in that group",
        "usage": "{tr}fpost <text>",
        "examples": "{tr}fpost SaViorX",
    },
)
async def _(event):
    "Split the word and forwards each letter from previous messages in that group"
    await event.delete()
    text = event.pattern_match.group(1)
    destination = await event.get_input_chat()
    if len(FPOST_.GROUPSID) == 0:
        FPOST_.GROUPSID = await all_groups_id(event)
    for c in text.lower():
        if c not in string.ascii_lowercase:
            continue
        if c not in FPOST_.MSG_CACHE:
            async for msg in event.client.iter_messages(event.chat_id, search=c):
                if msg.raw_text.lower() == c and msg.media is None:
                    FPOST_.MSG_CACHE[c] = msg
                    break
        if c not in FPOST_.MSG_CACHE:
            for i in FPOST_.GROUPSID:
                async for msg in event.client.iter_messages(event.chat_id, search=c):
                    if msg.raw_text.lower() == c and msg.media is None:
                        MSG_CACHE[c] = msg
                        break
        await event.client.forward_messages(destination, FPOST_.MSG_CACHE[c])
