import nekos

from userbot import savior

from ..funcs.managers import eor

menu_category = "fun"


@savior.savior_cmd(
    pattern="why$",
    command=("why", menu_category),
    info={
        "header": "Sends you some random Funny questions",
        "usage": "{tr}why",
    },
)
async def hmm(savior):
    "Some random Funny questions"
    lol = nekos.why()
    await eor(savior, lol)


@savior.savior_cmd(
    pattern="fact$",
    command=("fact", menu_category),
    info={
        "header": "Sends you some random facts",
        "usage": "{tr}fact",
    },
)
async def hmm(savior):
    "Some random facts"
    tol = nekos.fact()
    await eor(savior, tol)
