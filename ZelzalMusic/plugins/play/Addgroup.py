from pyrogram import Client, filters
from pyrogram.types import ChatMemberUpdated
from pyrogram.types import (
    Message,
    InlineKeyboardMarkup as Markup,
    InlineKeyboardButton as Button
)
from ZelzalMusic import app
import os

def added(_, __: Client, response: ChatMemberUpdated):
    if response.new_chat_member:
        return True if response.new_chat_member.user.id == __.me.id else False
    else: return False

Added = filters.create(added)

@app.on_chat_member_updated(Added & filters.group)
async def checkAdded(_: Client, response: ChatMemberUpdated):
    user_id = response.from_user.id
    chat_id = response.chat.id
    username = response.from_user.first_name
    OWNER_ID = 5449190469 # YOUR ID
    caption = f'‹ : تمت اضافة البوت الى المجموعه بواسطة {username} 🖤'
    ownername = (await _.get_chat(OWNER_ID)).first_name
    markup = Markup([[Button(ownername, user_id = OWNER_ID)]])
    bot = await _.get_chat(_.me.id)
    img = await app.download_media(bot.photo.big_file_id, file_name=os.path.join("./", "bot.jpg")) if bot.photo else 'https://telegra.ph/file/c8cab653cf02d05a25fa3.jpg'
    await _.send_photo(
        chat_id = response.chat.id, 
        photo = img,
        caption = caption,
        reply_markup = markup
    )
