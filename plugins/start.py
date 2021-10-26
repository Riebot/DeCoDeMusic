from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from config import BOT_NAME as bn
from helpers.filters import other_filters2
from time import time
from datetime import datetime
from helpers.decorators import authorized_users_only
from config import BOT_USERNAME, ASSISTANT_USERNAME

START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ("week", 60 * 60 * 24 * 7),
    ("day", 60 ** 2 * 24),
    ("hour", 60 ** 2),
    ("min", 60),
    ("sec", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else "s"))
    return ", ".join(parts)


@Client.on_message(other_filters2)
async def start(_, message: Message):
        await message.reply_text(
        f"""<b>𝐇𝐚𝐥𝐨 {bn}👨🏻‍🎤
🎤 __𝗦𝗮𝘆𝗮 𝗔𝗱𝗮𝗹𝗮𝗵 𝗕𝗼𝘁 𝗠𝘂𝘀𝗶𝗰__ 🎶\n
𝗗𝗮𝗻 𝗦𝗮𝘆𝗮 𝗗𝗶 𝗞𝗲𝗹𝗼𝗹𝗮 𝗢𝗹𝗲𝗵 𝗔𝗿𝗶 𝗗𝗮𝗻 𝗦𝗮𝘆𝗮 𝗕𝗶𝘀𝗮 𝗠𝗲𝗺𝘂𝘁𝗮𝗿 𝗟𝗮𝗴𝘂 𝗗𝗶 𝗢𝗯𝗿𝗼𝗹𝗮𝗻 𝗦𝘂𝗮𝗿𝗮 𝗚𝗿𝗼𝘂𝗽 𝗔𝗻𝗱𝗮 (𝚅𝙲𝙶) !..𝗗𝗮𝗻 𝗦𝗮𝘆𝗮 𝗠𝗲𝗺𝗶𝗹𝗶𝗸𝗶 𝗙𝗶𝘁𝘂𝗿 𝗦𝗲𝗽𝗲𝗿𝘁𝗶 :
• 𝗠𝗲𝗻𝗰𝗮𝗿𝗶 𝗗𝗮𝗻 𝗠𝗲𝗺𝘂𝘁𝗮𝗿 𝗟𝗮𝗴𝘂 𝗬𝗮𝗻𝗴 𝗞𝗮𝗺𝘂 𝗜𝗻𝗴𝗶𝗻𝗸𝗮𝗻.
• 𝗠𝗲𝗻𝗱𝗼𝘄𝗻𝗹𝗼𝗮𝗱 𝗟𝗮𝗴𝘂 𝗬𝗮𝗻𝗴 𝗜𝗻𝗴𝗶𝗻 𝗞𝗮𝗺𝘂 𝗗𝗼𝘄𝗻𝗹𝗼𝗮𝗱,𝗗𝗮𝗻
• 𝗠𝗲𝗻𝗱𝗼𝗻𝗮𝘀𝗶 𝗞𝗮𝗻 𝗞𝗲 𝗢𝘄𝗻𝗲𝗿 𝗕𝗼𝘁 𝗦𝗲 𝗜𝗸𝗵𝗹𝗮𝘀 𝗻𝘆𝗮,𝗝𝗶𝗸𝗮 𝗞𝗮𝗺𝘂 𝗞𝗲𝗹𝗲𝗯𝗶𝗵𝗮𝗻 𝗨𝗮𝗻𝗴.
🌹 __𝐒𝐩𝐞𝐜𝐢𝐚𝐥 𝐓𝐡𝐚𝐧𝐤𝐬 𝐓𝐨__ : 𝗣𝗮𝘁𝗿𝗶𝗰𝗶𝗮 𝗫 𝗔𝗿𝗶 🌹

👑 __𝐎𝐰𝐧𝐞𝐫__ : [𝐚𝐫𝐢](https://t.me/SilenceSpe4ks)


""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✨ 𝐆𝐫𝐨𝐮𝐩𝐬", url="https://t.me/luciddreaams")
                  ],[
                    InlineKeyboardButton(
                       " 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 ✨", url="https://t.me/infobotmusik")
                ],[
                    InlineKeyboardButton(
                        "➕ 𝐀𝐝𝐝 𝐌𝐞 𝐓𝐨 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩➕",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
         ),
      
     disable_web_page_preview=True
    )
