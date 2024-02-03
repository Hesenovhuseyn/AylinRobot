## Sahib HuseynH Satış Qadağandır

import logging, asyncio, random
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.types import ChannelParticipantsAdmins
from AylinRobot.config import Config
from Telethon.Mesajlar import soz,  emoji, bayrag

logging.basicConfig(
    level=logging.INFO,
    format='%(name)s - [%(levelname)s] - %(message)s'
)
LOGGER = logging.getLogger(__name__)
 
api_id = Config.API_ID
api_hash = Config.API_HASH
bot_token = Config.BOT_TOKEN

client = TelegramClient('client', api_id, api_hash).start(bot_token=bot_token)


anlik_calisan = []
 
ozel_list = [2074934667]
anlik_calisan = []
grup_sayi = []
etiketuye = []
rxyzdev_tagTot = {}
rxyzdev_initT = {}
	
@client.on(events.NewMessage(pattern='^.cancel ?(.*)'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)
  
  if event.chat_id in rxyzdev_tagTot:await event.respond(f"✅**Tağ Prosesi Dayandırıldı.**\n\n📊 **Tağ Edilənərin Sayı:** `{rxyzdev_tagTot[event.chat_id]}`")
 

@client.on(events.NewMessage(pattern='^.dayan ?(.*)'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)
  
  if event.chat_id in rxyzdev_tagTot:await event.respond(f"✅**Tağ Prosesi Dayandırıldı.**\n\n📊 **Tağ Edilənərin Sayı:** `{rxyzdev_tagTot[event.chat_id]}`")
 
	
@client.on(events.NewMessage(pattern="^.tag ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  rxyzdev_tagTot[event.chat_id] = 0
  if event.is_private:
    return await event.respond("**❌ PM Də Tağ Olmaz**\n**✅ Bu Əmr Sadəcə Qruplarda Və Kanallarda Keçərlidi!**")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**⛔ Siz Admin Deyilsiz!**\n✅ Bu Əmir Sadəcə Adminlər Üçün Keçərlidi**")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("**🔗 Keçmiş Mesajlar Üçün Userlərdən Bəhs Edə Bilmərəm❗**")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("**📌 Tağ Edə Bilməyim Üçün Mənə Mətin Ver**")
  else:
    return await event.respond("**❌ Tağ Edmək Üçün Bir Səbəb Yoxdur\n✅ Tağ Edə Bilməyim Üçün Səbəb Yazın\nℹ `/tag Salam`**")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    await event.respond(f"**✅ Tağ Prosesi Başladıldı!**")
        
    async for usr in client.iter_participants(event.chat_id, aggressive=False):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"\n• - [{usr.first_name}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"{msg}\n{usrtxt}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"**✅ Tağ Prosesi Uğurla Tamamlandı !.\n\n📊 Tağ Edilənlərin Sayı: {rxyzdev_tagTot[event.chat_id]}\n\n👤 Prosesi Başladan: {rxyzdev_initT}**")
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id, aggressive=False):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"\n• - [{usr.first_name}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
     
    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"      
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"**✅ Tağ Prosesi Uğurla Tamamlandı !.\n\n📊 Tağ Edilənlərin Sayı: {rxyzdev_tagTot[event.chat_id]}\n\n👤 Prosesi Başladan: {rxyzdev_initT}**")


@client.on(events.NewMessage(pattern="^.ttag ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  rxyzdev_tagTot[event.chat_id] = 0
  if event.is_private:
    return await event.respond("*❌ PM Də Tağ Olmaz**\n**✅ Bu Əmr Sadəcə Qruplarda Və Kanallarda Keçərlidi!**")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("** ⛔ Siz Admin Deyilsiz!**\n✅ Bu Əmir Sadəcə Adminlər Üçün Keçərlidi**")
 
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("***🔗 Keçmiş Mesajlar Üçün Userlərdən Bəhs Edə Bilmərəm❗**")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("**📌 Tağ Edə Bilməyim Üçün Mənə Mətin Ver!**")
  else:
    return await event.respond("**❌ Tağ Edmək Üçün Bir Səbəb Yoxdur\n✅ Tağ Edə Bilməyim Üçün Səbəb Yazın\nℹ `/ttag Salam`**")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    await event.respond(f"**✅ Tağ Prosesi Uğurla Başladıldl.!**")
        
    async for usr in client.iter_participants(event.chat_id, aggressive=False):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"\n📢 - [{usr.first_name}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, f"{msg}\n{usrtxt}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"**✅ Tağ Prosesi Uğurla Tamamlandı !.\n\n📊 Tağ Edilənlərin Sayı: {rxyzdev_tagTot[event.chat_id]}\n\n👤 Prosesi Başladan: {rxyzdev_initT}**")
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id, aggressive=False):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"\n📢 - [{usr.first_name}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
     
    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"      
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"**✅ Tağ Prosesi Uğurla Tamamlandı !.\n\n📊 Tağ Edilənlərin Sayı: {rxyzdev_tagTot[event.chat_id]}\n\n👤 Prosesi Başladan: {rxyzdev_initT}**")
 
 
 
@client.on(events.NewMessage(pattern="^.stag ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  rxyzdev_tagTot[event.chat_id] = 0
  if event.is_private:
    return await event.respond("*❌ PM Də Tağ Olmaz**\n✅ Bu Əmr Sadəcə Qruplar Və Kanllar Üçün Keçərlidir.")
  
  admins = []
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("⛔ **Siz Admin Deyilsiz!**\n✅ **Bu Əmir Sadəcə Adminlər Üçün Keçərlidi**")
 
  if event.pattern_match.group(0):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(0)
  elif event.reply_to_msg_id:
    mode = ""
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("ℹ **Köhnə Mesajlar Üçün Userlərdən Bəhs Edə Bilmərəm**")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("Bana bir metin verin.")
  else:
    return await event.respond("**Bir Mesajı Yanıtlayın Yada Tağ Edə Bilməyim Üçün Bir Səbəb Yazın\n✔ Misal Üçün:-`/etag Salam`**")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    await event.respond("**✅ Tağ Prosesi Başladıldı**")
        
    async for usr in client.iter_participants(event.chat_id, aggressive=False):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"\n• - [{random.choice(soz)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, f"{usrtxt}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"**✅  Tağ Prosesi Uğurla Tamamlandı**\n\n**📊 Tağ Edilınlərin Sayı:-**  `{rxyzdev_tagTot[event.chat_id]}`\n**👤 Prosesi Başladan:-** {rxyzdev_initT}")
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id, aggressive=False):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"\n• - [{random.choice(soz)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
     
    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"      
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"**✅ Tağ Prosesi Uğurla tamamlandı**\n\n**⚡ Tağ Edildi:-**  `{rxyzdev_tagTot[event.chat_id]}`\n**🗣 Prosesi Başladan:-**  {rxyzdev_initT}")
 
 
@client.on(events.NewMessage(pattern='^.cancel ?(.*)'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)
  
  if event.chat_id in rxyzdev_tagTot:await event.respond(f"✅**Tağ Prosesi Dayandırıldı.**\n\n📋 **Tağ Edilənərin Sayı:** `{rxyzdev_tagTot[event.chat_id]}`")
 
 
@client.on(events.NewMessage(pattern="^.etag ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  rxyzdev_tagTot[event.chat_id] = 0
  if event.is_private:
    return await event.respond("**❌ PM Də Tağ Olmaz**\n**✅ Bu Əmr Sadəcə Qruplarda Və Kanallarda Keçərlidi!**")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**⛔ Siz Admin Deyilsiz!**\n✅ Bu Əmir Sadəcə Adminlər Üçün Keçərlidi**")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("**🔗 Keçmiş Mesajlar Üçün Userlərdən Bəhs Edə Bilmərəm❗**")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("**📌 Tağ Edə Bilməyim Üçün Mənə Mətin Ver**")
  else:
    return await event.respond("**❌ Tağ Edmək Üçün Bir Səbəb Yoxdur\n✅ Tağ Edə Bilməyim Üçün Səbəb Yazın\nℹ `/etag Salam`**")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    await event.respond(f"**✅ Tağ Prosesi Başladıldı!**")
        
    async for usr in client.iter_participants(event.chat_id, aggressive=False):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"- [{random.choice(emoji)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"{msg}\n{usrtxt}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"**✅ Tağ Prosesi Uğurla Tamamlandı !.\n\n📊 Tağ Edilənlərin Sayı: {rxyzdev_tagTot[event.chat_id]}\n\n👤 Prosesi Başladan: {rxyzdev_initT}**")
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id, aggressive=False):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f" - [{random.choice(emoji)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
     
    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"      
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"**✅ Tağ Prosesi Uğurla Tamamlandı !.\n\n📊 Tağ Edilənlərin Sayı: {rxyzdev_tagTot[event.chat_id]}\n\n👤 Prosesi Başladan: {rxyzdev_initT}**")
  
@client.on(events.NewMessage(pattern='^.cancel ?(.*)'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)
  
  if event.chat_id in rxyzdev_tagTot:await event.respond(f"✅**Tağ Prosesi Dayandırıldı.**\n\n📊 **Tağ Edilənərin Sayı:** `{rxyzdev_tagTot[event.chat_id]}`**")
 


@client.on(events.NewMessage(pattern="^.rtag ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  rxyzdev_tagTot[event.chat_id] = 0
  if event.is_private:
    return await event.respond("**❌ PM Də Tağ Olmaz**\n**✅ Bu Əmr Sadəcə Qruplarda Və Kanallarda Keçərlidi!**")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**⛔ Siz Admin Deyilsiz!**\n✅ Bu Əmir Sadəcə Adminlər Üçün Keçərlidi**")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("**🔗 Keçmiş Mesajlar Üçün Userlərdən Bəhs Edə Bilmərəm❗**")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("**📌 Tağ Edə Bilməyim Üçün Mənə Mətin Ver**")
  else:
    return await event.respond("**❌ Tağ Edmək Üçün Bir Səbəb Yoxdur\n✅ Tağ Edə Bilməyim Üçün Səbəb Yazın\nℹ `/rtag Salam`**")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    await event.respond(f"**✅ Tağ Prosesi Başladıldı!**")
        
    async for usr in client.iter_participants(event.chat_id, aggressive=False):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"\n•- [{random.choice(seher)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"{msg}\n{usrtxt}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"**✅ Tağ Prosesi Uğurla Tamamlandı !.\n\n📊 Tağ Edilənlərin Sayı: {rxyzdev_tagTot[event.chat_id]}\n\n👤 Prosesi Başladan: {rxyzdev_initT}**")
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id, aggressive=False):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"\n•- [{random.choice(seher)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
     
    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"      
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"**✅ Tağ Prosesi Uğurla Tamamlandı !.\n\n📊 Tağ Edilənlərin Sayı: {rxyzdev_tagTot[event.chat_id]}\n\n👤 Prosesi Başladan: {rxyzdev_initT}**")
  
@client.on(events.NewMessage(pattern='^.cancel ?(.*)'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)
  
  if event.chat_id in rxyzdev_tagTot:await event.respond(f"✅**Tağ Prosesi Dayandırıldı.**\n\n📊 **Tağ Edilənərin Sayı:** `{rxyzdev_tagTot[event.chat_id]}`**")
 
 

@client.on(events.NewMessage(pattern="^.btag ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  rxyzdev_tagTot[event.chat_id] = 0
  if event.is_private:
    return await event.respond("**❌ PM Də Tağ Olmaz**\n**✅ Bu Əmr Sadəcə Qruplarda Və Kanallarda Keçərlidi!**")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**⛔ Siz Admin Deyilsiz!**\n✅ Bu Əmir Sadəcə Adminlər Üçün Keçərlidi**")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("**🔗 Keçmiş Mesajlar Üçün Userlərdən Bəhs Edə Bilmərəm❗**")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("**📌 Tağ Edə Bilməyim Üçün Mənə Mətin Ver**")
  else:
    return await event.respond("**❌ Tağ Edmək Üçün Bir Səbəb Yoxdur\n✅ Tağ Edə Bilməyim Üçün Səbəb Yazın\nℹ `/btag Salam`**")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    await event.respond(f"**✅ Tağ Prosesi Başladıldı!**")
        
    async for usr in client.iter_participants(event.chat_id, aggressive=False):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"- [{random.choice(bayrag)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"{msg}\n{usrtxt}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"**✅ Tağ Prosesi Uğurla Tamamlandı !.\n\n📊 Tağ Edilənlərin Sayı: {rxyzdev_tagTot[event.chat_id]}\n\n👤 Prosesi Başladan: {rxyzdev_initT}**")
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id, aggressive=False):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f" - [{random.choice(bayrag)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
     
    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"      
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"**✅ Tağ Prosesi Uğurla Tamamlandı !.\n\n📊 Tağ Edilənlərin Sayı: {rxyzdev_tagTot[event.chat_id]}\n\n👤 Prosesi Başladan: {rxyzdev_initT}**")
  
@client.on(events.NewMessage(pattern='^.cancel ?(.*)'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)
  
  if event.chat_id in rxyzdev_tagTot:await event.respond(f"✅**Tağ Prosesi Dayandırıldı.**\n\n📊 **Tağ Edilənərin Sayı:** `{rxyzdev_tagTot[event.chat_id]}`**")
 
		


@client.on(events.NewMessage(pattern="^.admin ?(.*)"))
async def tag_admin(event):
    chat = await event.get_input_chat()
    text = "♕︎ Qrup Adminlərinin Siyahısı ♕︎\n\n"
    async for x in event.client.iter_participants(chat, 100, filter=ChannelParticipantsAdmins):
        text += f" \n ➪ [{x.first_name}](tg://user?id={x.id})"
    if event.reply_to_msg_id:
        await event.client.send_message(event.chat_id, text, reply_to=event.reply_to_msg_id)
    else:
        await event.reply(text)
    raise StopPropagation
    
    
    
    
SAHIB = Config.OWNER_ID

@client.on(events.NewMessage(pattern="^.pin ?(.*)"))
async def pin(event):
    if event.sender_id == SAHIB:
        if not event.reply_to_msg_id:
            return await event.reply("🗨 Zəhmət Olmasa Bir Mesaja Yanıt Verin")
        await event.reply("📌 Sahibim Mesajınlz Pinləndi!")
        await event.client.pin_message(event.chat_id, event.reply_to_msg_id, notify=True)
    else:
        await event.reply(f"Sən {Config.BOT_NAME} Bota Sahib Deyilsən!\n⛔ Pinləməyə Çalışma.")
 

@client.on(events.NewMessage(pattern="^.unpin ?(.*)"))
async def unpin(event):
    if event.sender_id == SAHIB:
        if not event.reply_to_msg_id:
            return await event.reply("🗨 Zəhmət Olmasa Pinlənmiş Mesaja Yanıt Verin")
        await event.reply("Sahibim Pinlənmiş Mesaj Qaldırıldı")
        await event.client.unpin_message(event.chat_id)
    else:
        await event.reply(f"Sən {Config.BOT_NAME} Bota Sahib Deyilsən!\n⛔ UnPinləməyə Çalışma.")    
        





@client.on(events.ChatAction)
async def handler(event):
    if event.user_joined:
        await event.reply(random.choice(userjoin))


@client.on(events.ChatAction)
async def handler(event):
    if event.user_left:
        await event.reply("Əla Birdə gəlmə")

userjoin = (

    "Xoş Gəldoin",
    "Xoş Gəldin Gözəl İnsan", 
    "Sənin Gəlişin Məni Sevindirdi", 
    "Aramıza Xoş Gəldin",
    "Partimizə Xoş Gəldin",
    "Bayaqdan Səni Gözləyirəm",
    "Xoşgəldin, Pizza gətirəcəyivi düşnürdük.",
    "Xoşgəldin, Çıxacagsansa indidən çıx 😒.",
)




@client.on(events.NewMessage(pattern=f'@{Config.OWNER_NAME}'))
@client.on(events.NewMessage(pattern='Huseyn'))
@client.on(events.NewMessage(pattern='@Hesenov_H'))
@client.on(events.NewMessage(pattern='Husi'))
async def handler(event):
    await event.reply(random.choice(Aylin))



Aylin = (
    "😒 Az tağ elə sahibimi",
    "🤭 Hmm Mənim Sahibimlə Nə İşin Var?",
    "😖 Ged Yat",
    "🚷 Ban Olundun !\nSəbəb: Sahibimi tağ etdiyinçün \nŞaka ya korkma 😂",
    "Burda olmasada qəlbi sizinlədi ❤️",
)
