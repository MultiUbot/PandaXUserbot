#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.

import asyncio
import importlib
import sys

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall
from aiohttp import ClientSession
from userbot import config
from userbot.config import BANNED_USERS
from userbot import LOGGER, app, userbot, babu, extrabot
from userbot.Session.call import Panda
from userbot.plugins import ALL_MODULES
from userbot.utils.database import get_banned_users, get_gbanned
from Python_ARQ import ARQ
loop = asyncio.get_event_loop()


async def init():
    global arq
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER("userbot").error(
            "No Assistant Clients Vars Defined!.. Exiting Process."
        )
        return
    if (
        not config.SPOTIFY_CLIENT_ID
        and not config.SPOTIFY_CLIENT_SECRET
    ):
        LOGGER("userbot").warning(
            "No Spotify Vars defined. Your bot won't be able to play spotify queries."
        )
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    await babu.start()
    await userbot.start()
    for all_module in ALL_MODULES:
        importlib.import_module("userbot.plugins" + all_module)
    LOGGER("userbot.plugins").info(
        "Successfully Imported Modules "
    )
    await Panda.start()
    try:
        await Panda.stream_call(
            "http://docs.evostream.com/sample_content/assets/sintel1m720p.mp4"
        )
    except NoActiveGroupCall:
        LOGGER("userbot").error(
            "[ERROR] - \n\nPlease turn on your Logger Group's Voice Call. Make sure you never close/end voice call in your log group"
        )
        sys.exit()
    except:
        pass
    await Panda.decorators()
    LOGGER("userbot").info("Panda Music Bot Started Successfully")
    await idle()


if __name__ == "__main__":
    loop.run_until_complete(init())
    LOGGER("userbot").info("Stopping Panda Music Bot! GoodBye")
