from faker import Faker

from . import eor, savior

menu_category = "useless"


@savior.savior_cmd(
    pattern="gencc(?:\s|$)([\s\S]*)",
    command=("gencc", menu_category),
    info={
        "header": "To Make Fake Credit Card in short help u to generate fake cc",
        "usage": [
            "{tr}gencc",
        ],
    },
)
async def _(SAVIORevent):
    if SAVIORevent.fwd_from:
        return
    SAVIORcc = Faker()
    SAVIORname = SAVIORcc.name()
    SAVIORadre = SAVIORcc.address()
    SAVIORcard = SAVIORcc.credit_card_full()

    await eor(
        SAVIORevent,
        f"__**👤 NAME :- **__\n`{SAVIORname}`\n\n__**🏡 ADDRESS :- **__\n`{SAVIORadre}`\n\n__**💸 CARD :- **__\n`{SAVIORcard}`",
    )
