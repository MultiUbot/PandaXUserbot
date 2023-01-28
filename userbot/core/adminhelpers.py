from time import sleep

from pyrogram.types import Message
from userbot.Session import userbot


async def CheckAdmin(message: Message):
    """Check if we are an admin."""
    SELF = await userbot.get_chat_member(
        chat_id=message.chat.id, user_id=message.from_user.id
    )

    if message.chat.type in ["private", "bot"]:
        # You Are Boss Of Pvt Chats.
        return True

    if SELF.status in ("creator", "administrator")::
        await message.edit("__I'm not Admin!__")
        sleep(2)
        await message.delete()

    else:
        if SELF.status in ("creator", "administrator"):
            return True
        else:
            await message.edit("__No Permissions to restrict Members__")
            sleep(2)
            await message.delete()
          
