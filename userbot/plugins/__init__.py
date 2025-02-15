import math
import os
import re
import time

import heroku3
import lottie
import requests
import spamwatch as spam_watch
from validators.url import url

from .. import *
from ..Config import Config
from ..funcs.logger import logging
from ..funcs.managers import eod, eor
from ..funcs.session import savior
from ..helpers import *
from ..helpers.utils import _format, _saviortools, _saviorutils, install_pip, reply_id
from ..sql_helper.globals import gvarstatus

# =================== CONSTANT ===================
bot = savior
LOGS = logging.getLogger(__name__)
USERID = savior.uid if Config.OWNER_ID == 0 else Config.OWNER_ID
ALIVE_NAME = Config.ALIVE_NAME
AUTONAME = Config.AUTONAME
DEFAULT_BIO = Config.DEFAULT_BIO


Heroku = heroku3.from_key(Config.API_KEY)
heroku_api = "https://api.heroku.com"
APP_NAME = Config.APP_NAME
API_KEY = Config.API_KEY

thumb_image_path = os.path.join(Config.TMP_DOWNLOAD_DIRECTORY, "thumb_image.jpg")


# mention user
mention = f"[{Config.ALIVE_NAME}](tg://user?id={USERID})"
hmention = f"<a href = tg://user?id={USERID}>{Config.ALIVE_NAME}</a>"


SAVIOR_USER = savior.me.first_name
SaVior_Boy = savior.uid
savior_mention = f"[{SAVIOR_USER}](tg://user?id={SaVior_Boy})"


# pic
gban_pic = "./userbot/helpers/resources/pics/gban.mp4"
main_pic = "./userbot/helpers/resources/pics/main.jpg"
core_pic = "./userbot/helpers/resources/pics/core.jpg"
chup_pic = "./userbot/helpers/resources/pics/chup.mp4"
bsdk_pic = "./userbot/helpers/resources/pics/bsdk.jpg"
bsdkwale_pic = "./userbot/helpers/resources/pics/bsdk_wale.jpg"
chutiya_pic = "./userbot/helpers/resources/pics/chutiya.jpeg"
promote_pic = "./userbot/helpers/resources/pics/promote.mp4"
demote_pic = "./userbot/helpers/resources/pics/demote.jpg"
mute_pic = "./userbot/helpers/resources/pics/mute.jpg"
ban_pic = "./userbot/helpers/resources/pics/ban.mp4"


# channel
my_channel = Config.YOUR_CHANNEL or "SaViorSupport"
my_group = Config.YOUR_GROUP or "SaViorUpdates"
if "@" in my_channel:
    my_channel = my_channel.replace("@", "")
if "@" in my_group:
    my_group = my_group.replace("@", "")

# My Channel
chnl_link = "https://t.me/SaViorUpdates"
SaVior_channel = f"[ṠḀṼḭṏṙ]({chnl_link})"
grp_link = "https://t.me/SaViorSupport"
SaVior_grp = f"[ṠḀṼḭṏṙ]({grp_link})"


PM_START = []
PMMESSAGE_CACHE = {}
PMMENU = "pmpermit_menu" not in Config.NO_LOAD


TMP_DOWNLOAD_DIRECTORY = Config.TMP_DOWNLOAD_DIRECTORY

# spamwatch support
if Config.SPAMWATCH_API:
    token = Config.SPAMWATCH_API
    spamwatch = spam_watch.Client(token)
else:
    spamwatch = None


# ================================================

if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
    os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)


# thumb image
if Config.THUMB_IMAGE is not None:
    check = url(Config.THUMB_IMAGE)
    if check:
        try:
            with open(thumb_image_path, "wb") as f:
                f.write(requests.get(Config.THUMB_IMAGE).content)
        except Exception as e:
            LOGS.info(str(e))


def set_key(dictionary, key, value):
    if key not in dictionary:
        dictionary[key] = value
    elif isinstance(dictionary[key], list):
        if value in dictionary[key]:
            return
        dictionary[key].append(value)
    else:
        dictionary[key] = [dictionary[key], value]


async def make_gif(event, reply, quality=None, fps=None):
    fps = fps or 1
    quality = quality or 256
    result_p = os.path.join("temp", "animation.gif")
    animation = lottie.parsers.tgs.parse_tgs(reply)
    with open(result_p, "wb") as result:
        await _saviorutils.run_sync(
            lottie.exporters.gif.export_gif, animation, result, quality, fps
        )
    return result_p
