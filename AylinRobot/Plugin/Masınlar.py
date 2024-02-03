# @AylinRobot
# Sahib @HuseynH
# Repo Açığdısa İcazəsis Götürmə Oğlum
# Mamana Salam De 
import time
from time import time
import random
from random import choice
from pyrogram.types import Message
from AylinRobot import AylinRobot as app
from pyrogram import Client, filters
from AylinRobot.config import Config


photolist = ["https://te.legra.ph/file/abd505920b3b17aa96f28.jpg","https://te.legra.ph/file/3018cd6ff3ff220e9194e.jpg","https://te.legra.ph/file/d4dc67f19d41e1a5fdf90.jpg","https://te.legra.ph/file/a09236872222817119f60.jpg","https://te.legra.ph/file/28b030831cf75466b897f.jpg","https://te.legra.ph/file/19fa2d6632afb4bfebbb0.jpg","https://te.legra.ph/file/279d49cfaf6cbefce2ee9.jpg","https://te.legra.ph/file/b605c184a4afc84d46b9f.jpg","https://te.legra.ph/file/b07b69df189e80d4fb126.jpg","https://te.legra.ph/file/e7f49de2f7a0250ac31e7.jpg","https://te.legra.ph/file/46ff0c1b950bcbea00b1b.jpg","https://te.legra.ph/file/322198be38e841ae17d59.jpg","https://te.legra.ph/file/bf037363e0fb3b72b5eaf.jpg","https://te.legra.ph/file/0573c6a82fe2c7fc4671b.jpg","https://te.legra.ph/file/c82b90b28522c5f2f0d7a.jpg","https://te.legra.ph/file/2f5210a94d22bd277de3d.jpg","https://te.legra.ph/file/9cb99cb18622ec76f10b8.jpg","https://te.legra.ph/file/8671138e14d05dee81e7e.jpg","https://te.legra.ph/file/79cc99304afcc8806e05e.jpg","https://te.legra.ph/file/ec8c4645bb6604db5c994.jpg","https://te.legra.ph/file/fbe861995cb1282a08c4c.jpg","https://te.legra.ph/file/528c592598de90f99f719.jpg","https://te.legra.ph/file/957f575c3a24eb78de421.jpg","https://te.legra.ph/file/99d219cf6fba9010f9797.jpg","https://te.legra.ph/file/9a695bb9c7366119400a4.jpg","https://te.legra.ph/file/5fd62acdab6e7812fe4f3.jpg","https://te.legra.ph/file/9dc0cd5816c1e19385ea9.jpg","https://te.legra.ph/file/829e55df693005a955b57.jpg","https://te.legra.ph/file/df62287a6dde82d8538af.jpg","https://te.legra.ph/file/38044d80ae964dfc56c13.jpg","https://te.legra.ph/file/dbb28fae6166f7d2443cf.jpg","https://te.legra.ph/file/7a0cee3ce2eabb2377fd9.jpg","https://te.legra.ph/file/7bba66025c5e625e01c39.jpg","https://te.legra.ph/file/20944e170d088692b67bc.jpg","https://te.legra.ph/file/38e2f3b4a7eda5913095c.jpg","https://te.legra.ph/file/490d5b22c3f3d27ce1431.jpg","https://te.legra.ph/file/73a5de8573957e7873b81.jpg","https://te.legra.ph/file/ef82de0e8e59d8dc8e4cd.jpg","https://te.legra.ph/file/8e6c97a03732cb62de6f3.jpg","https://te.legra.ph/file/e6bd0027e83d3e1f8648c.jpg","https://te.legra.ph/file/0122c184a94bbf20c7d47.jpg","https://te.legra.ph/file/618b825168df960a618cd.jpg","https://telegra.ph/file/c2917a95346f456337391.jpg","https://telegra.ph/file/1825416a9179c4cb1110c.jpg","https://telegra.ph/file/83d06af361076573a663a.jpg","https://telegra.ph/file/6704c2ac2a6044d0c492a.jpg","https://telegra.ph/file/fa150f09af04ff768104a.jpg","https://telegra.ph/file/ac45fd5d1689b433278ad.jpg","https://telegra.ph/file/47be02880efe89f887bf7.jpg","https://telegra.ph/file/b1b60cc1f98ecd2f4bdd2.jpg","https://telegra.ph/file/1b6fd33469593fc7f06b0.jpg","https://telegra.ph/file/d7b9aab0416a5eabcdba1.jpg","https://telegra.ph/file/cad22263cfd0b3e5205a2.jpg","https://telegra.ph/file/37970db08a628e457392d.jpg","https://telegra.ph/file/2d32b870c290d48938244.jpg","https://telegra.ph/file/9ce5da0e27b233ca6bd21.jpg","https://telegra.ph/file/67bfe67fe14c790013ccd.jpg","https://telegra.ph/file/3e408fd85d7152e84c9b9.jpg","https://telegra.ph/file/fe074033a0cc596b166a9.jpg","https://telegra.ph/file/1f2c10914ab52ab8ce5d7.jpg","https://telegra.ph/file/0fc6bcc9a42381eaf88e7.jpg","https://telegra.ph/file/953df8b0a617b8a3222a6.jpg","https://telegra.ph/file/a4bea31bbf22f9ba053aa.jpg","https://telegra.ph/file/6c30b0d5d54b47db1db06.jpg","https://telegra.ph/file/8147e743d7f11e95c8582.jpg","https://telegra.ph/file/4e05687447e39ac83145b.jpg","https://telegra.ph/file/7e11dc724ea55f6f2ec56.jpg","https://telegra.ph/file/5470e53b7da78b77341e0.jpg","https://telegra.ph/file/33b3956547542927ef545.jpg","https://telegra.ph/file/4d3d51ed5699742f6f659.jpg","https://telegra.ph/file/4e345fef38d52bb2747b6.jpg","https://telegra.ph/file/5a69e9bb7cb590219f98c.jpg","https://telegra.ph/file/a721995123569bd8d571a.jpg","https://telegra.ph/file/4f209647a8ea1eb41c76e.jpg","https://telegra.ph/file/97cfe65d94d268588094c.jpg","https://telegra.ph/file/53113f5d1ec7206639d9f.jpg","https://telegra.ph/file/5817865cc19f0c994a66f.jpg","https://telegra.ph/file/f3c561b488a42d2d8adca.jpg","https://telegra.ph/file/708943581d8044c8f1a0c.jpg","https://telegra.ph/file/8fc613a538f08d5cf6be7.jpg","https://telegra.ph/file/372159a7160fdd06ce5bd.jpg","https://telegra.ph/file/26178c6ff74f83ed8e386.jpg","https://telegra.ph/file/afc73d2cb1c7bd50f441a.jpg","https://telegra.ph/file/b0e8304e14a565574da92.jpg","https://telegra.ph/file/1f7700a0afb7d6bf98856.jpg","https://telegra.ph/file/7fddcfd1bad654498980f.jpg","https://telegra.ph/file/10b9829110f814935bc34.jpg","https://telegra.ph/file/1350436a035f15cd10d8b.jpg","https://telegra.ph/file/288b9d13020ed104d6435.jpg"]



videolist = ["https://te.legra.ph/file/7c9892f18201efb39ff6a.mp4","https://te.legra.ph/file/b5340b9c1e6afb70e33b7.mp4","https://te.legra.ph/file/80604fecab9479ba086af.mp4","https://te.legra.ph/file/91e54b9e647b32017c4e6.mp4","https://te.legra.ph/file/ff6eecd8f11b172ef2099.mp4","https://te.legra.ph/file/0bf2b591c657bed225a29.mp4","https://te.legra.ph/file/875d1d69269abb1f4b2e2.mp4","https://te.legra.ph/file/c643aa58fb8cb18f55878.mp4","https://te.legra.ph/file/2bd4d8a8742fcedc9db8c.mp4","https://te.legra.ph/file/67eb47d9804f2ce9fb193.mp4","https://te.legra.ph/file/b231918cb8cfa655026b4.mp4","https://te.legra.ph/file/0796ddbb1d989aa7a88e3.mp4","https://te.legra.ph/file/6fd365494294937ae473e.mp4","https://te.legra.ph/file/7bff3368892504cd8967f.mp4","https://te.legra.ph/file/d97f64716c664a08243e6.mp4","https://te.legra.ph/file/3a04fc5bac35d4ec313e7.mp4","https://te.legra.ph/file/d24f126020cc49f97e580.mp4","https://te.legra.ph/file/5f0b2be3f96e952ee576d.mp4","https://te.legra.ph/file/11eef49944e033be32e09.mp4","https://te.legra.ph/file/b21cbe0b6610529503cf1.mp4","https://te.legra.ph/file/25481f0412b0532313c9a.mp4","https://te.legra.ph/file/1c67075297f2869c15a66.mp4","https://te.legra.ph/file/aec86a0165ea3dfef0c62.mp4","https://te.legra.ph/file/1c9894f8a36b9d15b873c.mp4","https://te.legra.ph/file/3c00d56c8393394771ff6.mp4","https://te.legra.ph/file/017517df1045cdae90ec4.mp4","https://te.legra.ph/file/0b10fa75246c3fa5cf43c.mp4","https://te.legra.ph/file/4e40d2e958fceaac189a6.mp4","https://te.legra.ph/file/3b2395f9f7dcd179f6007.mp4"]


@app.on_message(filters.command("masın"))
async def test_bot(bot: app, m: Message):
    start = time()
    replymsg = await m.reply_text("**❤ Rondom Bir Maşın Şəkili Seçilir...**")
    end = round(time() - start, 2)
    photo = random.choice(photolist)
    text = f"❤️ **{Config.BOT_USERNAME} Sizin Üçün Rondom Maşın Şəkili Seçdi**"
    await bot.send_photo(m.chat.id, photo=photo, caption=text)
    await replymsg.delete()
    
    
@app.on_message(filters.command("masın2"))
async def test_app(app: app, m: Message):
    start = time()
    replymsg = await m.reply_text("**❤ Rondom Maşın Videosu Seçilir...**")
    end = round(time() - start, 2)
    video = random.choice(videolist)
    text = f"❤️ **{Config.BOT_USERNAME} Sizin Üçün Rondom Maşın Videosu Seçdi**"
    await app.send_video(m.chat.id, video=video, caption=text)
    await replymsg.delete()    