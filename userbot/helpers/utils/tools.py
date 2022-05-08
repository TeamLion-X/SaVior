import os
from typing import Optional

from moviepy.editor import VideoFileClip
from PIL import Image

from ...funcs.logger import logging
from ...funcs.managers import eor
from ..tools import media_type
from .utils import runcmd

LOGS = logging.getLogger(__name__)


async def media_to_pic(event, reply, noedits=False):  # sourcery no-metrics
    mediatype = media_type(reply)
    if mediatype not in [
        "Photo",
        "Round Video",
        "Gif",
        "Sticker",
        "Video",
        "Voice",
        "Audio",
        "Document",
    ]:
        return event, None
    if not noedits:
        saviorevent = await eor(event, "`Transfiguration Time! Converting to ....`")

    else:
        saviorevent = event
    saviormedia = None
    saviorfile = os.path.join("./temp/", "meme.png")
    if os.path.exists(saviorfile):
        os.remove(saviorfile)
    if mediatype == "Photo":
        saviormedia = await reply.download_media(file="./temp")
        im = Image.open(saviormedia)
        im.save(saviorfile)
    elif mediatype in ["Audio", "Voice"]:
        await event.client.download_media(reply, saviorfile, thumb=-1)
    elif mediatype == "Sticker":
        saviormedia = await reply.download_media(file="./temp")
        if saviormedia.endswith(".tgs"):
            saviorcmd = f"lottie_convert.py --frame 0 -if lottie -of png '{saviormedia}' '{saviorfile}'"
            stdout, stderr = (await runcmd(saviorcmd))[:2]
            if stderr:
                LOGS.info(stdout + stderr)
        elif saviormedia.endswith(".webm"):
            clip = VideoFileClip(saviormedia)
            try:
                clip = clip.save_frame(saviorfile, 0.1)
            except Exception:
                clip = clip.save_frame(saviorfile, 0)
        elif saviormedia.endswith(".webp"):
            im = Image.open(saviormedia)
            im.save(saviorfile)
    elif mediatype in ["Round Video", "Video", "Gif"]:
        await event.client.download_media(reply, saviorfile, thumb=-1)
        if not os.path.exists(saviorfile):
            saviormedia = await reply.download_media(file="./temp")
            clip = VideoFileClip(saviormedia)
            try:
                clip = clip.save_frame(saviorfile, 0.1)
            except Exception:
                clip = clip.save_frame(saviorfile, 0)
    elif mediatype == "Document":
        mimetype = reply.document.mime_type
        mtype = mimetype.split("/")
        if mtype[0].lower() == "image":
            saviormedia = await reply.download_media(file="./temp")
            im = Image.open(saviormedia)
            im.save(saviorfile)
    if saviormedia and os.path.lexists(saviormedia):
        os.remove(saviormedia)
    if os.path.lexists(saviorfile):
        return saviorevent, saviorfile, mediatype
    return saviorevent, None


async def take_screen_shot(
    video_file: str, duration: int, path: str = ""
) -> Optional[str]:
    thumb_image_path = path or os.path.join(
        "./temp/", f"{os.path.basename(video_file)}.jpg"
    )
    command = f"ffmpeg -ss {duration} -i '{video_file}' -vframes 1 '{thumb_image_path}'"
    err = (await runcmd(command))[1]
    if err:
        LOGS.error(err)
    return thumb_image_path if os.path.exists(thumb_image_path) else None
