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
    command(["سورس","السورس","سورس دارك","سورس احمد","دارك"])
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/b3e5093cb07c6185cd3fc.jpg",
        caption=f"""⍟ 𝚃𝙷𝙴 𝙱𝙴𝚂𝚃 𝚂𝙾𝚄𝚁𝙲𝙴 𝙾𝙽 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼""",
        reply_markup=InlineKeyboardMarkup(
        [
            [
                    InlineKeyboardButton(
                        "𝐀𝐝𝐝 𝐌𝐞 𝐓𝐨 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩", url=f"https://t.me/{app.username}?startgroup=true"),
                ],[
                    InlineKeyboardButton(
                        "𝐒𝐎𝐔𝐑𝐂𝐄 𝐃𝐀𝐑𝐊", url=f"https://t.me/D2_RK"),
                    InlineKeyboardButton(
                        "𝐒𝐎𝐔𝐑𝐂𝐄 𝐃𝐀𝐑𝐊", url=f"https://t.me/source_dr"),
                ],[
                    InlineKeyboardButton(
                        "𝐃𝐄𝐕 𝐀𝐇𝐌𝐄𝐃", url=f"https://t.me/A7_M3"),
                ],[
                    InlineKeyboardButton(
                        "𝐃𝐄𝐕 𝐃𝐀𝐑𝐊", url=f"https://t.me/X_D_A_R_K_X"),
                ],[
                    InlineKeyboardButton(text="𝐂𝐥𝐨𝐬𝐞", callback_data="close"),   
            ]
        ]
         ),
     )
  
