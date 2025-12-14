=========================================================

CLONIFY USERBOT (API_ID + API_HASH)

⚠️ PRIVATE USE ONLY | HIGH BAN RISK CONTENT

=========================================================

---------- INSTALL ----------

pip install -U pyrogram tgcrypto pytgcalls yt-dlp requests beautifulsoup4

import os import random import requests import yt_dlp from bs4 import BeautifulSoup from pyrogram import Client, filters from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton from pytgcalls import PyTgCalls from pytgcalls.t>

---------- CONFIG ----------

API_ID = 39496551            # 🔴 apna api_id daalo API_HASH = "36495414098630fed4555734bcc9748b"   # 🔴 apna api_hash daalo SESSION_NAME = "clonify"     # session file name DOWNLOAD_DIR = "downloads"

os.makedirs(DOWNLOAD_DIR, exist_ok=True)

---------- CLIENTS ----------

app = Client( SESSION_NAME, api_id=API_ID, api_hash=API_HASH )

pytg = PyTgCalls(app)

---------- GLOBAL ----------

QUEUE = {}

keyboard = InlineKeyboardMarkup([ [ InlineKeyboardButton("⊝ CLOSE ⊝", callback_data="close"), InlineKeyboardButton("⊝ VC PLAY ⊝", callback_data="vplay"), ] ])

---------- HELPERS ----------

def search_xnxx(title: str): try: url = f"https://www.xnxx.com/search/{title.replace(' ', '%20')}" r = requests.get(url, timeout=20) soup = BeautifulSoup(r.text, "html.parser") cards = soup.find_all("div", class_="thumb-block") if not card>

def download_video(link: str): ydl_opts = { "format": "bestvideo+bestaudio/best", "outtmpl": f"{DOWNLOAD_DIR}/%(id)s.%(ext)s", "quiet": True, "nocheckcertificate": True, } with yt_dlp.YoutubeDL(ydl_opts) as ydl: info = ydl.extract_info(lin>

---------- CALLBACKS ----------

@app.on_callback_query(filters.regex("^close$")) async def close_btn(_, q): await q.message.delete()

@app.on_callback_query(filters.regex("^vplay$")) async def vplay_btn(_, q): chat_id = q.message.chat.id

if chat_id not in QUEUE:
    return await q.answer("❌ No video queued", show_alert=True)

file_path = QUEUE[chat_id]

await pytg.join_group_call(
    chat_id,
    AudioVideoPiped(file_path)
)

await q.answer("▶️ Playing in VC")

---------- COMMANDS ----------

@app.on_message(filters.command("porn") & filters.me) async def porn_cmd(_, msg): if len(msg.command) < 2: return await msg.reply("Usage: /porn title")

title = " ".join(msg.command[1:])
link = search_xnxx(title)

if not link:
    return await msg.reply("❌ No video found")

video = download_video(link)
QUEUE[msg.chat.id] = video

await msg.reply_video(
    video,
    caption=f"🔞 {title}",
    reply_markup=keyboard
)

@app.on_message(filters.command("xnxx") & filters.me) async def xnxx_cmd(_, msg): if len(msg.command) < 2: return await msg.reply("Usage: /xnxx title")

title = " ".join(msg.command[1:])
link = search_xnxx(title)

if not link:
    return await msg.reply("❌ No result")

video = download_video(link)

await msg.reply_video(video, caption=f"🔞 {title}")

---------- START ----------

async def main(): await app.start() await pytg.start() print("✅ Clonify Userbot Started") await idle()

from pyrogram import idle

if name == "main": app.run(main())
