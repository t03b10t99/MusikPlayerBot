from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


GB_MUSIK_BOT_IMG= "https://telegra.ph/file/625c18e0b9335553152ac.jpg"

@Client.on_message(filters.command("start") & filters.private & ~filters.channel)
async def start(_, message: Message):
    await message.reply_photo(GB_MUSIK_BOT_IMG)
    await message.reply_text(
        f"""**┗┓ Hai {message.from_user.mention} Nama Saya Adalah {bn} ┏┛

Saya Bot Music Group, Yang Dapat Memutar Musik Di Voice Chat Group Dengan Cara Yang Mudah
Saya Memiliki Banyak Fitur Praktis Seperti :
┏━━━━━━━━━━━━━━
┣• Memutar Musik.
┣• Mendownload Musik.
┣• Mencari Musik Yang Ingin Di Putar Atau Di Download.
┗━━━━━━━━━━━━━━
❃ Tekan: > /help < Untuk Melihat Cara Menggunakan Bot
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
                        "🎁 ᴅᴏɴᴀsɪ", url="https://saweria.co/DonasiUntukAdmin"
                    ),
                    InlineKeyboardButton(
                        "sᴜᴘᴘᴏʀᴛ 💬", url="https://t.me/GB_03101999"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start@GB_MusikBot") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**BAGAIMANA CARA MENGGUNAKANNYA?**
1) Pertama Tambahkan Bot @GB_MusikBot Ke Grup Anda Dan Berikan Hak Admin Penuh
2) Kemudian Tambahkan Assistent @GB_Musik Ke Grup Anda Dan Berikan Hak Admin
3) Setelah itu ikuti perintah di bawah ini.
**PERINTAH UNTUK SEMUA ANGGOTA GRUP**
• /play - balas url youtube atau file lagu untuk memutar lagu
• /play [judul musik] - putar lagu yang Anda minta
• /song [judul musik] - unduh lagu yang Anda inginkan dengan cepat
• /search [judul musik] - Cari video di youtube dengan detail

**PERINTAH UNTUK SEMUA ADMIN GRUP**
• /pause - jeda pemutaran lagu
• /resume - lanjutkan pemutaran lagu
• /skip - mainkan lagu berikutnya
• /end - hentikan pemutaran musik

**📝 CATATAN:
• Untuk Menghindari Bot Error Jangan Melakukan Spam Musik Ke Dalam Antrian Sekaligus
• Musik yang melebihi waktu 1 jam tidak dapat diputar di voice chat
• Jika Userbot Tidak Mau Naik Ke Voice Chat Akhiri Obrolan Suara Danan Mulai lagi Obrolan suara Nya
• Jika Ada Masalah Silahkan Hubungi [ɢᴏᴏᴅ ʙᴏʏs](https://t.me/GB_03101999)! Selamat Bermusik**
        """,
      reply_markup=InlineKeyboardMarkup(
            [
                [
                     InlineKeyboardButton(
                        "💬 sᴜᴘᴘᴏʀᴛ", url="https://t.me/GB_03101999"),

                    InlineKeyboardButton(
                        "ᴅᴏɴᴀsɪ 🎁", url="https://saweria.co/DonasiUntukAdmin")
                  ],[
                    InlineKeyboardButton(
                        "✅ Cari Link Youtube ✅", switch_inline_query_current_chat=""
                    )
                ]
            ]
        )
    )
