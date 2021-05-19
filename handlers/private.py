from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(filters.command("start") & filters.private & ~filters.channel)
async def start(_, message: Message):
    await message.reply_text(
        f"""👋🏻 Hai {message.from_user.mention}

Saya adalah robot manager grup dan saya juga bisa memainkan musik di obrolan suara di grup anda
Silahkan baca panduan bot musik [klik disini](https://telegra.ph/GB-MUSIK-BOT-05-12)
Silahkan tekan > /help untuk melihat fitur manager saya
━─━─━─━─━─━─━─━─━─━─━
Kutipan: "Ada waktunya kita akan terpuruk dan menangis.
Tapi Percayalah di setiap tangis pasti akan ada kebahagiaan yang akan datang"
Dikelola oleh [ɢᴏᴏᴅ ʙᴏʏs](t.me/GB_03101999)!
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🧾 𝗣𝗮𝗻𝗱𝘂𝗮𝗻 𝗠𝗲𝗻𝗴𝗴𝘂𝗻𝗮𝗸𝗮𝗻 𝗕𝗼𝘁 🧾", url="https://telegra.ph/GB-MUSIK-BOT-05-12")
                  ],[
                    InlineKeyboardButton(
                        "🎁 𝗗𝗼𝗻𝗮𝘀𝗶", url="https://saweria.co/DonasiUntukAdmin"
                    ),
                    InlineKeyboardButton(
                        "𝗣𝗲𝗺𝗶𝗹𝗶𝗸 👑", url="https://t.me/GB_03101999"
                    )
                ],[ 
                    InlineKeyboardButton(
                        " ➕ 𝗧𝗮𝗺𝗯𝗮𝗵𝗸𝗮𝗻 𝗞𝗲 𝗚𝗿𝘂𝗽 ➕", url="http://t.me/GB_MusikBot?startgroup=start"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start@GB_MusikBot") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**👋🏻 Hai, Terimakasih telah mengundang saya\n👇🏻 Silahkan klik tombol Panduan dibawah**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🗒️ Panduan", url="https://telegra.ph/GB-MUSIK-BOT-05-12")
                ]
            ]
        )
   )

