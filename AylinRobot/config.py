# @AylinRobot
# Sahib @HuseynH
# Repo Açığdısa İcazəsis Götürmə Oğlum
# Reponu Satan Kodların Götürən Kimliyindən Aslı Olmayaraq Peysərdi

# @AylinRobot
# Sahib @HuseynH
# Repo Açığdısa İcazəsis Götürmə Oğlum

import os

class Config:

   API_ID = int(os.getenv("API_ID", "8953338"))
   API_HASH = os.getenv("API_HASH", "fe21f223cb02d8f7c1cbda651f553a45")
   BOT_TOKEN = os.getenv("BOT_TOKEN", "7146344348:AAHR2PHd0WbeiHkT4t-UAg7MjWJ1weN4WB8")
   BOT_USERNAME = os.environ.get("BOT_USERNAME", "Fatimem_bot")
   BOT_NAME = os.environ.get("BOT_NAME", "Fatime")   
   OWNER_ID = int(os.environ.get("OWNER_ID","7114179583"))
   OWNER_NAME = os.environ.get("OWNER_NAME", "Miri_o47") 
   BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", "False"))
   MONGODB_URI = os.environ.get("MONGODB_URI", "mongodb+srv://huseyn:huseyn@cluster0.zvhh345.mongodb.net/?retryWrites=true&w=majority")
   LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002041351237"))
   PLAYLIST_NAME = os.environ.get("PLAYLIST_NAME", "FatimeRobotPlaylist")
   PLAYLIST_ID = int(os.environ.get("PLAYLIST_ID", "-1002103466673"))
   BAN_GROUP = int(os.environ.get("BAN_GROUP", "-1002041351237"))
   HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", "05a017d5-e3e5-424d-941f-3e60645e3141")
   ALIVE_NAME = os.environ.get("ALIVE_NAME", "HUSEYN")
   CHANNEL = os.environ.get("CHANNEL", "FatimeRobotPlaylist")
   SUPPORT = os.environ.get("SUPPORT", "retroteamqurup")
   ALIVE_IMG = os.environ.get("ALIVE_IMG", "https://telegra.ph/file/f6c186e3c581a223856c4.mp4") 
   START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/b2c2ed59a89933a384ae3.jpg")
   COMMAND_PREFIXES = list(os.environ.get("COMMAND_PREFIXES", "/ ! .").split())
