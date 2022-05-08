# collage plugin for SaViorX by @SaViorXBoy

# Copyright (C) 2020 Alfiananda P.A
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.import os

import os

from userbot import savior

from ..funcs.managers import eod, eor
from ..helpers import reply_id
from ..helpers.utils import _saviorutils
from . import make_gif

menu_category = "utils"


@savior.savior_cmd(
    pattern="collage(?:\s|$)([\s\S]*)",
    command=("collage", menu_category),
    info={
        "header": "To create collage from still images extracted from video/gif.",
        "description": "Shows you the grid image of images extracted from video/gif. you can customize the Grid size by giving integer between 1 to 9 to cmd by default it is 3",
        "usage": "{tr}collage <1-9> <reply to  ani sticker/mp4.",
    },
)
async def collage(event):
    "To create collage from still images extracted from video/gif."
    saviorinput = event.pattern_match.group(1)
    reply = await event.get_reply_message()
    saviorid = await reply_id(event)
    event = await eor(event, "```Wait A Minute Its Collaging😁```")
    if not (reply and (reply.media)):
        await event.edit("`Media not found...`")
        return
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    saviorsticker = await reply.download_media(file="./temp/")
    if not saviorsticker.endswith((".mp4", ".mkv", ".tgs")):
        os.remove(saviorsticker)
        await event.edit("`Media format is not supported...`")
        return
    if saviorinput:
        if not saviorinput.isdigit():
            os.remove(saviorsticker)
            await event.edit("`You input is invalid, check help`")
            return
        saviorinput = int(saviorinput)
        if not 0 < saviorinput < 10:
            os.remove(saviorsticker)
            await event.edit(
                "`Why too big grid you cant see images, use size of grid between 1 to 9`"
            )
            return
    else:
        saviorinput = 3
    if saviorsticker.endswith(".tgs"):
        hmm = await make_gif(event, saviorsticker)
        if hmm.endswith(("@tgstogifbot")):
            os.remove(saviorsticker)
            return await event.edit(hmm)
        collagefile = hmm
    else:
        collagefile = saviorsticker
    endfile = "./temp/collage.png"
    saviorcmd = f"vcsi -g {saviorinput}x{saviorinput} '{collagefile}' -o {endfile}"
    stdout, stderr = (await _saviorutils.runcmd(saviorcmd))[:2]
    if not os.path.exists(endfile):
        for files in (saviorsticker, collagefile):
            if files and os.path.exists(files):
                os.remove(files)
        return await eod(
            event, "`media is not supported or try with smaller grid size`", 5
        )

    await event.client.send_file(
        event.chat_id,
        endfile,
        reply_to=saviorid,
    )
    await event.delete()
    for files in (saviorsticker, collagefile, endfile):
        if files and os.path.exists(files):
            os.remove(files)
