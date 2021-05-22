from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgUAAxkBAAEFSQABYJyJBCa9zcPfokSy21glVGJ0ZS8AArwCAAIepmlUA2tU7m0u6EkeBA")
    await message.reply_text(
        f"""👋🏻 Hai, Saya {bn} 🎵

Bot musik adalah bot sumber terbuka yang memungkinkan Anda memutar musik di grup telegram Anda.
Tidak mengetahui cara memakainya? Baca ᴘᴀɴᴅᴜᴀɴ ᴍᴇɴɢɢᴜɴᴀᴋᴀɴ ʙᴏᴛ agar langsung memahami tanpa bertanya!
─────────────────────
Kutipan: "Ada waktunya kita akan terpuruk dan menangis.
Tapi Percayalah di setiap tangis pasti akan ada kebahagiaan yang akan datang"
Dikelola oleh [ɢᴏᴏᴅ ʙᴏʏs](t.me/GB_03101999)!
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
