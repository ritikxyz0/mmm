CLONIFY USERBOT - CLEAN VERSION (NO EMOJI, NO VC)

PRIVATE USE ONLY

from pyrogram import Client, filters from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton import requests import yt_dlp from bs4 import BeautifulSoup import os

===== CONFIG =====

API_ID = 39496551  # <-- apna API_ID daalo API_HASH = "36495414098630fed4555734bcc9748b"  # <-- apna API_HASH daalo SESSION_NAME = "sex"

app = Client(SESSION_NAME, api_id=API_ID, api_hash=API_HASH)

===== HELPERS =====

def search_xnxx(query): url = f"https://www.xnxx.com/search/{query.replace(' ', '%20')}" r = requests.get(url, timeout=15) soup = BeautifulSoup(r.text, "html.parser") a = soup.select_one("div.mozaique a") if not a: return None return "https://www.xnxx.com" + a.get("href")

def download_video(url, out="video.mp4"): ydl_opts = { "outtmpl": out, "format": "best[ext=mp4]/best", "quiet": True, } with yt_dlp.YoutubeDL(ydl_opts) as ydl: ydl.download([url])

===== COMMANDS =====

@app.on_message(filters.command("xnxx") & filters.me) async def xnxx_cmd(_, m): if len(m.command) < 2: await m.edit("Usage: /xnxx <keyword>") return q = " ".join(m.command[1:]) await m.edit("Searching...") link = search_xnxx(q) if not link: await m.edit("No result found") return await m.edit("Downloading...") fname = "video.mp4" if os.path.exists(fname): os.remove(fname) download_video(link, fname) await m.reply_video(fname, caption=q) os.remove(fname) await m.delete()

@app.on_message(filters.command("porn") & filters.me) async def porn_cmd(, m): # same as xnxx for simplicity await xnxx_cmd(, m)

app.run()
