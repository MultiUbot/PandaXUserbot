from pyrogram import filters
from pyrogram.types import Message

from userbot import babu as app
from userbot.core.decorators.errors import capture_err
from telegraph import Telegraph
telegraph = Telegraph()

telegraph.create_account(short_name="Panda")

@app.on_message(filters.command("telegraph") & ~filters.edited)
@capture_err
async def paste(_, message: Message):
    reply = message.reply_to_message

    if not reply or not reply.text:
        return await message.reply("Reply to a text message")

    if len(message.command) < 2:
        return await message.reply("**Usage:**\n /telegraph [Page name]")

    page_name = message.text.split(None, 1)[1]
    page = telegraph.create_page(
        page_name, html_content=reply.text.html.replace("\n", "<br>")
    )
    return await message.reply(
        f"**Posted:** {page['url']}",
        disable_web_page_preview=True,
    )
