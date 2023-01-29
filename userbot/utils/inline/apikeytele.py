from logging import INFO, WARNING, FileHandler, StreamHandler, basicConfig, getLogger
LOGS = getLogger("Panda")
from random import choice, randint
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from asyncio.exceptions import TimeoutError
from pyrogram import Client, filters
import asyncio
import os
import sys
import subprocess

import requests
import bs4
os.system("clear")
loop = asyncio.get_event_loop()




async def cancelled(msg):
    if "/cancel" in msg.text:
        await msg.reply("Membatalkan Process!", quote=True, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Back", callback_data="settings_back_helper")]]))
        return True
    elif "/restart" in msg.text:
        await msg.reply("Memulai Ulang Bot!", quote=True, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Back", callback_data="settings_back_helper")]]))
        return True
    elif msg.text.startswith("/"):  # Bot Commands
        await msg.reply("Membatalkan process!", quote=True)
        return True
    else:
        return False






async def apitelegram(client, msg, apikey=False):
    user_id = msg.chat.id
    api_id_msg = await client.ask(user_id, 'Silahkan kirimkan  `No HP` Jika ingin membatalkan klik /cancel', filters=filters.text)
    if await cancelled(api_id_msg):
        return
    try:
        phone = int(api_id_msg.text)
    except ValueError:
        await api_id_msg.reply('Tidak Benar No hp Gunakan +62xxxxxxx. Please start lagi.', quote=True, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Back", callback_data="settings_back_helper")]]))
        return
    if apikey:
        await msg.reply(
          "Cek Kode disini",
      reply_markup=InlineKeyboardMarkup([[
        InlineKeyboardButton("Click here", url="tg://openmessage?user_id=777000")
        ]]))
    try:
        rastgele = requests.post("https://my.telegram.org/auth/send_password", data={"phone": phone}).json()["random_hash"]
    except Exception as ap:
        LOGS.info(f"ERROR - {ap}")
        exit(1)  
    code_msg = await client.ask(user_id, 'Mengirim  `code otp `', filters=filters.text)
    if await cancelled(api_id_msg):
        return
    hk_code = code_msg.text.replace(" ", "")
    try:
        cookie = requests.post("https://my.telegram.org/auth/login", data={"phone": phone, "random_hash": rastgele, "password": hk_code}).cookies.get_dict()
    except Exception as ap:
        LOGS.info(f"ERROR - {ap}")
        exit(1)  
    app = requests.post("https://my.telegram.org/apps", cookies=cookie).text
    soup = bs4.BeautifulSoup(app, features="html.parser")
    if soup.title.string == "Create new application":
            hashh = soup.find("input", {"name": "hash"}).get("value")
            app_title = choice(["pd", "panda", "pandabot", "pandauserbot", "telethon", "pyrogram"]) + choice(["", "-", "+", " "]) + choice(["user", "bot", "vue", "jsx", "python", "php"]) + choice([str(randint(10000, 99999)), ""])
            app_shortname = choice(["pd", "panda", "pandabot", "pandauserbot", "telethon", "pyrogram"]) + choice(["", "-", "+", " "]) + choice(["user", "bot", "vue", "jsx", "python", "php"]) + choice([str(randint(10000, 99999)), ""])
            AppInfo = {
                "hash": hashh,
                "app_title": app_title,
                "app_shortname": app_shortname,
                "app_url": "",
                "app_platform": choice(["android", "ios", "web", "desktop"]),
                "app_desc": choice(["madelineproto", "pyrogram", "telethon", "", "web", "cli"])
            }
            app = requests.post("https://my.telegram.org/apps/create", data=AppInfo, cookies=cookie).text
    try:
        newapp = requests.get("https://my.telegram.org/apps", cookies=cookie).text
        newsoup = bs4.BeautifulSoup(newapp, features="html.parser")
        g_inputs = newsoup.find_all("span", {"class": "form-control input-xlarge uneditable-input"})
        app_id = g_inputs[0].string
        api_hash = g_inputs[1].string
    except Exception as ap:
        LOGS.info(f"ERROR - {ap}")
        exit(1)      
    await msg.reply(
          f"Ini Adalah Data Kamu\n\n𝗔𝗣𝗜_𝗜𝗗: `{app_id}`\n𝗔𝗣𝗜_𝗛𝗔𝗦𝗛: `{api_hash}`",
      reply_markup=InlineKeyboardMarkup([[
        InlineKeyboardButton("DEV", url="https://t.me/diemmmmmmmmmm")
        ]])
    ) 
