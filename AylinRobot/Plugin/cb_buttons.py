# @AylinRobot
# Sahib @HuseynH
# Repo Açığdısa İcazəsis Götürmə Oğlum


import os
from AylinRobot.translation import Translation
from AylinRobot.Plugin import Button
from AylinRobot.config import Config
from pyrogram import Client
from pyrogram.errors import UserNotParticipant
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from AylinRobot import AylinRobot as app


@app.on_callback_query()
async def cb_data(client, message):
    if message.data == "home":
        await message.message.edit_text(
            text=Translation.START_TEXT.format(message.from_user.mention, Config.BOT_USERNAME, Config.OWNER_NAME, Config.BOT_NAME),
            reply_markup=Button.START_BUTTONS,
            disable_web_page_preview=True,
        )
    elif message.data == "bh":
        await message.message.edit_text(
            text=Translation.BH_TEXT.format(message.from_user.mention, Config.BOT_USERNAME, Config.OWNER_NAME, Config.BOT_NAME),
            reply_markup=Button.BH_BUTTONS,
            disable_web_page_preview=True
        )
    elif message.data == "help":
        await message.message.edit_text(
            text=Translation.HELP_TEXT.format(message.from_user.mention, Config.BOT_USERNAME, Config.OWNER_NAME, Config.BOT_NAME),
            reply_markup=Button.HELP_BUTTONS,
            disable_web_page_preview=True
        )
    elif message.data == "musıc":
        await message.message.edit_text(
            text=Translation.MUSIC_TEXT,
            reply_markup=Button.MUSIC_BUTTONS,
            disable_web_page_preview=True
        )
    elif message.data == "tg":
        await message.message.edit_text(
            text=Translation.TELEGRAPH_TEXT,
            reply_markup=Button.TELEGRAPH_BUTTONS,
            disable_web_page_preview=True
        ) 
    elif message.data == "eylence":
        await message.message.edit_text(
            text=Translation.EYLENCE_TEXT,
            reply_markup=Button.EYLENCE_BUTTONS,
            disable_web_page_preview=True
        )        
    elif message.data == "sehıd":
        await message.message.edit_text(
            text=Translation.SEHID_TEXT,
            reply_markup=Button.SEHID_BUTTONS,
            disable_web_page_preview=True
        ) 
    elif message.data == "oyun":
        await message.message.edit_text(
            text=Translation.OYUN_TEXT,
            reply_markup=Button.OYUN_BUTTONS,
            disable_web_page_preview=True
        )        
    elif message.data == "elave":
        await message.message.edit_text(
            text=Translation.ELAVELER_TEXT,
            reply_markup=Button.ELAVE_BUTTONS,
            disable_web_page_preview=True
        )   
    elif message.data == "axtar":
        await message.message.edit_text(
            text=Translation.AXTARIS_TEXT,
            reply_markup=Button.AXTAR_BUTTONS,
            disable_web_page_preview=True
        )   
    elif message.data == "tag":
        await message.message.edit_text(
            text=Translation.TAGGER_TEXT,
            reply_markup=Button.TAGGER_BUTTONS,
            disable_web_page_preview=True
        )                
    else:
        await message.message.delete()
        