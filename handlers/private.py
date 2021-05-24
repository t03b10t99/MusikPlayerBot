from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


GROUP_MUSIC_PROBOT_IMG= "https://telegra.ph/file/625c18e0b9335553152ac.jpg"

@Client.on_message(filters.command("start") & filters.private & ~filters.channel)
async def start(_, message: Message):
    await message.reply_photo(GROUP_MUSIC_PROBOT_IMG)
    await message.reply_text(
        f"""👋🏻 Hai {message.from_user.mention} saya {bn}

Saya bisa memutar musik di grup obrolan suara anda
Silahkan baca panduan cara menggunakan bot musik [klik sini](https://telegra.ph/GB-MUSIK-BOT-05-12)
━─━─━─━─━─━─━─━─━─━─━
Kutipan: Ada waktunya kita akan terpuruk dan menangis.
Tapi Percayalah di setiap tangis pasti akan ada kebahagiaan yang akan datang
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
                        "sᴜᴘᴘᴏʀᴛ 💬", url="https://t.me/GB_03101999"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**ɢʙ | ᴍᴜsɪᴋ Player Online ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🎁 ᴅᴏɴᴀsɪ", url="https://saweria.co/DonasiUntukAdmin")
                ]
            ]
        )
   )
