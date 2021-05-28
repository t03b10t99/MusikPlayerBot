from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


GROUP_MUSIC_PROBOT_IMG= "https://telegra.ph/file/625c18e0b9335553152ac.jpg"

@Client.on_message(filters.command("help") & filters.private & ~filters.channel)
async def start(_, message: Message):
    await message.reply_photo(GROUP_MUSIC_PROBOT_IMG)
    await message.reply_text(
        f"""**┗┓ Hai {message.from_user.mention} Nama Saya Adalah {bn} ┏┛**

**Bagaimana Cara Menggunakannya?**
1) Pertama tambahkan bot @GB_MusikBot ke grup Anda dan berikan hak admin penuh
2) Kemudian tambahkan assistent @GB_Musik ke grup Anda dan berikan hak admin
3) Setelah itu ikuti perintah di bawah ini.
**PERINTAH UNTUK SEMUA ANGGOTA GRUP**
• /play - balas url youtube atau file lagu untuk memutar lagu
• /play [song name] - putar lagu yang Anda minta
• /song [song name] - unduh lagu yang Anda inginkan dengan cepat
• /search [song name] - Cari video di youtube dengan detail

**PERINTAH UNTUK SEMUA ADMIN GRUP**
• /pause - jeda pemutaran lagu
• /resume - lanjutkan pemutaran lagu
• /skip - mainkan lagu berikutnya
• /end - hentikan pemutaran musik

**📝 CATATAN:
• Untuk menghindari bot error jangan melakukan spam musik ke dalam antrian sekaligus
• Musik yang melebihi waktu 1 jam tidak dapat diputar di voice chat
• Jika userbot tidak mau ke voice chat akhiri obrolan suara dan mulai lagi obrolan suara nya
• Jika ada masalah silahkan hubungi [ɢᴏᴏᴅ ʙᴏʏs](https://t.me/GB_03101999) Terimakasih**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➗ ᴛᴀᴍʙᴀʜᴋᴀɴ ᴋᴇ ɢʀᴜᴘ➗", url="http://t.me/GB_MusikBot?startgroup=start")
                  ],[
                    InlineKeyboardButton(
                        "🎁 ᴅᴏɴᴀsɪ", url="https://saweria.co/DonasiUntukAdmin"
                    ),
                    InlineKeyboardButton(
                        "sᴜᴘᴘᴏʀᴛ 💬", url="https://t.me/GB_03101999"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("help@GB_MusikBot") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**Bagaimana Cara Menggunakannya?**
1) Pertama tambahkan bot @GB_MusikBot ke grup Anda dan berikan hak admin penuh
2) Kemudian tambahkan assistent @GB_Musik ke grup Anda dan berikan hak admin
3) Setelah itu ikuti perintah di bawah ini.
**PERINTAH UNTUK SEMUA ANGGOTA GRUP**
• /play - balas url youtube atau file lagu untuk memutar lagu
• /play [song name] - putar lagu yang Anda minta
• /song [song name] - unduh lagu yang Anda inginkan dengan cepat
• /search [song name] - Cari video di youtube dengan detail

**PERINTAH UNTUK SEMUA ADMIN GRUP**
• /pause - jeda pemutaran lagu
• /resume - lanjutkan pemutaran lagu
• /skip - mainkan lagu berikutnya
• /end - hentikan pemutaran musik

**📝 CATATAN:
• Untuk menghindari bot error jangan melakukan spam musik ke dalam antrian sekaligus
• Musik yang melebihi waktu 1 jam tidak dapat diputar di voice chat
• Jika userbot tidak mau ke voice chat akhiri obrolan suara dan mulai lagi obrolan suara nya
• Jika ada masalah silahkan hubungi [ɢᴏᴏᴅ ʙᴏʏs](https://t.me/GB_03101999) Terimakasih**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💬 sᴜᴘᴘᴏʀᴛ", url="https://t.me/GB_03101999"),

                    InlineKeyboardButton(
                        "ᴅᴏɴᴀsɪ 🎁", url="https://saweria.co/DonasiUntukAdmin")
                ]
            ]
        )
   )
