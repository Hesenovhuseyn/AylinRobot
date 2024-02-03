# @AylinRobot
# Sahib @HuseynH
# Repo Açığdısa İcazəsis Götürmə Oğlum

import time
from AylinRobot import AylinRobot as app
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, Message
from AylinRobot.config import Config
from datetime import datetime
from os import path
from time import time
from pyrogram.errors import FloodWait
from sys import version_info
from helpers import __version__
from pyrogram import __version__ as pyrover
__major__ = 0
__minor__ = 2
__micro__ = 1

__python_version__ = f"{version_info[0]}.{version_info[1]}.{version_info[2]}"


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ("week", 60 * 60 * 24 * 7),
    ("day", 60 * 60 * 24),
    ("hour", 60 * 60),
    ("min", 60),
    ("sec", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else "s"))
    return ", ".join(parts)


@app.on_message(filters.command(["alive"]) & filters.group)
async def Alive(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.delete()   
    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("📢 Kanal", url=f"https://t.me/{Config.CHANNEL}"),
                InlineKeyboardButton(
                    "🎧 Playlist Kanalı", url=f"https://t.me/{Config.PLAYLIST_NAME}"
                ),
            ]
        ]
    )

    alive = f"**Haycan❤️ {message.from_user.mention()}, Mənim Adım {Config.BOT_USERNAME}**\n\n✨ Mən Super İşləyirəm\n🍀 Sahibim: [{Config.ALIVE_NAME}](https://t.me/{Config.OWNER_NAME})\n✨ Bot Versiyası: `v{__version__}`\n🍀 Pyrogram Versiyası: `{pyrover}`\n✨ Python Versiyası: `{__python_version__}`\n🍀 İş vaxtı Status: `{uptime}`\n\n**Məni Qrupunuza əlavə etdiyiniz üçün təşəkkürlər ** ❤"

    await message.reply_video(
        video=f"{Config.ALIVE_IMG}",
        caption=alive,
        reply_markup=keyboard,
    )