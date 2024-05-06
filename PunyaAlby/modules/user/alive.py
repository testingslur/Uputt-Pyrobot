# Credits: @mrismanaziz
# Copyright (C) 2022 Pyro-ManUserbot
#
# This file is a part of < https://github.com/mrismanaziz/PyroMan-Userbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/mrismanaziz/PyroMan-Userbot/blob/main/LICENSE/>.
#
# t.me/SharingUserbot & t.me/Lunatic0de

import asyncio
import os
import time
from platform import python_version

from pyrogram import Client
from pyrogram import __version__ as versipyro
from pyrogram import filters
from pyrogram.types import Message
from telegraph import exceptions, upload_file

from config import BOT_VER, CHANNEL
from config import CMD_HANDLER
from config import GROUP
from PunyaAlby import CMD_HELP, StartTime
from PunyaAlby.helpers.basic import edit_or_reply
from PunyaAlby.helpers.PyroHelpers import ReplyCheck
from PunyaAlby.helpers.SQL.globals import gvarstatus
from PunyaAlby.helpers.tools import convert_to_image
from PunyaAlby.utils import get_readable_time
from PunyaAlby.utils.misc import restart

from .help import *

modules = CMD_HELP
alivemodules = CMD_HELP
alive_logo = (
    gvarstatus("ALIVE_LOGO") or ""
)
emoji = gvarstatus("ALIVE_EMOJI") or "✵"
alive_text = gvarstatus("ALIVE_TEKS_CUSTOM") or "l am alive✨"


@Client.on_message(filters.command(["alip", "awake"], cmd) & filters.me)
async def alip(client: Client, message: Message):
    alby = await edit_or_reply(message, "🥶")
    await asyncio.sleep(2)
    sad = client.send_video if alive_logo.endswith(".mp4") else client.send_photo
    uptime = await get_readable_time((time.time() - StartTime))
    man = (
        f"<b>{alive_text}</b>\n\n"
        f"{emoji} <b>Mᴀsᴛᴇʀ :</b> {client.me.mention} \n"
        f"{emoji} <b>Mᴏᴅᴜʟᴇs :</b> <code>{len(modules)} Modules</code> \n"
        f"{emoji} <b>Bot versi:</b> <code>{BOT_VER}</code> \n"
        f"{emoji} <b>Python versi:</b> <code>{python_version()}</code> \n"
        f"{emoji} <b>Pyrogram versi :</b> <code>{versipyro}</code> \n"
        f"{emoji} <b>Bot Uptime :</b> <code>{uptime}</code> \n\n"
        f"{emoji}**[𝗦𝘂𝗽𝗽𝗼𝗿𝘁](https://t.me/{GROUP})** \n" 
        f"{emoji}**[𝗖𝗵𝗮𝗻𝗻𝗲𝗹](https://t.me/{CHANNEL})** \n"
        f"{emoji}**[𝗢𝘄𝗻𝗲𝗿](tg://user?id={client.me.id})** \n"
    )
    try:
      await sad(
                message.chat.id,
                alive_logo,
                caption=man,
                reply_to_message_id=ReplyCheck(message),
            )
      await alby.delete()
    except:
      await alby.edit(man, disable_web_page_preview=True)


@Client.on_message(filters.command("setalivelogo", cmd) & filters.me)
async def setalivelogo(client: Client, message: Message):
    try:
        import PunyaAlby.helpers.SQL.globals as sql
    except AttributeError:
        await message.edit("**Running on Non-SQL mode!**")
        return
    PunyaAlby = await edit_or_reply(message, "`Processing...`")
    link = (
        message.text.split(None, 1)[1]
        if len(
            message.command,
        )
        != 1
        else None
    )
    if message.reply_to_message.media:
        if message.reply_to_message.sticker:
            m_d = await convert_to_image(message, client)
        else:
            m_d = await message.reply_to_message.download()
        try:
            media_url = upload_file(m_d)
        except exceptions.TelegraphException as exc:
            await PunyaAlby.edit(f"**ERROR:** `{exc}`")
            os.remove(m_d)
            return
        link = f"https://telegra.ph/{media_url[0]}"
        os.remove(m_d)
    sql.addgvar("ALIVE_LOGO", link)
    await PunyaAlby.edit(
        f"**Berhasil Mengcustom ALIVE LOGO Menjadi {link}**",
        disable_web_page_preview=True,
    )
    restart()


@Client.on_message(filters.command("setalivetext", cmd) & filters.me)
async def setalivetext(client: Client, message: Message):
    try:
        import PunyaAlby.helpers.SQL.globals as sql
    except AttributeError:
        await message.edit("**Running on Non-SQL mode!**")
        return
    text = (
        message.text.split(None, 1)[1]
        if len(
            message.command,
        )
        != 1
        else None
    )
    if message.reply_to_message:
        text = message.reply_to_message.text or message.reply_to_message.caption
    PunyaAlby = await edit_or_reply(message, "`Processing...`")
    if not text:
        return await edit_or_reply(
            message, "**Berikan Sebuah Text atau Reply ke text**"
        )
    sql.addgvar("ALIVE_TEKS_CUSTOM", text)
    await PunyaAlby.edit(f"**Berhasil Mengcustom ALIVE TEXT Menjadi** `{text}`")
    restart()


@Client.on_message(filters.command("setemoji", cmd) & filters.me)
async def setemoji(client: Client, message: Message):
    try:
        import PunyaAlby.helpers.SQL.globals as sql
    except AttributeError:
        await message.edit("**Running on Non-SQL mode!**")
        return
    emoji = (
        message.text.split(None, 1)[1]
        if len(
            message.command,
        )
        != 1
        else None
    )
    PunyaAlby = await edit_or_reply(message, "`Processing...`")
    if not emoji:
        return await edit_or_reply(message, "**Berikan Sebuah Emoji**")
    sql.addgvar("ALIVE_EMOJI", emoji)
    await PunyaAlby.edit(f"**Berhasil Mengcustom EMOJI ALIVE Menjadi** {emoji}")
    restart()

