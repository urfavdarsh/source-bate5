

import asyncio

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from ZelzalMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from ZelzalMusic import app
from pyrogram import Client
from random import  choice, randint


@app.on_message(
    command(["مميزات","مميزات"])
 )
async def mmmezat(client, message):
        await message.reply_text(f"""مرحبًا بك عزيزي » {message.from_user.mention} في قسم مميزات ميوزك دارك \n

⌯ ميزة ⦂ المطور بيجيب مطور البوت 
⌯ ميزة ⦂ تنبيه بفتح وقفل الكول
⌯ ميزة ⦂ جروب بيجيب الجروب والرابط والايدي
⌯ ميزة ⦂ كت وتويت و حروف
⌯ ميزة ⦂ ا او ايدي لكشف معلوماتك
⌯ ميزة ⦂ جمالي بالرد بالصورة والنسبه
⌯ ميزة ⦂ اذاعه بالتثبيت او بالمساعد او عام
⌯ ميزة ⦂ افتح و اقفل الكول
⌯ ميزة ⦂ بث مباشر للقرآن وغيره في القنوات 
⌯ ميزة ⦂ سورس بيجيب معلومات السورس
⌯ ميزة ⦂ حظر من استخدام الميوزك
⌯ ميزة ⦂ الكتم في الجروبات
⌯ ميزة ⦂ رتبتي / الاحصائيات
⌯ ميزة ⦂ تفعيل الأدعيه و الاذكار
⌯ ميزة ⦂ مواقيت الصلاة
⌯ ميزة ⦂ اشعار بالدعوة في الكول
⌯ ميزة ⦂ بايو / نكته / انصحني
⌯ ميزة ⦂ سؤال / صراحه / حكم
⌯ ميزة ⦂ مميزات. بيجبلك مميزات الميوزك
⌯ ميزة ⦂ رفع و تنزيل مطور 
⌯ ميزة ⦂ تنزيل صوتيات
⌯ ميزة ⦂ مين في الكول وعددهم
⌯ ميزة ⦂ الرابط + رابط الجروب
⌯ ميزة ⦂ حساب العمر 2-9-2000
⌯ ميزة ⦂ لعبة البنك و ردود كلمة بوت
⌯ ميزة ⦂ اشعار تغيير صورة الجروب واللي غيرها
⌯ ميزة ⦂ فحص الجروب
⌯ ميزة ⦂ همسه / رايك بصورتي
⌯ ميزة ⦂ لو خيروك / كتابات
⌯ ميزة ⦂ اي حاجه تتبعت في البوت تجيلك في مجموعة السجل

لتنصيب بوت مشابه تواصل معي فالخاص @A7_M3""",


        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝙎𝙊𝙐𝙍𝘾𝙀 𝘿𝘼𝙍𝙆", url=f"https://t.me/D2_RK"),                        
                 ],[
                InlineKeyboardButton(
                        "Close", callback_data="close"),
               ],
          ]
        ),
    )

