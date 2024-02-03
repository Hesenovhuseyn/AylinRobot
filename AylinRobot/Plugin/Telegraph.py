# @AylinRobot
# Sahib @HuseynH
# Repo Açığdısa İcazəsis Götürmə Oğlum

import os, pyrogram
from telegraph import upload_file
from AylinRobot import AylinRobot as app
from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from AylinRobot.config import Config


@app.on_message(filters.command("tgm"))
async def telegraph(client, message):
    replied = message.reply_to_message
    if not replied:
        await message.reply("🤕 Dəstəklənən media faylına cavab verin")
        await message.delete()         
        return
    if not (
        (replied.photo and replied.photo.file_size <= 5242880)
        or (replied.animation and replied.animation.file_size <= 5242880)
        or (
            replied.video
            and replied.video.file_name.endswith(".mp4")
            and replied.video.file_size <= 5242880
        )
        or (
            replied.document
            and replied.document.file_name.endswith(
                (".jpg", ".jpeg", ".png", ".gif", ".mp4"),
            )
            and replied.document.file_size <= 5242880
        )
    ):
        await message.reply("😔 Dəstəklənmir!!")
        return
    download_location = await client.download_media(
        message=message.reply_to_message,
        file_name="root/downloads/",
    )
    try:
        response = upload_file(download_location)
    except Exception as document:
        await message.reply(message, text=document)
    else:
        await message.reply(f"**🌐 Budur Sizin Telegraph Linginiz**:\n\n`https://telegra.ph{response[0]}`\n\nGöndərdi 🙎‍♀️ [{Config.BOT_NAME}](https://t.me/{Config.BOT_USERNAME})**", disable_web_page_preview=False)
    finally:
        os.remove(download_location)
    