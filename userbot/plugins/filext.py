import requests
from bs4 import BeautifulSoup

from userbot import savior

from ..funcs.managers import eor

menu_category = "utils"


@savior.savior_cmd(
    pattern="filext(?:\s|$)([\s\S]*)",
    command=("filext", menu_category),
    info={
        "header": "Shows you the detailed information of given extension type.",
        "usage": "{tr}filext <extension>",
        "examples": "{tr}filext py",
    },
)
async def _(event):
    "Shows you the detailed information of given extension type."
    sample_url = "https://www.fileext.com/file-extension/{}.html"
    input_str = event.pattern_match.group(1).lower()
    response_api = requests.get(sample_url.format(input_str))
    status_code = response_api.status_code
    if status_code == 200:
        raw_html = response_api.content
        soup = BeautifulSoup(raw_html, "html.parser")
        ext_details = soup.find_all("td", {"colspan": "3"})[-1].text
        await eor(
            event,
            f"**File Extension**: `{input_str}`\n**Description**: `{ext_details}`",
        )
    else:
        await eor(
            event,
            f"https://www.fileext.com/ responded with {status_code} for query: {input_str}",
        )
