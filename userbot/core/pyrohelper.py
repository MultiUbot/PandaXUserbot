import shlex
from pyrogram import Client
from pyrogram.types import Message


from userbot.utils.database.welcomedb import get_welcome
from userbot.utils.database.afkdb import get_afk_status
from userbot.utils.database.pmpermitdb import get_approved_users, pm_guard


def get_arg(message):
    msg = message.text
    msg = msg.replace(" ", "", 1) if msg[1] == " " else msg
    split = msg[1:].replace("\n", " \n").split(" ")
    if " ".join(split[1:]).strip() == "":
        return ""
    return " ".join(split[1:])


def get_args(message):
    try:
        message = message.text
    except AttributeError:
        pass
    if not message:
        return False
    message = message.split(maxsplit=1)
    if len(message) <= 1:
        return []
    message = message[1]
    try:
        split = shlex.split(message)
    except ValueError:
        return message  # Cannot split, let's assume that it's just one long message
    return list(filter(lambda x: len(x) > 0, split))


async def user_afk(filter, client: Client, message: Message):
    check = await get_afk_status()
    if check:
        return True
    else:
        return False

async def denied_users(filter, client: Client, message: Message):
    if not await pm_guard():
        return False
    if message.chat.id in (await get_approved_users()):
        return False
    else:
        return True

def ReplyCheck(message: Message):
    reply_id = None
    if message.reply_to_message:
        reply_id = message.reply_to_message.id
    elif not message.from_user.is_self:
        reply_id = message.id
    return reply_id


async def welcome_chat(filter, client: Client, message: Message):
    to_welcome = await get_welcome(str(message.chat.id))
    if to_welcome:
        return True
    else:
        return False

class Pandabot:
    REPO = """
    ❏ **Hai👋🏻**, Saya Menggunakan **Panda-Userbot**
    └» **Group :** [Prime Support](https://t.me/TeamSquadUserbotSupport)
    └» **Channel :** [Prime Channel](https://t.me/PandaUserbot)
    └» **Owner Repo :** {} & {}
    └» **Repo :** [Prime-Userbot](https://github.com/ilhammansiz/PandaX_Userbot)
    """
    DEPLOY = """
    Jika kamu ingin menggunakan repo ini bisa deploy dibawah sini👇🏻
    [🤖Deploy via Bot🤖](https://t.me/herokudev_pandabot)
    [🌐Deploy via Web🌐](https://heroku.com/deploy?template=https://github.com/ilhammansiz/PandaX_Userbot)
    """
