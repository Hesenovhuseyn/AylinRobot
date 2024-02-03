# @AylinRobot
# Sahib @HuseynH
# Repo Açığdısa İcazəsis Götürmə Oğlum
# Mamana Salam De 

import random
from random import choice
from pyrogram.errors import FloodWait
from pyrogram.types import Message
from AylinRobot import AylinRobot as app
from pyrogram import Client, filters
from AylinRobot.config import Config



temalar = [" [Fidan](https://t.me/addtheme/sf158WSw7LWOtpvV) ",
" [Fidan](https://t.me/addtheme/bpcrFtP4qYu0DdnJ) " ,
" [Fidan](https://t.me/addtheme/aUFKCX7AQ3aQpDjp) " ,
" [Fidan](https://t.me/addtheme/L7HVQjC4UUyOfL9y) " ,
" [Fidan](https://t.me/addtheme/Qd4eBWTIOH4Ai3Zv) " ,
" [Fidan](https://t.me/addtheme/NightWolf) " ,
" [Fidan](https://t.me/addtheme/GreenBlack) " ,
" [Fidan](https://t.me/addtheme/TvldPzYmpG8LqkY3) " ,
" [Fidan](https://t.me/addtheme/Q4GuvNPpMvG59G6V) " ,
" [Fidan](https://t.me/addtheme/kGQaW0HHsjc7oFOv) " ,
" [Fidan](https://t.me/addtheme/z3E6vkceX0pfmo5P) " ,
" [Fidan](https://t.me/addtheme/poMW3amfnwUwOefI) " ,
" [Fidan](https://t.me/addtheme/l1felAbEVNQCN3NW) " ,
" [Fidan](https://t.me/addtheme/y6xMaSuBOmuGekHj) " ,
" [Fidan](https://t.me/addtheme/Fp6h6JpzXrWnjF9y) " ,
" [Fidan](https://t.me/addtheme/Purple_Grapes) " ,
" [Fidan](https://t.me/addtheme/xQNP1Jp2aklmldNx) " ,
" [Fidan](https://t.me/addtheme/ry0AgHsISs439fxi) " ,
" [Fidan](https://t.me/addtheme/ZHl93FYO9ja7hN81) " ,
" [Fidan](https://t.me/addtheme/gc2MlPyKHMBjw5WS) " ,
" [Fidan](https://t.me/addtheme/ciNZt5N6QCFjsrQI) " ,
" [Fidan](https://t.me/addtheme/bEKOF0v8XuLAFZ6P) " ,
" [Fidan](https://t.me/addtheme/IOSTelegramThemes2020_11july) " ,
" [Fidan](https://t.me/addtheme/DarkPink_1) " ,
" [Fidan](https://t.me/addtheme/Halloween_04) " ,
" [Fidan](https://t.me/addtheme/BlackBlue_ByYamila) " ,
" [Fidan](https://t.me/addtheme/NewYorkNyVK) " ,
" [Fidan](https://t.me/addtheme/blackcircles_ByYamila) " ,
" [Fidan](https://t.me/addtheme/KINGByVK) " ,
" [Fidan](https://t.me/addtheme/MRPERFECTBYVK) " ,
" [Fidan](https://t.me/addtheme/ChanchiNeonByVK) " ,
" [Fidan](https://t.me/addtheme/SamurayByVK) " ,
" [Fidan](https://t.me/addtheme/NeonRocks_ByYamila) " ,
" [Fidan](https://t.me/addtheme/StichOhanaByVK) " ,
" [Fidan](https://t.me/addtheme/SkullDarkByVK) " ,
" [Fidan](https://t.me/addtheme/RedGirlByVK) " ,
" [Fidan](https://t.me/addtheme/SpidermanByVK) " ,
" [Fidan](https://t.me/addtheme/CuteMelodyByVK) " ,
" [Fidan](https://t.me/addtheme/YouAreBeautifulStichByVK) " ,
" [Fidan](https://t.me/addtheme/ManchesterUnitedByVK) "]



@app.on_message(filters.command("tema"))
async def tema(app: Client, msg: Message):
    await msg.reply(random.choice(temalar))