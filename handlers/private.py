from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2

GROUP_MUSIC_PROBOT_IMG= "https://telegra.ph/file/625c18e0b9335553152ac.jpg"

@Client.on_message(filters.command("start") & filters.private & ~filters.channel)
async def start(_, message: Message):
    await message.reply_photo(GROUP_MUSIC_PROBOT_IMG)
    await message.reply_text(
        f"""👋🏻 Hai {message.from_user.mention}

Saya adalah robot manager grup dan saya juga bisa memainkan musik di obrolan suara di grup anda
Silahkan baca panduan bot musik [klik disini](https://telegra.ph/GB-MUSIK-BOT-05-12)
Silahkan tekan > /help untuk melihat fitur manager saya
━─━─━─━─━─━─━─━─━─━─━
Kutipan: "Ada waktunya kita akan terpuruk dan menangis.
Tapi Percayalah di setiap tangis pasti akan ada kebahagiaan yang akan datang"
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [

                    InlineKeyboardButton(
                        "➗ Tambahkan Ke Grup➗", url="http://t.me/GB_MusikBot?startgroup=start")
                  ],[
                    InlineKeyboardButton(
                        "💳 Donasi", url="https://saweria.co/DonasiUntukAdmin"
                    ),
                    InlineKeyboardButton(
                        "Support 💬", url="https://t.me/GB_03101999"
                    )
            ]

     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start@GB_MusikBot") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**✅ Saya Sudah Online\n👤 Jangan Sampai Lupa Masukin Assistent Saya: @GB_Musik**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🗒️ Panduan", url="https://telegra.ph/GB-MUSIK-BOT-05-12")
                ]
            ]
        )
   )

