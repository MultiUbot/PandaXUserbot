import time
import asyncio
from datetime import datetime
from sys import version_info
import random
from pyrogram import __version__ as jembut
from pyrogram import filters
from pyrogram.types import Message

from userbot.config import ALIVE_LOGO, PREFIX
from userbot.core import ReplyCheck
from userbot import CMD_HELP, StartTime, userbot as app

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


@app.on_message(filters.command("alive", PREFIX) & filters.me)
async def alive(_, m):
    time.time()
    eek = m.from_user.first_name
    berak = m.from_user.id
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
        m.delete(),
        ahh(
            m.chat.id,
            {random.choice(ALIVE_LOGO)},
            caption=reply_msg,
            reply_to_message_id=ReplyCheck(m),
        ),
    )


@app.on_message(filters.command("ping", PREFIX) & filters.me)
async def pingme(_, message: Message):
    start = datetime.now()
    await message.edit("`Pong!`")
    end = datetime.now()
    m_s = (end - start).microseconds / 1000
    await message.edit(f"**Pong!**\n`{m_s} ms`")
