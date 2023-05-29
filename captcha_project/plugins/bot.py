from pyrogram import Client, filters
from pyrogram.types import Message, CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup 
from emboy.captcha import captcha
random_items = []
random_image = ""
m_id = ""

@Client.on_message()
def main(c: Client, m: Message):
    global random_items, random_image , m_id
    if not random_items or not random_image:
        random_items, random_image = captcha("folder_img")
    
    btn = InlineKeyboardMarkup([
        [InlineKeyboardButton(text=random_items[0], callback_data=random_items[0])],
        [InlineKeyboardButton(text=random_items[1], callback_data=random_items[1])],
        [InlineKeyboardButton(text=random_items[2], callback_data=random_items[2])],
        [InlineKeyboardButton(text=random_items[3], callback_data=random_items[3])]
    ])
    
    if m.text == "/start":
       m_id = m.reply_photo("folder_img/" + random_image, reply_markup=btn)
@Client.on_callback_query()
def CallbackHandler(c: Client, call: CallbackQuery):
    global random_items , random_image , m_id
    if len(random_items) >= 4 and call.data == random_items[3]:
        c.delete_messages(chat_id=call.message.chat.id,message_ids=m_id.id)
        call.message.reply_text("True✅")
        del random_items[:]
        random_image = ""
    else:
        c.delete_messages(chat_id=call.message.chat.id,message_ids=m_id.id)
        call.message.reply_text("False🚫")
        del random_items[:]
        random_image = ""