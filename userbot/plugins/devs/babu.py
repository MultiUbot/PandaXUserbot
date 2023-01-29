
import re
import os
from asyncio import gather, get_event_loop, sleep

from aiohttp import ClientSession
from pyrogram import Client, filters, idle
from Python_ARQ import ARQ
from userbot import config
from userbot import babu

bot_id = int(config.BOT_TOKEN.split(":")[0])
arq = None

session = ClientSession()
arq = ARQ(config.ARQ_API_BASE_URL, config.ARQ_API_KEY, session)
   
async def babuQuery(query: str, user_id: int):
    query = (
        query
        if config.LANGUAGE == "id"
        else (await arq.translate(query, "id")).result.translatedText
    )
    resp = (await arq.luna(query, user_id)).result
    return (
        resp
        if config.LANGUAGE == "id"
        else (
            await arq.translate(resp, config.LANGUAGE)
        ).result.translatedText
    )


async def type_and_send(message):
    chat_id = message.chat.id
    user_id = message.from_user.id if message.from_user else 0
    query = message.text.strip()
    await message._client.send_chat_action(chat_id, "typing")
    response, _ = await gather(babuQuery(query, user_id), sleep(1))
    await message.reply_text(response)
    await message._client.send_chat_action(chat_id, "cancel")

@babu.on_message(
    ~filters.private
    & filters.text
    & ~filters.command("babu")
    & ~filters.edited,
    group=69,
)
async def chat(_, message):
    if message.reply_to_message:
        if not message.reply_to_message.from_user:
            return
        from_user_id = message.reply_to_message.from_user.id
        if from_user_id != bot_id:
            return
    else:
        match = re.search(
            "[.|\n]{0,}babu[.|\n]{0,}",
            message.text.strip(),
            flags=re.IGNORECASE,
        )
        if not match:
            return
    await type_and_send(message)



from pyrogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from userbot.utils.inline.apikeytele import apitelegram


@babu.on_callback_query()
async def _callbacks(client: Client, callback_query: CallbackQuery):
    user = await client.get_me()
    mention = user["mention"]
    query = callback_query.data.lower()
    if query.startswith("home"):
        if query == 'home':
            chat_id = callback_query.from_user.id
            message_id = callback_query.message.message_id
            await client.edit_message_text(
                chat_id=chat_id,
                message_id=message_id,
                text="Menu Utama",
                reply_markup=InlineKeyboardMarkup(keyboard),
            )
    elif query in ["hb13", "apikey"]:
        await callback_query.answer()
        try:
            if query == "hb13":
                await apitelegram(client, callback_query.message, apikey=True)
            else:
                await apitelegram(client, callback_query.message, apikey=True)
        except Exception as e:
            await callback_query.message.reply(f"Jika Eror lapor ke Devolover {e}")

               
