import os
import time
from asyncio import sleep
from pyrogram import Client, filters
from pyrogram import enums, filters
from strings.filters import command
from ZelzalMusic import app

@app.on_message(~filters.private & command(["فحص الجروب","الجروب"]), group=2)
async def instatus(app, message):
    start_time = time.perf_counter()
    user = await app.get_chat_member(message.chat.id, message.from_user.id)
    count = await app.get_chat_members_count(message.chat.id)
    if user.status in (
        enums.ChatMemberStatus.ADMINISTRATOR,
        enums.ChatMemberStatus.OWNER,
    ):
        sent_message = await message.reply_text("جاري تجميع البينات 🔰⋅")
        deleted_acc = 0
        premium_acc = 0
        banned = 0
        bot = 0
        uncached = 0
        async for ban in app.get_chat_members(message.chat.id, filter=enums.ChatMembersFilter.BANNED):
            banned += 1
        async for member in app.get_chat_members(message.chat.id):
            user = member.user
            if user.is_deleted:
                deleted_acc += 1
            elif user.is_bot:
                bot += 1
            elif user.is_premium:
                premium_acc += 1
            else:
                uncached += 1
        end_time = time.perf_counter()
        timelog = "{:.2f}".format(end_time - start_time)
        await sent_message.edit(f"""
• ⌯ 𝙎𝙊𝙐𝙍𝘾𝙀 𝘿𝘼𝙍𝙆 ⌯ •
-᚜ - اسم الـجروب » ⦗ {message.chat.title} ⦘ 🌹 ⋅ 
-᚜ - عدد الاعضاء » ⦗ {count} ⦘ 👥 ⋅ 
-᚜ - عدد الـبوتات »  ⦗ {bot} ⦘ 🤖 ⋅
-᚜ - عدد الحسابات الـمحذوفه » ⦗ {deleted_acc} ⦘ 🗑️ ⋅ 
-᚜ - عدد المطرودين » ⦗ {banned} ⦘ ⛔ ⋅
-᚜ - عدد الاغنية اللي موثقين » ⦗ {premium_acc} ⦘ 😂♥️ ⋅""")
    else:
        sent_message = await message.reply_text("يمكن للمسؤولين فقط!")
        await sleep(5)
        await sent_message.delete()
