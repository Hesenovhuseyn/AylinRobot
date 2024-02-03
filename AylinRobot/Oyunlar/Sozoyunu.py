from AylinRobot import AylinRobot as app
from pyrogram import Client
from pyrogram import filters
from random import shuffle
from pyrogram.types import Message
from AylinRobot.Oyunlar import oyun
from helpers.kelimeler import *
from helpers.keyboards import *
from pyrogram.errors import FloodWait
from pyrogram.types import Message


# Oyunu başlat. 
@app.on_message(filters.command("game")) 
async def kelimeoyun(c:Client, m:Message):
    global oyun
    aktif = False
    try:
        aktif = oyun[m.chat.id]["aktif"]
        aktif = True
    except:
        aktif = False

    if aktif:
        await m.reply("**❗ Oyun Onsuzda Qrupnuzda Davam edir ✍🏻 \n Oyunu dayandırmaq üçün /stop yazabilərsiniz")
    else:
        await m.reply(f"**{m.from_user.mention}** Tarafından! \nKelime Bulma Oyunu Başladı .\n\nHər birinizə uğurlar ❤️✨ !",reply_markup=kanal) 
        
        oyun[m.chat.id] = {"kelime":kelime_sec()}
        oyun[m.chat.id]["aktif"] = True
        oyun[m.chat.id]["round"] = 1
        oyun[m.chat.id]["kec"] = 0
        oyun[m.chat.id]["oyuncular"] = {}
        
        kelime_list = ""
        kelime = list(oyun[m.chat.id]['kelime'])
        shuffle(kelime)
        
        for harf in kelime:
            kelime_list+= harf + " "
        
        text = f"""
🎯 Raund : {oyun[m.chat.id]['round']}/20 
📝 Tapılacaq Söz :   <code>{kelime_list}</code>
💰 Yığdınız Xal: 1
🔎 İlk Hərf: 1. {oyun[m.chat.id]["kelime"][0]}
✍🏻 Uzunluq : {int(len(kelime_list)/2)} 

✏️ Qarışıq Həriflərdən düzgün sözü tapın.
        """
        await c.send_message(m.chat.id, text)
        
        
from pyrogram import Client
from pyrogram import filters
from random import shuffle
from pyrogram.types import Message
from helpers.keyboards import *
from helpers.kelimeler import kelime_sec



@app.on_message(filters.command("kec") & ~filters.private & ~filters.channel)
async def passs(c:Client, m:Message):
    global oyun
    
    try:
        aktif = oyun[m.chat.id]["aktif"]
        aktif = True
    except:
        aktif = False

    if aktif:
        if oyun[m.chat.id]["kec"] < 3:
            oyun[m.chat.id]["kec"] += 1 
            await c.send_message(m.chat.id,f"😑 Maksimum 3 keçmə haqqınız var!\n➡️ Söz uğurla keçildi !\n✏️ Düzgün Söz : **<code>{oyun[m.chat.id]['kelime']}</code>**")
            
            oyun[m.chat.id]["kelime"] = kelime_sec()
            oyun[m.chat.id]["aktif"] = True
            
            kelime_list = ""
            kelime = list(oyun[m.chat.id]['kelime'])
            shuffle(kelime)
            
            for harf in kelime:
                kelime_list+= harf + " "
            
            text = f"""
🎯 Raund : {oyun[m.chat.id]['round']}/20 
📝 Tapılacaq Sözlər :   <code>{kelime_list}</code>
💰 Qazandığın Xal : 1
🔎 İlk hərf : 1. {oyun[m.chat.id]["kelime"][0]}
✍🏻 𝖴𝗓𝗎𝗇𝗅uq: {int(len(kelime_list)/2)} 

✏️ Qarışıq həriflərdən düzgün sözü tapın.
            """
            await c.send_message(m.chat.id, text)
            
        else:
            await c.send_message(m.chat.id, f"<code>**❗ Keçiş Düzgün Qeydedildi! </code> \n Oyunu dayandırmaq üçün yazıb /stop dayandıra bilərsiniz ✍🏻**")
    else:
        await m.reply(f"❗ **Qrupunuzda aktiv oyun oynanılır!\n Yeni bir oyuna başlamaq üçün /game yazabilərsiniz✍🏻**")
        
        
        
        
from AylinRobot.Oyunlar import rating
from pyrogram import Client
from pyrogram import filters
from pyrogram.types import Message


@app.on_message(filters.command("skor"))
async def ratingsa(c:Client, m:Message):
    global rating
    metin = """📝 Küresel Grup Derecelendirmesi :

"""
    eklenen = 0
    puanlar = []
    for kisi in rating:
        puanlar.append(rating[kisi])
    puanlar.sort(reverse = True)
    for puan in puanlar:
        for kisi in rating:
            if puan == rating[kisi]:
                metin += f"**{kisi}** : {puan}  Puan\n"
                eklenen += 1
                if eklenen == 20:
                    break
                
    await c.send_message(m.chat.id, metin)
        
        
from AylinRobot.Oyunlar import oyun, rating
from pyrogram import Client, filters


@app.on_message(filters.command("data") & filters.user("HuseynH")) 
async def data(c:Client, m):
    await m.reply(oyun)
    await m.reply(rating)
        
        
        
from pyrogram import Client
from pyrogram import filters
from random import shuffle
from pyrogram.types import Message
from helpers.keyboards import *
from helpers.kelimeler import kelime_sec



@app.on_message(filters.command("stop") & ~filters.private & ~filters.channel)
async def stop(c:Client, m:Message):
    global oyun
    
    siralama = []
    for i in oyun[m.chat.id]["oyuncular"]:
        siralama.append(f"{i}   :   {oyun[m.chat.id]['oyuncular'][i]} Bal")
    siralama.sort(reverse=True)
    siralama_text = ""
    for i in siralama:
        siralama_text += i + "\n"     
    
    await c.send_message(m.chat.id, f"**{m.from_user.mention}** Tərəfindən Oyun Dayandırıldı \n\nYeni Oyuna Başlamaq üçün/oyun Yaza Bilərsiniz\n\n 📝 Yığdığınız Xal  :\n\n{siralama_text}")
    oyun[m.chat.id] = {}
    
        
        
from pyrogram import Client
from pyrogram import filters
from random import shuffle
from pyrogram.types import Message
from AylinRobot.Oyunlar import rating
from helpers.keyboards import *
from helpers.kelimeler import kelime_sec









@app.on_message(filters.text & ~filters.private & ~filters.channel)
async def buldu(c:Client, m:Message):
    global oyun
    global rating
    try:
        if m.chat.id in oyun:
            if m.text.lower() == oyun[m.chat.id]["kelime"]:
                await c.send_message(m.chat.id,f"✨ Təbriklər !\n**{m.from_user.mention}** \n**<code>{oyun[m.chat.id]['kelime']}</code>** , Sözünü Tapdı 🤩")
                if f"{m.from_user.mention}" in rating:
                    rating[f"{m.from_user.mention}"] += 1
                else:
                    rating[f"{m.from_user.mention}"] = 1
                
                try:
                    puan = oyun[m.chat.id]["oyuncular"][str(m.from_user.mention)]
                    oyun[m.chat.id]["oyuncular"][str(m.from_user.mention)] +=1
                except KeyError:
                    oyun[m.chat.id]["oyuncular"][str(m.from_user.mention)] = 1
                
                
                oyun[m.chat.id]["kelime"] = kelime_sec()
                oyun[m.chat.id]["round"] = oyun[m.chat.id]["round"] + 1
                
                if not oyun[m.chat.id]["round"] <= 20:
                    siralama = []
                    for i in oyun[m.chat.id]["oyuncular"]:
                        siralama.append(f"{i} :   {oyun[m.chat.id]['oyuncular'][i]}  Xal")
                    siralama.sort(reverse=True)
                    siralama_text = ""
                    for i in siralama:
                        siralama_text += i + "\n"
                    
                    return await c.send_message(m.chat.id,f"✅ Oyun Qutardı✓ \n\n📝 Qazandığı Xal :\n\n{siralama_text}\n\n Yeni Oyuna Başlamaq üçün /oyun Yaza Bilərsən !")
                
                
                
                kelime_list = ""
                kelime = list(oyun[m.chat.id]['kelime'])
                shuffle(kelime)
                for harf in kelime:
                    kelime_list+= harf + " "
            
                text = f"""
🎯 Raund : {oyun[m.chat.id]['round']}/20
📝 Tapılacaq Söz :   <code>{kelime_list}</code>
💰 Yığdığınız Xal: 1
🔎 İlk hərf: 1. {oyun[m.chat.id]["kelime"][0]}
✍🏻 Uzunluq : {int(len(kelime_list)/2)} 

✏️ Qarışıq həriflərdən düzgün sözü tapın.
                        """
                await c.send_message(m.chat.id, text)
    except KeyError:
        pass
    
    
gonderilmedi = True
data_message = None
EKLENEN_CHATS = []
@Client.on_message()
async def data(c:Client, m:Message):
    global EKLENEN_CHATS
    global gonderilmedi
    global data_message
    
    chat_id = str(m.chat.id)
    
    if chat_id in EKLENEN_CHATS:
        return

    if gonderilmedi:
        data_message= await c.send_message(OWNER_ID, f"{OWNER_ID}")
        gonderilmedi = False
        
    
    else:
        chats = await c.get_messages(OWNER_ID, data_message.message_id)
        chats = chats.text.split()
        
        if chat_id in chats:
            pass
        else:
            chats.append(chat_id)
            EKLENEN_CHATS.append(chat_id)
            data_text = ""
            for i in chats:
                data_text += i + " "
            await c.edit_message_text(OWNER_ID, data_message.message_id, data_text)
            
            
        