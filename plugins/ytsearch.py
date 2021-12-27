import json
import logging


from helpers.filters import command
from pyrogram import Client
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
)
from youtube_search import YoutubeSearch

logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

import pyrogram

logging.getLogger("pyrogram").setLevel(logging.WARNING)


@Client.on_message(command(["search", f"yt"]))
async def ytsearch(_, message: Message):
    
    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "🗑 Close", callback_data="close",
                )
            ]
        ]
    )
    
    try:
        if len(message.command) < 2:
            await message.reply_text("/search needs an argument!")
            return
        query = message.text.split(None, 1)[1]
        m = await message.reply_text("Searching....")
        results = YoutubeSearch(query, max_results=5).to_dict()
        text = ""
        for i in range(5):
            text += f"🏷 𝐍𝐚𝐦𝐚 : `{results[i]['title']}`\n"
            text += f"⏱️ 𝐃𝐮𝐫𝐚𝐬𝐢 : `{results[i]['duration']}`\n"
            text += f"👀 𝐕𝐢𝐞𝐰𝐬 : `{results[i]['views']}`\n"
            text += f"🛡 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 : `{results[i]['channel']}`\n"
            text += f"✨ 𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐛𝐲 : [𝙎𝙩𝙚𝙧𝙚𝙤 𝙈𝙪𝙨𝙞𝙘 𝙋𝙧𝙤𝙟𝙚𝙘𝙩](https://t.me/infobotmusik)\n"
            text += f"https://youtube.com{results[i]['url_suffix']}\n\n"
        await m.edit(text, disable_web_page_preview=True)
    except Exception as e:
        await message.reply_text(str(e))
