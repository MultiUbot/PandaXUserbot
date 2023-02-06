from io import BytesIO
from aiohttp import ClientSession

aiohttpsession = ClientSession()

async def make_carbon(code):
    url = "https://carbonara.vercel.app/api/cook"
    async with aiohttpsession.post(url, json={"code": code}) as resp:
        image = BytesIO(await resp.read())
    image.name = "carbon.png"
    return image


from pyrogram import filters

from userbot import babu as app
from userbot.core.decorators.errors import capture_err


@app.on_message(
    filters.command("carbon")
    & ~filters.edited
)
@capture_err
async def carbon_func(_, message):
    if not message.reply_to_message:
        return await message.reply_text(
            "Reply to a text message to make carbon."
        )
    if not message.reply_to_message.text:
        return await message.reply_text(
            "Reply to a text message to make carbon."
        )
    m = await message.reply_text("Prosessing Carbon")
    carbon = await make_carbon(message.reply_to_message.text)
    await m.edit("Uploading")
    await app.send_document(message.chat.id, carbon)
    await m.delete()
    carbon.close()
