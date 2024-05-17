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
    command(["احمد","دارك","المطور","مبرمج السورس","مطور السورس","الهكر","الهقر","مطور"])
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/cc514ad2cb01a66e8eaa0.jpg",
        caption=f"""◉ 𝙽𝙰𝙼𝙴 : ❪𝗔 𝗵 𝗠 𝗲 𝗱❫
◉ 𝚄𝚂𝙴𝚁 : ❪ @A7_M3 ❫
◉ 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 : ❪ D2_RK.t.me ❫
◉ 𝙱𝙸𝙾    : ❪[#𝖱ꫀᥲ️ᥣᥣ𝗒,!Ꭵ ძ᥆ꪀ'𝗍 ᥴᥲ️𝗋ꫀ#ɪ'َᴍ 𓏺 𝗔 𝗵 𝗠 𝗲 𝗱 𓏺 ¹🦅🇪🇬](https://t.me/D2_RK ❫""",
        reply_markup=InlineKeyboardMarkup(
        [
            [
                    InlineKeyboardButton(
                        "𝗔 𝗵 𝗠 𝗲 𝗱", url=f"https://t.me/A7_M3"),
            ]
        ]
         ),
     )
  
