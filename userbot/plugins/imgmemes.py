#  Copyright (C) 2020  SaViorXBoy
# credits to @SaViorXBoy (@SaViorXBoy)
import asyncio
import os
import re

from userbot import savior

from ..funcs.managers import eod, eor
from ..helpers.utils import reply_id
from . import (
    changemymind,
    deEmojify,
    fakegs,
    kannagen,
    moditweet,
    reply_id,
    trumptweet,
    tweets,
)

menu_category = "fun"


@savior.savior_cmd(
    pattern="fakegs(?:\s|$)([\s\S]*)",
    command=("fakegs", menu_category),
    info={
        "header": "Fake google search meme",
        "usage": "{tr}fakegs search query ; what you mean text",
        "examples": "{tr}fakegs SaViorX ; One of the Popular userbot",
    },
)
async def nekobot(lol):
    "Fake google search meme"
    text = lol.pattern_match.group(1)
    reply_to_id = await reply_id(lol)
    if not text:
        if lol.is_reply and not reply_to_id.media:
            text = reply_to_id.message
        else:
            return await eod(lol, "`What should i search in google.`", 5)
    saviore = await eor(lol, "`Connecting to https://www.google.com/ ...`")
    text = deEmojify(text)
    if ";" in text:
        search, result = text.split(";")
    else:
        await eod(
            lol,
            "__How should i create meme follow the syntax as show__ `.fakegs top text ; bottom text`",
            5,
        )
        return
    saviorfile = await fakegs(search, result)
    await asyncio.sleep(2)
    await lol.client.send_file(lol.chat_id, saviorfile, reply_to=reply_to_id)
    await saviore.delete()
    if os.path.exists(saviorfile):
        os.remove(saviorfile)


@savior.savior_cmd(
    pattern="trump(?:\s|$)([\s\S]*)",
    command=("trump", menu_category),
    info={
        "header": "trump tweet sticker with given custom text",
        "usage": "{tr}trump <text>",
        "examples": "{tr}trump SaViorX is One of the Popular userbot",
    },
)
async def nekobot(lol):
    "trump tweet sticker with given custom text_"
    text = lol.pattern_match.group(1)
    text = re.sub("&", "", text)
    reply_to_id = await reply_id(lol)

    reply = await lol.get_reply_message()
    if not text:
        if lol.is_reply and not reply.media:
            text = reply.message
        else:
            return await eod(lol, "**Trump : **`What should I tweet`", 5)
    saviore = await eor(lol, "`Requesting trump to tweet...`")
    text = deEmojify(text)
    await asyncio.sleep(2)
    saviorfile = await trumptweet(text)
    await lol.client.send_file(lol.chat_id, saviorfile, reply_to=reply_to_id)
    await saviore.delete()
    if os.path.exists(saviorfile):
        os.remove(saviorfile)


@savior.savior_cmd(
    pattern="modi(?:\s|$)([\s\S]*)",
    command=("modi", menu_category),
    info={
        "header": "modi tweet sticker with given custom text",
        "usage": "{tr}modi <text>",
        "examples": "{tr}modi SaViorX is One of the Popular userbot",
    },
)
async def nekobot(lol):
    "modi tweet sticker with given custom text"
    text = lol.pattern_match.group(1)
    text = re.sub("&", "", text)
    reply_to_id = await reply_id(lol)

    reply = await lol.get_reply_message()
    if not text:
        if lol.is_reply and not reply.media:
            text = reply.message
        else:
            return await eod(lol, "**Modi : **`What should I tweet`", 5)
    saviore = await eor(lol, "Requesting modi to tweet...")
    text = deEmojify(text)
    await asyncio.sleep(2)
    saviorfile = await moditweet(text)
    await lol.client.send_file(lol.chat_id, saviorfile, reply_to=reply_to_id)
    await saviore.delete()
    if os.path.exists(saviorfile):
        os.remove(saviorfile)


@savior.savior_cmd(
    pattern="cmm(?:\s|$)([\s\S]*)",
    command=("cmm", menu_category),
    info={
        "header": "Change my mind banner with given custom text",
        "usage": "{tr}cmm <text>",
        "examples": "{tr}cmm SaViorX is One of the Popular userbot",
    },
)
async def nekobot(lol):
    text = lol.pattern_match.group(1)
    text = re.sub("&", "", text)
    reply_to_id = await reply_id(lol)

    reply = await lol.get_reply_message()
    if not text:
        if lol.is_reply and not reply.media:
            text = reply.message
        else:
            return await eod(lol, "`Give text to write on banner, man`", 5)
    saviore = await eor(lol, "`Your banner is under creation wait a sec...`")
    text = deEmojify(text)
    await asyncio.sleep(2)
    saviorfile = await changemymind(text)
    await lol.client.send_file(lol.chat_id, saviorfile, reply_to=reply_to_id)
    await saviore.delete()
    if os.path.exists(saviorfile):
        os.remove(saviorfile)


@savior.savior_cmd(
    pattern="kanna(?:\s|$)([\s\S]*)",
    command=("kanna", menu_category),
    info={
        "header": "kanna chan sticker with given custom text",
        "usage": "{tr}kanna text",
        "examples": "{tr}kanna SaViorX is One of the Popular userbot",
    },
)
async def nekobot(lol):
    "kanna chan sticker with given custom text"
    text = lol.pattern_match.group(1)
    text = re.sub("&", "", text)
    reply_to_id = await reply_id(lol)

    reply = await lol.get_reply_message()
    if not text:
        if lol.is_reply and not reply.media:
            text = reply.message
        else:
            return await eod(lol, "**Kanna : **`What should i show you`", 5)
    saviore = await eor(lol, "`Kanna is writing your text...`")
    text = deEmojify(text)
    await asyncio.sleep(2)
    saviorfile = await kannagen(text)
    await lol.client.send_file(lol.chat_id, saviorfile, reply_to=reply_to_id)
    await saviore.delete()
    if os.path.exists(saviorfile):
        os.remove(saviorfile)


@savior.savior_cmd(
    pattern="tweet(?:\s|$)([\s\S]*)",
    command=("tweet", menu_category),
    info={
        "header": "The desired person tweet sticker with given custom text",
        "usage": "{tr}tweet <username> ; <text>",
        "examples": "{tr}tweet iamsrk ; SaViorX is One of the Popular userbot",
    },
)
async def nekobot(lol):
    "The desired person tweet sticker with given custom text"
    text = lol.pattern_match.group(1)
    text = re.sub("&", "", text)
    reply_to_id = await reply_id(lol)

    reply = await lol.get_reply_message()
    if not text:
        if lol.is_reply and not reply.media:
            text = reply.message
        else:
            return await eod(
                lol,
                "what should I tweet? Give some text and format must be like `.tweet username ; your text` ",
                5,
            )
    if ";" in text:
        username, text = text.split(";")
    else:
        await eod(
            lol,
            "__what should I tweet? Give some text and format must be like__ `.tweet username ; your text`",
            5,
        )
        return
    saviore = await eor(lol, f"`Requesting {username} to tweet...`")
    text = deEmojify(text)
    await asyncio.sleep(2)
    saviorfile = await tweets(text, username)
    await lol.client.send_file(lol.chat_id, saviorfile, reply_to=reply_to_id)
    await saviore.delete()
    if os.path.exists(saviorfile):
        os.remove(saviorfile)
