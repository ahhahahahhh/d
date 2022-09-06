import asyncio

from helpers.filters import command
from config import BOT_NAME as bn, BOT_USERNAME as bu, SUPPORT_GROUP, OWNER_USERNAME as me, START_IMG
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(command("/start") & filters.private & ~filters.group & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"{START_IMG}",
        caption=f"""**━───⊶⛧•[- ᴹᵁᔆᴵᶜ ᴰᴬᵂᔆ⁴ᴬ♪·º♫ ](https://t.me/Daws4a)•⛧⊷───━**\n

🎻¦**انا بوت تشغيل وتنزيل الاغاني والفديو**\n

 👮🏼‍♂️¦**اضفني مشرف في مجموعتك لأعمل**\n

 🌐¦**اتبع مايلي لمعرفه كيفيه الاستخدام**\n

 ❓¦**اضغط علي ذر طريقه الاستخدام**\n

 ◍**مميزات الروبوت يعمل بجودة فائقه**\n

**━───⊶⛧•[- ᴹᵁᔆᴵᶜ ᴰᴬᵂᔆ⁴ᴬ♪·º♫ ](https://t.me/Daws4a)•⛧⊷───━**\n""",
    reply_markup=InlineKeyboardMarkup(
             [
            [
                InlineKeyboardButton("أضف لبوت لمجموعتك ✅", url=f"https://t.me/{bu}?startgroup=true"),
            ],
            [
            InlineKeyboardButton( "🔎 كيف تستخدمني؟ قائمة الأوامر.",url=f"https://t.me/Daws4A/19177"),
            ],
            [
            InlineKeyboardButton("𝙳𝙴𝚅𝙴𝙻𝙾𝙿𝙴𝚁 ", url=f"https://t.me/Daws4A_1"),
              ],
              [
                  InlineKeyboardButton(
                         " ☣️ ¦ جـروب الدعم ", url=f"https://t.me/{SUPPORT_GROUP}"
                ),
            ],
            [
                InlineKeyboardButton("𝚂𝙾𝚄𝚁𝙲𝙴 ", url=f"https://t.me/Daws4a"),
            ]
         ]
     )
  )

@Client.on_message(
    command(["مبرمج السورس","دوشه"])
    & filters.group
    & ~filters.edited
)
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://t.me/jsjjssjsjw/11",
        caption=f"""المـبرمـج دوشــه مـبرمج جـميع الـسورس لو حاابـب تتـواصل مـعاه 🫡""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "D𝗘𝗩𝗘𝗟𝗢𝗣𝗘𝗗 ", url=f"https://t.me/Daws4A_1"),
                ],
                [
                    InlineKeyboardButton(
                    "S𝗢𝗨𝗥𝗖𝗘 ", url=f"https://t.me/Daws4a"
                ),
            ],
            [
                InlineKeyboardButton("أضف لبوت لمجموعتك ✅", url=f"https://t.me/{bu}?startgroup=true"),
            ]
         ]
     )
  )

@Client.on_message(command(["مطور السورس" ,"Daws4A","سورس","السورس بويكا"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://t.me/jsjjssjsjw/11",
        caption=f""" المـبرمـج دوشــه مـبرمج جـميع الـسورس لو حاابـب تتـواصل مـعاه 🫡 """,
        reply_markup=InlineKeyboardMarkup(
         [
            [
                InlineKeyboardButton("D𝗘𝗩𝗘𝗟𝗢𝗣𝗘𝗗 ", url=f"https://t.me/Daws4A_1"),
           ],
            [ 
                InlineKeyboardButton(
                    "S𝗢𝗨𝗥𝗖𝗘 ", url=f"https://t.me/Daws4a"
                ),
            ],
            [
                InlineKeyboardButton("أضف لبوت لمجموعتك ✅", url=f"https://t.me/{bu}?startgroup=true"),
            ]
         ]
     )
  )

@Client.on_message(command(["سورس","ياسورس","السورس","source","يا سورس"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_video(
        video=f"https://t.me/jsjjssjsjw/11",
        caption=f"""[━═━═━ٰ˚₊·Daws4a.↺═━═━•](https://t.me/Daws4a)
 [✨╎𝚆𝙴𝙻𝙲𝙾𝙼𝙴 𝚃𝙾 𝚂𝙾𝚄𝚁𝙲𝙴 Daws4a](https://t.me/Daws4A_1)

 [⚙╎𝚃𝙷𝙴 𝙱𝙴𝚂𝚃 𝚂𝙾𝚄𝚁𝙲𝙴 𝙾𝙽 𝙴𝙶𝚈𝙿𝚃](https://t.me/Daws4A_1)
 
 [⚡╎𝚁𝚄𝙽 𝚈𝙾𝚄𝚁 𝙱𝙾𝚃 𝚆𝙸𝚃𝙷 𝚄𝚂 𝙽𝙾𝚆](https://t.me/Daws4A_1)
[━═━═━ٰ˚₊·Daws4a.↺═━═━•](https://t.me/Daws4A_1)
──┈┈┈┄┄╌╌╌╌┄┄┈┈┈
[◍ 𝐶𝐻"✈َٰS𝗢𝗨𝗥𝗖𝗘 .↺ ◍](https://t.me/Daws4A)
[━═━═━═━ٰ═━═━═━•](https://t.me/S6222_50)""",
        reply_markup=InlineKeyboardMarkup(
         [
            [
                InlineKeyboardButton("D𝗘𝗩𝗘𝗟𝗢𝗣𝗘𝗗 ", url=f"https://t.me/Daws4A_1"),
            ],
            [
            InlineKeyboardButton(" َِ𝘾 َِ𝙃 ", url=f"https://t.me/Daws4A"),
            ],
            [
                InlineKeyboardButton(
                        "S𝗢𝗨𝗥𝗖𝗘 ", url=f"https://t.me/Daws4A"
                ),
            ],
            [
                InlineKeyboardButton("أضف لبوت لمجموعتك ✅", url=f"https://t.me/{bu}?startgroup=true"),
            ]
         ]
     )
  )


@Client.on_message(filters.new_chat_members)
async def new_chat(c: Client, m: Message):
    chat_id = m.chat.id
    if await is_served_chat(chat_id):
        pass
    else:
        await add_served_chat(chat_id)
    ass_uname = (await user.get_me()).username
    bot_id = (await c.get_me()).id
    for member in m.new_chat_members:
        if member.id == bot_id:
            return await m.reply(
                " **شكرا لإضافتي إلى مجموعتك لتشغيل الموسيقي!**\n\n"
                " **قم بترقيتي مسؤول في المجموعة لكي أتمكن من العمل بشكل صحيح\nولا تنسى كتابة `/انضم` لدعوة الحساب المساعد\nقم بكتابة`/تحديث` لتحديث قائمة المشرفين",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("⚙️ ¦ السورس ", url=f"https://t.me/{UPDATES_CHANNEL}"),
                            ],
                            [
                            InlineKeyboardButton("☣️ ¦ جـروب الدعم", url=f"https://t.me/{GROUP_SUPPORT}")
                        ],
                        [
                            InlineKeyboardButton(
                        ALIVE_NAME, url=f"https://t.me/{ass_uname}"),
                        ],
                        [
                            InlineKeyboardButton(
                        "أضف لبوت لمجموعتك ✅", url=f'https://t.me/{bu}?startgroup=true'),
                        ],
                    ]
                )
            )


chat_watcher_group = 5
