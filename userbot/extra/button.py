from pyrogram import Client
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from .apikeytele import apitelegram


ERROR_MESSAGE = "Oops! \n\n**Error😔** : {} " \
            "\n\nHelp to @diemmmmmmmmmm Erors"

               
@Client.on_callback_query()
async def _callbacks(bot: Client, callback_query: CallbackQuery):
    user = await bot.get_me()
    # user_id = callback_query.from_user.id
    mention = user["mention"]
    query = callback_query.data.lower()
    if query.startswith("home"):
        if query == 'home':
            chat_id = callback_query.from_user.id
            message_id = callback_query.message.message_id
            await bot.edit_message_text(
                chat_id=chat_id,
                message_id=message_id,
                text="Menu Utama",
                reply_markup=InlineKeyboardMarkup(keyboard),
            )  
    elif query in ["hb13"]:
        await callback_query.answer()
        try:
            if query == "hb13":
                await apitelegram(bot, callback_query.message)
        except Exception as e:
            await callback_query.message.reply(ERROR_MESSAGE.format(str(e)))
  
