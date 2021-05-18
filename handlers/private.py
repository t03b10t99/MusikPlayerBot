from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgUAAx0CTvHoHwACVxZgoeo1z6IvIuovhaKpGgT777YyegACOAIAAounEFUEmmIndT6-Ix8E")
    await message.reply_text(
        f"""👋🏻 Hai {message.from_user.first_name}

Bot musik adalah bot sumber terbuka yang memungkinkan Anda memutar musik di grup telegram Anda.
Tidak mengetahui cara memakainya? Baca ᴘᴀɴᴅᴜᴀɴ ᴍᴇɴɢɢᴜɴᴀᴋᴀɴ ʙᴏᴛ agar langsung memahami tanpa bertanya!
━─━─━─━─━─━─━─━─━─━─━
Kutipan: "Ada waktunya kita akan terpuruk dan menangis.
Tapi Percayalah di setiap tangis pasti akan ada kebahagiaan yang akan datang"
Dikelola oleh [ɢᴏᴏᴅ ʙᴏʏs](t.me/GB_03101999)!
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🧾 ᴘᴀɴᴅᴜᴀɴ ᴍᴇɴɢɢᴜɴᴀᴋᴀɴ ʙᴏᴛ 🧾", url="https://telegra.ph/GB-MUSIK-BOT-05-12")
                  ],[
                    InlineKeyboardButton(
                        "🎁 ᴅᴏɴᴀsɪ", url="https://saweria.co/DonasiUntukAdmin"
                    ),
                    InlineKeyboardButton(
                        "ᴘᴇᴍɪʟɪᴋ 👑", url="https://t.me/GB_03101999"
                    )
                ],[ 
                    InlineKeyboardButton(
                        " ➕ ᴛᴀᴍʙᴀʜᴋᴀɴ ᴋᴇ ɢʀᴜᴘ ➕", url="http://t.me/GB_MusikBot?startgroup=start"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start@GB_MusikBot") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**✅ Jangan lupa beri saya hak admin agar saya dapat berjalan dengan baik**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🗒️ Panduan", url="https://telegra.ph/GB-MUSIK-BOT-05-12")
                ]
            ]
        )
   )

