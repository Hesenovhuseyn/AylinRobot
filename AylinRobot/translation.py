# @AylinRobot
#@MusicAzBot
# Sahib @HuseynH
# Repo Açığdısa İcazəsis Götürmə Oğlum

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

class Translation(object):

    START_TEXT = """
╔═════════════════
║▻ **🙋‍♀️ Salam {}**
║
║▻ 🙋‍♀️ Mənim Adım  ️️️️️️🙎‍♀️ [{}](https://t.me/{}) Mən 
║▻ 🇦🇿 Azərbaycan Dilində Çox Özəllikili 
║▻ 💌 Telegram Botuyam Bacarıqlarımı Görmək Üçün
║▻ `📚 Kömək` Buttonuna Toxun
╚═════════════════
👨‍💻 **Sahibim** ♒️ @{}

"""    
    HELP_TEXT = """
╔═════════════════
║▻ **🙋‍♀️ Salam {} 
║
║▻ 💁‍♀️ ️️️️️️ [{}](https://t.me/{})- Un  
║▻ 📚 Əmrləri  Bunlardır Aşağıdakı 
║▻ 🖲 Buttonlara Toxunaraq istədiyiniz
║▻ ✔️ Əmr Haqqında Məlumat Ala Bilərsiniz 
╚═════════════════
"""

    GSTART_TEXT = """
╔═════════════════
║▻ **🙋‍♀️ Salam {} 
║
║▻ 💁‍♀️ ️️️️️️ [{}](https://t.me/{})
║
║▻ ❤️‍🔥 {}  Qrupun Da Super İşləyir  🥳
╚═════════════════
"""



### Bot Haqqında Ümumi Məlumat

    BH_TEXT = """
╔═════════════════
║▻ **🙋‍♀️ Salam {} 
║
║▻ 🙎‍♀️ [{}](https://t.me/{}) 🇦🇿 Azərbaycan Dilində Çox Özəllikli Telegram Botudur...**
║
║▻ ✨ Bot Versiyası: v0.7.0
║▻ 🍀 Pyrogram Versiyası: 1.4.16
║▻ ✨ Python Versiyası: 3.11.1
║▻ ⚙️ Server [Heroku](https://heroku.com)
║▻ 📆 Botun İstifadəyə Verilmə Tarixi `20.11.2022` 
╚═════════════════
╔═════════════════
║▻ **⚠️ Qeyd Botun Qrupunuzda İşləməsi 
║▻ Üçün Admin Əmirlərindən Sadəcə 
║▻ 💬 Mesajları Silmə 🚫 Yetkisi Verin**
╚═════════════════
"""

    MUSIC_TEXT = """
╔═════════════════
║▻ 🔮 Istifadə: /song 
║▻ 🧩 Nümunə: /song Rei - Ah Canım Sevgilim
║▻ 📃 Açıqlama: Musiqi yükləyir.
║
║▻ 🔮 Istifadə: /video
║▻ 🧩  Nümunə:/video Rei - Ah Canım Sevgilim
║▻ 📃 Açıqlama: Video yükləyir.
║
║▻ 🔮 Istifadə: /lyrics 
║▻ 🧩 Nümunə: /lyrics Rei - Ah Canım Sevgilim
║
║▻ 📃 Açıqlama: Musiqinin sözlərini tapır.
╚═════════════════
"""

    TELEGRAPH_TEXT = """
╔═════════════════
║▻ 🔮 Istifadə: /tgm
║▻ 📃 Açıqlama: Şəkil, video və ya GIF göndərərək link ala bilərsiniz.
╚═════════════════
"""

    SEHID_TEXT = """
╔═════════════════
║▻ 🔮 Istifadə: /sehid 
║▻ 📃 Açıqlama:  Bu əmr vaistəsiylə sizə **Şəhid** adları göndərəcəm
╚═════════════════
╔═════════════════
║▻ 🥀 **Allah bütün Şəhidimizə rəhmət eləsin**
║▻ 🤲 Qazilərimizə şəfa versin 
║▻ 😔 Başın sağolsun Azərbaycan 🇦🇿
║▻ 🇦🇿 Bazada **2881** Şəhid adı mövcuddur
╚═════════════════
""" 
    OYUN_TEXT = """
╔═════════════════
║▻ 🔮 Istifadə: /zer
║▻ 📃 Açıqlama: zər atar
║
║▻ 🔮 Istifadə: /top
║▻ 📃 Açıqlama: top atar
║
║▻ 🔮 Istifadə: /bowling
║▻ 📃 Açıqlama: bowling atar
║
║▻ 🔮 Istifadə: /ox
║▻ 📃 Açıqlama: ox atar
║
║▻ 🔮 Istifadə: /jackpot
║▻ 📃 Açıqlama: jackpot atar
║
║▻ 🔮 Istifadə: /basket
║▻ 📃 Açıqlama: basket atar
╚═════════════════

╔═════════════════
║▻🆕️  SÖZ-OYUNU Nunun Əsas Əmrləri
║
║▻ 🔮 Istifadə: /game
║▻ 📃 Açıqlama: Oyunu Başladar
║
║▻ 🔮 Istifadə: /kec
║▻ 📃 Açıqlama: Çətin Sözü Keçər
║
║▻ 🔮 Istifadə: /stop
║▻ 📃 Açıqlama: Mövcud Oyunu Saxlayar
║
║▻ 🔮 Istifadə: /skor
║▻ 📃 Nümunə: Hər Bir Oyunçunun Reytinqi Göstərər
╚═════════════════
"""

    EYLENCE_TEXT = """
╔═════════════════
║▻ 🔮 Istifadə: /soxri 
║▻ 📃 Açıqlama: Rondom 16+ Şəkillər Atar.
║
║▻ 🔮 Istifadə: /pisik
║▻ 📃 Açıqlama: Rondom Pişik Şəkili Atar
║
║▻ 🔮 Istifadə: /anime
║▻ 📃 Açıqlama: Rondom Anime Şəkili Atar
║
║▻ 🔮 Istifadə: /masin
║▻ 📃 Açıqlama: Rondom Maşın Şəkili Atar
║
║▻ 🔮 Istifadə: /masin2
║▻ 📃 Açıqlama: Rondom Maşın Videosu Atar
║
║▻ 🔮 Istifadə: /tema
║▻ 📃 Açıqlama: Rondom Telegram Teması Atar
║
║▻ 🔮 Istifadə: /pp
║▻ 📃 Açıqlama: Rondom Profil Şəkili Atar
║
║▻ 🔮 Istifadə: /sevgi
║▻ 📃 Açıqlama: Hazır Sevgi Yə Aid Sözlər Atar.
║
║▻ 🔮 Istifadə: /bio
║▻ 📃 Açıqlama: Hazır Bio Nuz Üçün Sözlər Atar.
╚═════════════════
"""


    ELAVELER_TEXT = """
╔═════════════════
║▻ 🔮 Istifadə: /id
║▻ 📃 Açıqlama: İstifadəçinin ID alın.
║
║▻ 🔮 Istifadə: /info
║▻ 📃 Açıqlama: İstifadəçi haqqında məlumat verər
║
║▻ 🔮 Istifadə: /alive
║▻ 📃 Açıqlama: Botun işlək olduğunu yoxlayar.
╚═════════════════
"""


    AXTARIS_TEXT = """
╔═════════════════
║▻ 🔮 Istifadə: /github 
║▻ 🧩 Nümunə: /github HesenovHuseyn
║▻ 📃 Açıqlama: Github Axtarışı Edər.
║
║▻ 🔮 Istifadə: /search
║▻ 🧩 Nümunə: /search Rei - Ah Canım Sevgilim
║▻ 📃 Açıqlama: YouTube axtarış üçün istifadə edə bilərsiniz.
╚═════════════════
"""

    TAGGER_TEXT = """
╔═════════════════
║▻ 🔮 Istifadə: /tag
║▻ 📃  Açıqlama: [Səbəb] - 5 - Li Tağ.
║
║▻ 🔮 Istifadə: /ttag
║▻ 📃  Açıqlama: [Səbıb] - Təkli Tağ.
║
║▻ 🔮 Istifadə: /stag
║▻ 📃  Açıqlama: Maraqlı Sözlərlə Tağ.
║
║▻ 🔮 Istifadə: /etag
║▻ 📃  Açıqlama: [Səbəb] - Emoji İlə Tağ.
║
║▻ 🔮 Istifadə: /btag
║▻ 📃  Açıqlama: [Səbəb] - Bayraqlarla Tağ
║
║▻ 🔮 Istifadə: /admin
║▻ 📃 Açıqlama: Adminlərin Toplu Siyahısı
╚═════════════════
"""

    SAHIB_TEXT = """
╔═════════════════
║▻ 🔮 Istifadə: /stats
║▻ 📃 Açıqlama: Bot haqqında ümumi məlumat verər.
║
║▻ 🔮 Istifadə: /block
║▻ 📃 Açıqlama: İstifadəçini Və Ya Qrupu Bloklayar.
║
║▻ 🔮 Istifadə: /unblock
║▻ 📃 Açıqlama: Bloku Açar.
║
║▻ 🔮 Istifadə: /blocklist
║▻ 📃 Açıqlama: Blok olunanların siyahısını göstərər.
║
║▻ 🔮 Istifadə: /broadcastall
║▻ 📃 Açıqlama: Qrupa Və Şəxsiyə Yayım Edər.
║
║▻ 🔮 Istifadə: /gcast
║▻ 📃 Açıqlama: Qruplarda yayım edər.
║
║▻ 🔮 Istifadə: /broadcast_pin
║▻ 📃 Açıqlama: Qruplarda yayım edər və pinləyər.
║
║▻ 🔮 Istifadə: /dyno
║▻ 📃 Açıqlama: Heroku Dyno Miqdarını Ölçər.
║
║▻ 🔮 Istifadə: /pin
║▻ 📃 Açıqlama:  Yanıtlanan Mesajı Pinləyər.
╚═════════════════
"""

##### Broadcast Mesajları


class LAN(object):


    BILDIRIM = """**🆕 Yeni istifadəçi bota start etdi**\n\n👤 {}\n🆔 `{}`\n🔗 [{}](tg://user?id={})"""
    GRUP_BILDIRIM = """**🆕 Yeni istifdəçi bota qrupda start etdi**\n\n👤 Qrupa əlavə edən: `{}`\n🆔 Qrupa əlavə edən istifadəçi id: `{}`\n🔗 Profil linki: [{}](tg://user?id={})\nQrupun ID: {})

"""
    SAHIBIME = """
sahibimə
"""
    PRIVATE_BAN = """
Məyusam, əngəlləndiniz! Bunun bir xəta olduğunu düşünürsünüzsə {} yazın.
 """
    GROUP_BAN = """
Məyusam, qrupunuz qara siyahıya əlavə olundu! Artıq burada qala bilmərəm! Bunun bir xəta olduğunu düşünürsünüzsə {} yazın.'
"""
    NOT_ONLINE = """
aktiv deyil
"""
    BOT_BLOCKED = """
botu əngəlləyib
"""
    USER_ID_FALSE = """
istifadəçi ID yanlışdır.
"""
    BROADCAST_STARTED = """
```📥 Reklam yayımı başladı!\nBitəndə mesaj göndərəcəm
"""
    BROADCAST_STOPPED = """
```✅ Reklam yayımı uğurla tamamlandı.```\n\n**Bu qədər vaxtda tamamlandı** `{}`\n\n**Ümumi istifadəçilər:** `{}`\n\n**Ümumi göndərmə cəhdləri:** `{}`\n\n**Uğurla göndərilən:** `{}`\n\n**Ümumi xəta:** `{}`
"""
    STATS_STARTED = """
{} **Zəhmət olmasa gözləyin, bilgiləri gətirirəm!**
"""
    STATS = """
**@{} Məlumatları**\n\n**İstifadəçiləri;**\n» Ümumi: `{}`\n» Qruplar: `{}`\n» Şəxsi: `{}`\n\n**Disk İstifadəsi;**\n» Disk'in Sahəsi: `{}`\n» İstifadə Edilən: `{} ({}%)`\n» Boş Qalan: `{}`\n\n**🎛 Ən yüksək istifadə dəyərləri;**\n» CPU: `{}%`\n» RAM: `{}%`\n» Pyrogram: {}
"""
    BAN_REASON = """
Bu səbəbdən qadağan olundunuz @{} tərəfindən avtomatik olaraq yaradılmışdır."""
    NEED_USER = """
**Zəhmət olmasa istifadəçi ID'si yazın.**
"""
    BANNED_GROUP = """
🚷 **Qadağan olundu!\n\nQadağan edən:** {}\n**Qrup ID:** `{}`\n**Vaxt:** `{}`\n**Səbəb:** `{}`
"""
    AFTER_BAN_GROUP = """
**Məyusam, qrupunuz qara siyahıya əlavə edildi!\n\nSəbəb:** `{}`\n\n**Artıq burada qala bilmərəm. Bunun bir xəta olduğunu düşünürsünüzsə, dəstək qrupuna gəlin.**
"""
    GROUP_BILGILENDIRILDI = """\n\n✅ **Qrupu bilgiləndirdim və qrupdan çıxdım.**
"""
    GRUP_BILGILENDIRILEMEDI = """\n\n❌ **Qrupu məlumatlandırarkən xəta yarandı:**\n\n`{}`
"""
    USER_BANNED = """
🚷 **Qadağan olundu\n\nQadağan edən:** {}\n **İstifadəçi ID:** `{}`\n**Vaxt:** `{}`\n**Səbəb:** `{}`
"""
    AFTER_BAN_USER = """
**Məyusam, qara siyahıya əlavə edildiniz! \n\nSəbəb:** `{}`\n\n**Bundan sonra sizə xidmət etməyəcəyəm.**
"""
    KULLANICI_BILGILENDIRME = """\n\n✅ İstifadəçini məlumatlandırdım.
"""
    KULLANICI_BILGILENDIRMEME = """\n\n❌ **İstifadəçini məlumatlandırarkən xəta yarandı:**\n\n`{}`
"""
    UNBANNED_USER = """
🆓 **İstifadəçinin qadağası qaldırıldı!** \nQadağanı qaldıran: {}\n**İstifadəçi ID:** `{}`
"""
    USER_UNBAN_NOTIFY = """
🎊 Sizə gözəl bir xəbərim var! Artıq əngəliniz qaldırıldı!
"""
    BLOCKS = """
🆔 **İstifadəçi ID:** `{}`\n⏱ **Vaxt:** `{}`\n🗓 **Qadağan edildiyi tarix:** `{}`\n💬 **Səbəb:** `{}`\n\n"""
    TOTAL_BLOCK = """
🚷 **Ümumi əngəllənən:** `{}`\n\n{}
"""
