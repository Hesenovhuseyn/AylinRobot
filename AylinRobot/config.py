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
   BOT_TOKEN = os.getenv("BOT_TOKEN", "6272485125:AAFlfnMAtPd8GXLVfa95gKS4yZt6ThTO8rE")
   BOT_USERNAME = os.environ.get("BOT_USERNAME", "dddd")
   BOT_NAME = os.environ.get("BOT_NAME", "Fatime")   
   OWNER_ID = int(os.environ.get("OWNER_ID","6799203666"))
   OWNER_NAME = os.environ.get("OWNER_NAME", "huseynh") 
   GONDERME_TURU = bool(os.environ.get("GONDERME_TURU", "False"))
   MONGODB_URI = os.environ.get("MONGODB_URI", "mongodb+srv://Huseyn:Huseyn@cluster0.zelpu0o.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
   LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002209683682"))
   PLAYLIST_NAME = os.environ.get("PLAYLIST_NAME", "fffff")
   PLAYLIST_ID = int(os.environ.get("PLAYLIST_ID", "-1002209683682"))
   BAN_GROUP = int(os.environ.get("BAN_GROUP", "-1002209683682"))
   HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", "05a017d5-e3e5-424d-941f-3e60645e3141")
   ALIVE_NAME = os.environ.get("ALIVE_NAME", "HUSEYN")
   CHANNEL = os.environ.get("CHANNEL", "huseynh")
   SUPPORT = os.environ.get("SUPPORT", "huseynh")
   ALIVE_IMG = os.environ.get("ALIVE_IMG", "https://telegra.ph/file/f6c186e3c581a223856c4.mp4") 
   START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/b2c2ed59a89933a384ae3.jpg")
   COMMAND_PREFIXES = list(os.environ.get("COMMAND_PREFIXES", "/ ! .").split())
