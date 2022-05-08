from ..funcs.session import savior
from . import ALIVE_NAME, eor

menu_category = "useless"


@savior.savior_cmd(
    pattern="dead ([\s\S]*)",
    command=("dead", menu_category),
    info={
        "header": "Just a art command try out yourself to see",
        "usage": "{tr}dead",
    },
)
async def lon(frog):
    "Fun art command"
    name = frog.pattern_match.group(1)
    D = (
        f"**{ALIVE_NAME} ~> {name} .\n\n**"
        "⣿⣿⣿⡇⠄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
        "⣿⣿⣿⡇⠄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
        "⣿⣿⣿⡇⠄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
        "⣿⣿⣿⡇⠄⣿⣿⣿⡿⠋⣉⣉⣉⡙⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
        "⣿⣿⣿⠃⠄⠹⠟⣡⣶⢟⣛⣛⡻⢿⣦⣩⣤⣬⡉⢻⣿⣿⣿⣿\n"
        "⣿⣿⣿⠄⢀⢤⣾⣿⣿⣿⡿⠿⠿⠿⢮⡃⣛⡻⢿⠈⣿⣿⣿⣿\n"
        "⣿⡟⢡⣴⣯⣿⣿⣿⠤⣤⣭⣶⣶⣶⣮⣔⡈⠛⢓⠦⠈⢻⣿⣿\n"
        "⠏⣠⣿⣿⣿⣿⣿⣿⣯⡪⢛⠿⢿⣿⣿⣿⡿⣼⣿⣿⣮⣄⠙⣿\n"
        "⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣾⡭⠴⣶⣶⣽⣽⣛⡿⠿⠿⠇⣿\n"
        "⣿⣿⣿⣿⣿⣿⣿⠿⣿⣿⣿⣿⣿⣿⣿⣷⣝⣛⢛⢋⣥⣴⣿⣿\n"
        "⣿⣿⣿⣿⣿⢿⠱⣿⣛⠾⣭⣛⡿⢿⣿⣿⣿⣿⣿⡀⣿⣿⣿⣿\n"
        "⠑⠽⡻⢿⣮⣽⣷⣶⣯⣽⣳⠮⣽⣟⣲⠯⢭⣿⣛⡇⣿⣿⣿⣿\n"
        "⠄⠄⠈⠑⠊⠉⠟⣻⠿⣿⣿⣿⣷⣾⣭⣿⠷⠶⠂⣴⣿⣿⣿⣿\n"
        "⠄⠄⠄⠄⠄⠄⠄⠁⠙⠒⠙⠯⠍⠙⢉⣡⣶⣿⣿⣿⣿⣿⣿⣿\n"
        "⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
    )
    await eor(frog, D)


P = (
    "╭━━━┳╮╱╱╭╮╱╭━━━┳━━━╮\n"
    "┃╭━╮┃┃╱╭╯╰╮┃╭━╮┃╭━╮┃\n"
    "┃╰━━┫╰━╋╮╭╯┃┃╱┃┃╰━━╮\n"
    "╰━━╮┃╭╮┣┫┃╱┃┃╱┃┣━━╮┃\n"
    "┃╰━╯┃┃┃┃┃╰╮┃╰━╯┃╰━╯┃\n"
    "╰━━━┻╯╰┻┻━╯╰━━━┻━━━╯\n"
)


@savior.savior_cmd(
    pattern="shitos$",
    command=("shitos", menu_category),
    info={
        "header": "Just a art command try out yourself to see",
        "usage": "{tr}shitos",
    },
)
async def bluedevilshitos(shitos):
    "fun art command"
    await eor(shitos, P)


R = (
    "███████▄▄███████████▄\n"
    "▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n"
    "▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n"
    "▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n"
    "▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n"
    "▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n"
    "▓▓▓▓▓▓███░░░░░░░░░░░░█\n"
    "██████▀░░█░░░░██████▀\n"
    "░░░░░░░░░█░░░░█\n"
    "░░░░░░░░░░█░░░█\n"
    "░░░░░░░░░░░█░░█\n"
    "░░░░░░░░░░░█░░█\n"
    "░░░░░░░░░░░░▀▀\n"
)


@savior.savior_cmd(
    pattern="dislike$",
    command=("dislike", menu_category),
    info={
        "header": "Just a art command try out yourself to see",
        "usage": "{tr}dislike",
    },
)
async def bluedislike(dislike):
    "fun art command"
    await eor(dislike, R)


@savior.savior_cmd(
    pattern="sthink ([\s\S]*)",
    command=("sthink", menu_category),
    info={
        "header": "Just a art command try out yourself to see",
        "usage": "{tr}sthink <text>",
    },
)
async def legedjjd(think):
    name = think.pattern_match.group(1)
    B = (
        f"**{ALIVE_NAME} ~> {name} .\n\n**"
        "⠀⠀⠀⠀⢀⣀⣀⣀\n"
        "⠀⠀⠀⠰⡿⠿⠛⠛⠻⠿⣷\n"
        "⠀⠀⠀⠀⠀⠀⣀⣄⡀⠀⠀⠀⠀⢀⣀⣀⣤⣄⣀⡀\n"
        "⠀⠀⠀⠀⠀⢸⣿⣿⣷⠀⠀⠀⠀⠛⠛⣿⣿⣿⡛⠿⠷\n"
        "⠀⠀⠀⠀⠀⠘⠿⠿⠋⠀⠀⠀⠀⠀⠀⣿⣿⣿⠇\n"
        "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠁\n"
        "⠀\n"
        "⠀⠀⠀⠀⣿⣷⣄⠀⢶⣶⣷⣶⣶⣤⣀\n"
        "⠀⠀⠀⠀⣿⣿⣿⠀⠀⠀⠀⠀⠈⠙⠻⠗\n"
        "⠀⠀⠀⣰⣿⣿⣿⠀⠀⠀⠀⢀⣀⣠⣤⣴⣶⡄\n"
        "⠀⣠⣾⣿⣿⣿⣥⣶⣶⣿⣿⣿⣿⣿⠿⠿⠛⠃\n"
        "⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄\n"
        "⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡁\n"
        "⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁\n"
        "⠀⠀⠛⢿⣿⣿⣿⣿⣿⣿⡿⠟\n"
    )
    if name:
        await eor(think, B)
    else:
        await eor(think, "Give Me Some Text")


@savior.savior_cmd(
    pattern="frog ([\s\S]*)",
    command=("frog", menu_category),
    info={
        "header": "Just a art command try out yourself to see",
        "usage": "{tr}frog <text>",
    },
)
async def lisj(frogsay):
    name = frogsay.pattern_match.group(1) or "No Mention"
    C = (
        f"**{ALIVE_NAME} ~> {name} .\n\n**"
        "⠄⠄⠄⠄⠄⣀⣀⣤⣶⣿⣿⣶⣶⣶⣤⣄⣠⣴⣶⣿⣶⣦⣄⠄\n"
        "⠄⣠⣴⣾⣿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦\n"
        "⢠⠾⣋⣭⣄⡀⠄⠙⠻⣿⣿⡿⠛⠋⠉⠉⠉⠙⠛⠿⣿⣿⣿⣿\n"
        "⡎⡟⢻⣿⣷⠄⠄⠄⠄⡼⣡⣾⣿⣿⣦⠄⠄⠄⠄⠄⠈⠛⢿⣿\n"
        "⡇⣷⣾⣿⠟⠄⠄⠄⢰⠁⣿⣇⣸⣿⣿⠄⠄⠄⠄⠄⠄⠄⣠⣼\n"
        "⣦⣭⣭⣄⣤⣤⣴⣶⣿⣧⡘⠻⠛⠛⠁⠄⠄⠄⠄⣀⣴⣿⣿⣿\n"
        "⢉⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣦⣶⣶⣶⣶⣿⣿⣿⣿⣿⣿\n"
        "⡿⠛⠛⠛⠛⠻⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
        "⡇⠄⠄⢀⣀⣀⠄⠄⠄⠄⠉⠉⠛⠛⠻⠿⣿⣿⣿⣿⣿⣿⣿⣿\n"
        "⠈⣆⠄⠄⢿⣿⣿⣷⣶⣶⣤⣤⣀⣀⡀⠄⠄⠉⢻⣿⣿⣿⣿⣿\n"
        "⠄⣿⡀⠄⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠂⠄⢠⣿⣿⣿⣿⣿\n"
        "⠄⣿⡇⠄⠄⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠄⢀⣼⣿⣿⣿⣿⣿\n"
        "⠄⣿⡇⠄⠠⣿⣿⣿⣿⣿⣿⣿⡿⠋⠄⠄⣠⣾⣿⣿⣿⣿⣿⣿\n"
        "⠄⣿⠁⠄⠐⠛⠛⠛⠉⠉⠉⠉⠄⠄⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿\n"
        "⠄⠻⣦⣀⣀⣀⣀⣀⣤⣤⣤⣤⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋\n"
    )
    await eor(frogsay, C)


@savior.savior_cmd(
    pattern="bye$",
    command=("bye", menu_category),
    info={
        "header": "Just a art command try out yourself to see",
        "usage": "{tr}bye",
    },
)
async def bluedevilbye(event):
    "fun art command"
    BYE_PIC = "https://te.legra.ph/file/aa16cad62645045062c0f.jpg"
    if BYE_PIC:
        event = await eor(event, "**❛ Bye ❜!**")
        lol = "Bye Friends"
        await event.delete()
        await event.client.send_file(event.chat_id, BYE_PIC, caption=lol)
