import random

from userbot import savior

from ..funcs.managers import eor
from . import saviormemes

menu_category = "fun"


@savior.savior_cmd(
    pattern="congo$",
    command=("congo", menu_category),
    info={
        "header": " Congratulate the people..",
        "usage": "{tr}congo",
    },
)
async def _(e):
    "Congratulate the people."
    txt = random.choice(saviormemes.CONGOREACTS)
    await eor(e, txt)


@savior.savior_cmd(
    pattern="shg$",
    command=("shg", menu_category),
    info={
        "header": "Shrug at it !!",
        "usage": "{tr}shg",
    },
)
async def shrugger(e):
    "Shrug at it !!"
    txt = random.choice(saviormemes.SHGS)
    await eor(e, txt)


@savior.savior_cmd(
    pattern="runs$",
    command=("runs", menu_category),
    info={
        "header": "Run, run, RUNNN!.",
        "usage": "{tr}runs",
    },
)
async def runner_lol(e):
    "Run, run, RUNNN!"
    txt = random.choice(saviormemes.RUNSREACTS)
    await eor(e, txt)


@savior.savior_cmd(
    pattern="noob$",
    command=("noob", menu_category),
    info={
        "header": "Whadya want to know? Are you a NOOB?",
        "usage": "{tr}noob",
    },
)
async def metoo(e):
    "Whadya want to know? Are you a NOOB?"
    txt = random.choice(saviormemes.NOOBSTR)
    await eor(e, txt)


@savior.savior_cmd(
    pattern="insult$",
    command=("insult", menu_category),
    info={
        "header": "insult someone.",
        "usage": "{tr}insult",
    },
)
async def insult(e):
    "insult someone."
    txt = random.choice(saviormemes.INSULT_STRINGS)
    await eor(e, txt)


@savior.savior_cmd(
    pattern="love$",
    command=("love", menu_category),
    info={
        "header": "Chutiyappa suru",
        "usage": "{tr}love",
    },
)
async def suru(chutiyappa):
    "Chutiyappa suru"
    txt = random.choice(saviormemes.LOVESTR)
    await eor(chutiyappa, txt)


@savior.savior_cmd(
    pattern="dhoka$",
    command=("dhoka", menu_category),
    info={
        "header": "Dhokha kha gya",
        "usage": "{tr}dhoka",
    },
)
async def katgya(chutiya):
    "Dhokha kha gya"
    txt = random.choice(saviormemes.DHOKA)
    await eor(chutiya, txt)


@savior.savior_cmd(
    pattern="hey$",
    command=("hey", menu_category),
    info={
        "header": "start a conversation with people",
        "usage": "{tr}hey",
    },
)
async def hoi(e):
    "start a conversation with people."
    txt = random.choice(saviormemes.HELLOSTR)
    await eor(e, txt)


@savior.savior_cmd(
    pattern="pro$",
    command=("pro", menu_category),
    info={
        "header": "If you think you're pro, try this.",
        "usage": "{tr}pro",
    },
)
async def proo(e):
    "If you think you're pro, try this."
    txt = random.choice(saviormemes.PRO_STRINGS)
    await eor(e, txt)


@savior.savior_cmd(
    pattern="react ?([\s\S]*)",
    command=("react", menu_category),
    info={
        "header": "Make your userbot react",
        "flags": [
            "happy",
            "think",
            "wave",
            "wtf",
            "love",
            "confused",
            "dead",
            "sad",
            "dog",
        ],
        "usage": ["{tr}react <type>", "{tr}react"],
    },
)
async def _(e):
    "Make your userbot react."
    input_str = e.pattern_match.group(1)
    if input_str in "happy":
        emoticons = saviormemes.FACEREACTS[0]
    elif input_str in "think":
        emoticons = saviormemes.FACEREACTS[1]
    elif input_str in "wave":
        emoticons = saviormemes.FACEREACTS[2]
    elif input_str in "wtf":
        emoticons = saviormemes.FACEREACTS[3]
    elif input_str in "love":
        emoticons = saviormemes.FACEREACTS[4]
    elif input_str in "confused":
        emoticons = saviormemes.FACEREACTS[5]
    elif input_str in "dead":
        emoticons = saviormemes.FACEREACTS[6]
    elif input_str in "sad":
        emoticons = saviormemes.FACEREACTS[7]
    elif input_str in "dog":
        emoticons = saviormemes.FACEREACTS[8]
    else:
        emoticons = saviormemes.FACEREACTS[9]
    txt = random.choice(emoticons)
    await eor(e, txt)


@savior.savior_cmd(
    pattern="10iq$",
    command=("10iq", menu_category),
    info={
        "header": "You retard !!",
        "usage": "{tr}10iq",
    },
)
async def iqless(e):
    "You retard !!"
    await eor(e, "♿")


@savior.savior_cmd(
    pattern="fp$",
    command=("fp", menu_category),
    info={
        "header": "send you face pam emoji!",
        "usage": "{tr}fp",
    },
)
async def facepalm(e):
    "send you face pam emoji!"
    await eor(e, "🤦‍♂")


@savior.savior_cmd(
    pattern="bt$",
    command=("bt", menu_category),
    info={
        "header": "Believe me, you will find this useful.",
        "usage": "{tr}bt",
    },
    groups_only=True,
)
async def bluetext(e):
    """Believe me, you will find this useful."""
    await eor(
        e,
        "/BLUETEXT /MUST /CLICK.\n"
        "/ARE /YOU /A /STUPID /ANIMAL /WHICH /IS /ATTRACTED /TO /COLOURS?",
    )


@savior.savior_cmd(
    pattern="session$",
    command=("session", menu_category),
    info={
        "header": "telethon session error code(fun)",
        "usage": "{tr}session",
    },
)
async def _(event):
    "telethon session error code(fun)."
    mentions = "**telethon.errors.rpcerrorlist.AuthKeyDuplicatedError: The authorization key (session file) was used under two different IP addresses simultaneously, and can no longer be used. Use the same session exclusively, or use different sessions (caused by GetMessagesRequest)**"
    await eor(event, mentions)
