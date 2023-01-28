import time
import asyncio
from datetime import datetime
from sys import version_info
import random
from pyrogram import __version__ as jembut
from pyrogram import filters
from pyrogram.types import Message
from datetime import datetime

from pyrogram import filters
from pyrogram.types import Message

from userbot.config import BANNED_USERS, MUSIC_BOT_NAME, PING_IMG_URL
from strings import get_command
from userbot import userbot
from userbot.Session.call import Panda as Yukki
from userbot.utils import bot_sys_stats
from userbot.utils.decorators.language import language


from userbot.config import ALIVE_LOGO, PREFIX
from userbot.core import ReplyCheck
from userbot import CMD_HELP, StartTime
app = userbot
CMD_HELP.update(
    {
        "alive": f"""
『 **Alive** 』
  `{PREFIX}alive` -> Pamerkan kepada orang-orang dengan bot Anda menggunakan perintah ini.
  `{PREFIX}ping` -> Menampilkan kecepatan respons bot.
"""
    }
)

__major__ = 0
__minor__ = 2
__micro__ = 1

__python_version__ = f"{version_info[0]}.{version_info[1]}.{version_info[2]}"


def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time


@userbot.on_message(
    filters.command("alive", PREFIX)
    & filters.group
    & ~filters.edited
    & ~filters.me
)
async def alive(client, message: Message, _):
    time.time()
    eek = message.from_user.first_name
    berak = message.from_user.id
    ahh = app.send_video if {random.choice(ALIVE_LOGO)}.endswith(".mp4") else app.send_photo
    uptime = get_readable_time((time.time() - StartTime))
    reply_msg = f"┌───────═━┈━═──────\n► **Panda Userbot**\n"
    reply_msg += f"► Modules : `{len(CMD_HELP)}`\n"
    reply_msg += f"► Python: `{__python_version__}`\n"
    reply_msg += f"► Pyrogram : `{jembut}`\n"
    reply_msg += f"► Version  : `3.2.1`\n"
    reply_msg += f"► Owner: [{eek}](tg://user?id={berak})\n"
    time.time()
    reply_msg += f"►Uptime  : `{uptime}`\n└───────═━┈━═──────"
    await asyncio.gather(
        message.delete(),
        ahh(
            message.chat.id,
            {random.choice(ALIVE_LOGO)},
            caption=reply_msg,
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@userbot.on_message(
    filters.command("ping", PREFIX)
    & filters.group
    & ~filters.edited
    & ~filters.me
)
@language
async def ping_com(client, message: Message, _):
    response = await message.reply_photo(
        photo=PING_IMG_URL,
        caption=_["ping_1"],
    )
    start = datetime.now()
    pytgping = await Yukki.ping()
    UP, CPU, RAM, DISK = await bot_sys_stats()
    resp = (datetime.now() - start).microseconds / 1000
    await response.edit_text(
        _["ping_2"].format(
            MUSIC_BOT_NAME, resp, UP, DISK, CPU, RAM, pytgping
        )
    )
