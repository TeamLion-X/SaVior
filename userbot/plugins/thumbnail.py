import os

from hachoir.metadata import extractMetadata
from hachoir.parser import createParser
from PIL import Image

from userbot import savior

from ..Config import Config
from ..funcs.managers import eor
from ..helpers.utils import _saviortools

menu_category = "utils"

# Thumbnail Utilities ported from uniborg
# credits @spechide


thumb_image_path = Config.TMP_DOWNLOAD_DIRECTORY + "/thumb_image.jpg"


@savior.savior_cmd(
    pattern="savethumb$",
    command=("savethumb", menu_category),
    info={
        "header": "To save replied image as temporary thumb.",
        "usage": "{tr}savethumb",
    },
)
async def _(event):
    "To save replied image as temporary thumb."
    saviorevent = await eor(event, "`Processing ...`")
    if not event.reply_to_msg_id:
        return await saviorevent.edit("`Reply to a photo to save custom thumbnail`")
    downloaded_file_name = await event.client.download_media(
        await event.get_reply_message(), Config.TMP_DOWNLOAD_DIRECTORY
    )
    if downloaded_file_name.endswith(".mp4"):
        metadata = extractMetadata(createParser(downloaded_file_name))
        if metadata and metadata.has("duration"):
            duration = metadata.get("duration").seconds
        downloaded_file_name = await _saviortools.take_screen_shot(
            downloaded_file_name, duration
        )
    # https://stackoverflow.com/a/21669827/4723940
    Image.open(downloaded_file_name).convert("RGB").save(thumb_image_path, "JPEG")
    # https://pillow.readthedocs.io/en/3.1.x/reference/Image.html#create-thumbnails
    os.remove(downloaded_file_name)
    await saviorevent.edit(
        "Custom video/file thumbnail saved. This image will be used in the upload, till `.clearthumb`. \nTo get : .getthumb"
    )


@savior.savior_cmd(
    pattern="clearthumb$",
    command=("clearthumb", menu_category),
    info={
        "header": "To delete thumb image.",
        "usage": "{tr}clearthumb",
    },
)
async def _(event):
    "To delete thumb image."
    if os.path.exists(thumb_image_path):
        os.remove(thumb_image_path)
    else:
        await eor(event, "`No thumbnail is set to clear`")
    await eor(event, "✅ Custom thumbnail cleared successfully.")


@savior.savior_cmd(
    pattern="getthumb$",
    command=("getthumb", menu_category),
    info={
        "header": "To get thumbnail of given video or gives your present thumbnail.",
        "usage": "{tr}getthumb",
    },
)
async def _(event):
    "To get thumbnail of given video or gives your present thumbnail"
    if event.reply_to_msg_id:
        r = await event.get_reply_message()
        try:
            a = await r.download_media(thumb=-1)
        except Exception as e:
            return await eor(event, str(e))
        try:
            await event.client.send_file(
                event.chat_id,
                a,
                force_document=False,
                allow_cache=False,
                reply_to=event.reply_to_msg_id,
            )
            os.remove(a)
            await event.delete()
        except Exception as e:
            await eor(event, str(e))
    elif os.path.exists(thumb_image_path):
        caption_str = "Currently Saved Thumbnail"
        await event.client.send_file(
            event.chat_id,
            thumb_image_path,
            caption=caption_str,
            force_document=False,
            allow_cache=False,
            reply_to=event.message.id,
        )
        await eor(event, caption_str)
    else:
        await eor(event, "Reply `.gethumbnail` as a reply to a media")
