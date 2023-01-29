#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.


from typing import Union
from userbot.utils.inline.apikeytele import apitelegram
from pyrogram import filters, types
from pyrogram.types import InlineKeyboardMarkup, Message

from userbot.config import BANNED_USERS
from strings import get_command, get_string, helpers
from userbot import app
from userbot.misc import SUDOERS
from userbot.utils import help_pannel
from userbot.utils.database import get_lang, is_commanddelete_on
from userbot.utils.decorators.language import (LanguageStart,
                                                  languageCB)
from userbot.utils.inline.help import (help_back_markup,
                                          private_help_panel)

### Command
HELP_COMMAND = get_command("HELP_COMMAND")


@app.on_message(
    filters.command(HELP_COMMAND)
    & filters.private
    & ~filters.edited
    & ~BANNED_USERS
)
@app.on_callback_query(
    filters.regex("settings_back_helper") & ~BANNED_USERS
)
async def helper_private(
    client: app, update: Union[types.Message, types.CallbackQuery]
):
    is_callback = isinstance(update, types.CallbackQuery)
    if is_callback:
        try:
            await update.answer()
        except:
            pass
        chat_id = update.message.chat.id
        language = await get_lang(chat_id)
        _ = get_string(language)
        keyboard = help_pannel(_, True)
        if update.message.photo:
            await update.message.delete()
            await update.message.reply_text(
                _["help_1"], reply_markup=keyboard
            )
        else:
            await update.edit_message_text(
                _["help_1"], reply_markup=keyboard
            )
    else:
        chat_id = update.chat.id
        if await is_commanddelete_on(update.chat.id):
            try:
                await update.delete()
            except:
                pass
        language = await get_lang(chat_id)
        _ = get_string(language)
        keyboard = help_pannel(_)
        await update.reply_text(_["help_1"], reply_markup=keyboard)


@app.on_message(
    filters.command(HELP_COMMAND)
    & filters.group
    & ~filters.edited
    & ~BANNED_USERS
)
@LanguageStart
async def help_com_group(client, message: Message, _):
    keyboard = private_help_panel(_)
    await message.reply_text(
        _["help_2"], reply_markup=InlineKeyboardMarkup(keyboard)
    )


@app.on_callback_query(filters.regex("help_callback") & ~BANNED_USERS)
@languageCB
async def helper_cb(client, CallbackQuery, _):
    callback_data = CallbackQuery.data.strip()
    cb = callback_data.split(None, 1)[1]
    keyboard = help_back_markup(_)
    if cb == "hb5":
        if CallbackQuery.from_user.id not in SUDOERS:
            return await CallbackQuery.answer(
                "Only for Sudo Users", show_alert=True
            )
        else:
            await CallbackQuery.edit_message_text(
                _["HELP_5"], reply_markup=keyboard
            )
            return await CallbackQuery.answer()
    try:
        await CallbackQuery.answer()
    except:
        pass
    if cb == "hb1":
        await CallbackQuery.edit_message_text(
            _["HELP_1"], reply_markup=keyboard
        )
    elif cb == "hb2":
        await CallbackQuery.edit_message_text(
            _["HELP_2"], reply_markup=keyboard
        )
    elif cb == "hb3":
        await CallbackQuery.edit_message_text(
            _["HELP_3"], reply_markup=keyboard
        )
    elif cb == "hb4":
        await CallbackQuery.edit_message_text(
            _["HELP_4"], reply_markup=keyboard
        )
    elif cb == "hb6":
        await CallbackQuery.edit_message_text(
            _["HELP_6"], reply_markup=keyboard
        )
    elif cb == "hb7":
        await CallbackQuery.edit_message_text(
            _["HELP_7"], reply_markup=keyboard
        )
    elif cb == "hb8":
        await CallbackQuery.edit_message_text(
            _["HELP_8"], reply_markup=keyboard
        )
    elif cb == "hb9":
        await CallbackQuery.edit_message_text(
            _["HELP_9"], reply_markup=keyboard
        )
    elif cb == "hb10":
        await CallbackQuery.edit_message_text(
            _["HELP_10"], reply_markup=keyboard
        )
    elif cb == "hb11":
        await CallbackQuery.edit_message_text(
            _["HELP_11"], reply_markup=keyboard
        )
    elif cb == "hb12":
        await CallbackQuery.edit_message_text(
            _["HELP_12"], reply_markup=keyboard
        )
    
