from os import path

from pyrogram import Client
from pyrogram.types import Message, Voice
from pytgcalls.types.input_stream import InputAudioStream
from Client import callsmusic, queues

import converter
from youtube import youtube

from config import BOT_NAME as bn, DURATION_LIMIT, UPDATES_CHANNEL, AUD_IMG, QUE_IMG, GROUP_SUPPORT
from helpers.filters import command, other_filters
from helpers.decorators import errors
from helpers.errors import DurationLimitError
from helpers.gets import get_url, get_file_name
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(command("audio") & other_filters)
@errors
async def stream(_, message: Message):

    lel = await message.reply("🔁 𝐌𝐞𝐧𝐠𝐡𝐮𝐛𝐮𝐧𝐠𝐤𝐚𝐧 𝐤𝐞 𝐯𝐜𝐠...")
    sender_id = message.from_user.id
    sender_name = message.from_user.first_name

    keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="✨ 𝐆𝐫𝐨𝐮𝐩𝐬",
                        url=f"https://t.me/luciddreaams"),
                    InlineKeyboardButton(
                        text="🌻 𝐂𝐡𝐚𝐧𝐧𝐞𝐥",
                        url=f"https://t.me/infobotmusik"),
                ]
            ]
        )

    audio = (message.reply_to_message.audio or message.reply_to_message.voice) if message.reply_to_message else None
    url = get_url(message)

    if audio:
        if round(audio.duration / 60) > DURATION_LIMIT:
            raise DurationLimitError(
                f"❎ 𝐕𝐢𝐝𝐞𝐨 𝐥𝐞𝐛𝐢𝐡 𝐝𝐚𝐫𝐢 {DURATION_LIMIT} 𝐦𝐞𝐧𝐢𝐭(𝐬) 𝐭𝐢𝐝𝐚𝐤 𝐝𝐚𝐩𝐚𝐭 𝐝𝐢 𝐩𝐮𝐭𝐚𝐫!"
            )

        file_name = get_file_name(audio)
        file_path = await converter.convert(
            (await message.reply_to_message.download(file_name))
            if not path.isfile(path.join("downloads", file_name)) else file_name
        )
    elif url:
        file_path = await converter.convert(youtube.download(url))
    else:
        return await lel.edit_text("𝐒𝐢𝐥𝐚𝐡𝐤𝐚𝐧 𝐜𝐨𝐩𝐲 𝐩𝐚𝐬𝐭𝐞 𝐥𝐢𝐧𝐤 𝐝𝐚𝐫𝐢 𝐲𝐨𝐮𝐭𝐮𝐛𝐞 𝐦𝐮𝐬𝐢𝐤 𝐲𝐚𝐧𝐠 𝐢𝐧𝐠𝐢𝐧 𝐝𝐢 𝐦𝐚𝐢𝐧𝐤𝐚𝐧 𝐝𝐚𝐧 𝐛𝐚𝐥𝐚𝐬 𝐦𝐞𝐧𝐠𝐠𝐮𝐧𝐚𝐤𝐚𝐧 𝐩𝐞𝐫𝐢𝐧𝐭𝐚𝐡 `/audio`")

    if message.chat.id in callsmusic.pytgcalls.active_calls:
        position = await queues.put(message.chat.id, file=file_path)
        await message.reply_photo(
        photo=f"{QUE_IMG}",
        reply_markup=keyboard,
        caption=f"# 𝐋𝐚𝐠𝐮 𝐩𝐞𝐫𝐦𝐢𝐧𝐭𝐚𝐚𝐧 𝐤𝐚𝐦𝐮 𝐝𝐢𝐭𝐚𝐦𝐛𝐚𝐡𝐤𝐚𝐧 𝐤𝐞 𝐚𝐧𝐭𝐫𝐢𝐚𝐧 𝐝𝐚𝐧 𝐛𝐞𝐫𝐚𝐝𝐚 𝐝𝐢 𝐩𝐨𝐬𝐢𝐬𝐢 {position}!\n\n⚡ __𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐛𝐲 𝐒𝐭𝐞𝐫𝐞𝐨 𝐦𝐮𝐬𝐢𝐜 𝐩𝐫𝐨𝐣𝐞𝐜𝐭__")
        return await lel.delete()
    else:
        callsmusic.pytgcalls.join_group_call(message.chat.id, file_path)
        costumer = message.from_user.mention
        await message.reply_photo(
        photo=f"{AUD_IMG}",
        reply_markup=keyboard,
        caption=f"🎧 **𝐒𝐞𝐝𝐚𝐧𝐠 𝐦𝐞𝐦𝐮𝐭𝐚𝐫 𝐥𝐚𝐠𝐮 𝐚𝐭𝐚𝐬 𝐩𝐞𝐫𝐦𝐢𝐧𝐭𝐚𝐚𝐧** {costumer}!\n\n⚡ __𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐛𝐲 𝐒𝐭𝐞𝐫𝐞𝐨 𝐦𝐮𝐬𝐢𝐜 𝐩𝐫𝐨𝐣𝐞𝐜𝐭__"
        )
        return await lel.delete()
