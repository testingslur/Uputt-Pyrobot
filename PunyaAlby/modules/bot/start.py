# if you can read this, this meant you use code from Geez | Ram Project
# this code is from somewhere else
# please dont hestitate to steal it
# because Geez and Ram doesn't care about credit
# at least we are know as well
# who Geez and Ram is
#
#
# kopas repo dan hapus credit, ga akan jadikan lu seorang developer
# ©2023 Geez | Ram Team
import random
from PunyaAlby import app
from pyrogram import filters
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
from config import OWNER_ID as owner 

@app.on_callback_query()
def pmowner(client, callback_query):
    user_id = owner
    message = "Lu Siapa Anjeng!!!!"
    client.send_message(user_id, message)
    client.answer_callback_query(callback_query.id, text="Message sent")

logoalby = [
    "https://graph.org/file/f832baf4ee57272d4dd3f.jpg",
    "https://telegra.ph//file/a96bdaccd5beb26d4cd51.jpg",
    "https://telegra.ph//file/5779af04a54f14357f5b4.jpg",
    "https://telegra.ph//file/4f61d3c4e77e998f3e6d6.jpg"
]

alive_logo = random.choice(logoalby)

@app.on_message(filters.command("start") & filters.private)
async def start(app, message):
    chat_id = message.chat.id
    file_id = alive_logo
    caption = "Hi, Saya Asisstant ALBY-Pyrobot\nTidak Ada Yang Special Kecuali Manisnya kamu."
    reply_markup = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("Support", url="https://t.me/MT_Force"),
            InlineKeyboardButton("Channel", url="https://t.me/kontenMT"),
        ],
    ])

    await app.send_photo(chat_id, file_id, caption=caption, reply_markup=reply_markup)
