from time import sleep

from pyrogram.types import Message
from pyrogram import enums

from userbot.Session import userbot


async def CheckAdmin(message: Message):
    """Check if we are an admin."""
    admin = enums.ChatMemberStatus.ADMINISTRATOR
    creator = enums.ChatMemberStatus.OWNER
    ranks = [admin, creator]

    SELF = await userbot.get_chat_member(
        chat_id=message.chat.id, user_id=message.from_user.id
    )

    if SELF.status not in ranks:
        await message.edit("__I'm not Admin!__")
        sleep(2)
        await message.delete()

    else:
        if SELF.status is not admin or SELF.privileges:
            return True
        else:
            await message.edit("__No Permissions to restrict Members__")
            sleep(2)
            await message.delete()
          
