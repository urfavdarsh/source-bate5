import asyncio

import os
import time
import requests
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from ZelzalMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from ZelzalMusic import app
from random import  choice, randint

                
@app.on_message(
    command(["مصطفى","بطيخ","المطور","مبرمج السورس","مطور السورس","الهكر","الهقر","مطور"])
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/cc514ad2cb01a66e8eaa0.jpg",
        caption=f"""◉ 𝙽𝙰𝙼𝙴 : ❪ 𝐌 𝐔 𝐒 𝐓 𝐀 𝐅 𝐀❫
◉ 𝚄𝚂𝙴𝚁 : ❪ @urfav_darsh ❫
◉ 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 : ❪ urfav_darsh2.t.me ❫
◉ 𝙱𝙸𝙾    : ❪[#𝖱ꫀᥲ️ᥣᥣ𝗒,!Ꭵ ძ᥆ꪀ'𝗍 ᥴᥲ️𝗋ꫀ#ɪ'َᴍ 𓏺 𝐌 𝐔 𝐒 𝐓 𝐀 𝐅 𝐀 𓏺 ¹🦅🇪🇬](https://t.me/urfav_darsh2 ❫""",
        reply_markup=InlineKeyboardMarkup(
        [
            [
                    InlineKeyboardButton(
                        "𝐌 𝐔 𝐒 𝐓 𝐀 𝐅 𝐀", url=f"https://t.me/urfav_darsh"),
            ]
        ]
         ),
     )
  
