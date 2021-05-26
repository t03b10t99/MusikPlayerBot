from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


GROUP_MUSIC_PROBOT_IMG= "https://telegra.ph/file/625c18e0b9335553152ac.jpg"

@Client.on_message(filters.command("start") & filters.private & ~filters.channel)
async def start(_, message: Message):
    await message.reply_photo(GROUP_MUSIC_PROBOT_IMG)
    await message.reply_text(
        f"""**┗┓ Hai {message.from_user.mention} Nama Saya Adalah {bn} ┏┛

Saya Bot Music Group, Yang Dapat Memutar Musik Di Voice Chat Group Dengan Cara Yang Mudah
Saya Memiliki Banyak Fitur Praktis Seperti :
┏━━━━━━━━━━━━━━
┣• Memutar Musik.
┣• Mendownload Musik.
┣• Mencari Musik Yang Ingin Di Putar Atau Di Download.
┗━━━━━━━━━━━━━━
❃ Cara Menggunakan: [BACA DISINI](https://telegra.ph/GB-MUSIK-BOT-05-12)
━━━━━━━━━━━━━━━
Kutipan: Ada Waktunya Kita Akan Terpuruk Dan Menangis.
Tapi Percayalah Di Setiap Tangis Pasti Akan Ada Kebahagiaan Yang Akan Datang**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➗ ᴛᴀᴍʙᴀʜᴋᴀɴ ᴋᴇ ɢʀᴜᴘ➗", url="http://t.me/GB_MusikBot?startgroup=start")
                  ],[
                    InlineKeyboardButton(
                        "💳 ᴅᴏɴᴀsɪ", url="https://saweria.co/DonasiUntukAdmin"
                    ),
                    InlineKeyboardButton(
                        "sᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ 💬", url="https://t.me/GB_03101999"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start@GB_MusikBot") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**👋🏻 Hai perkenalkan saya ɢʙ | ᴍᴜsɪᴋ ʙᴏᴛ\n👥 Jangan lupa masukin @GB_Musik**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🎟️ sᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ", url="https://t.me/GB_03101999")
                ]
            ]
        )
   )
