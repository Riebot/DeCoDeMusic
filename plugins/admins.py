from asyncio.queues import QueueEmpty
from config import que
from pyrogram import Client, filters
from pyrogram.types import Message
import sira
import DeCalls
from cache.admins import set
from helpers.decorators import authorized_users_only, errors
from helpers.channelmusic import get_chat_id
from helpers.filters import command, other_filters
from Client import callsmusic
from pytgcalls.types.input_stream import InputAudioStream


@Client.on_message(command(["pause", "jeda"]) & other_filters)
@errors
@authorized_users_only
async def pause(_, message: Message):
    callsmusic.pytgcalls.pause_stream(message.chat.id)
    await message.reply_photo(
                             photo="https://telegra.ph/file/e6443c3ba9f2cc48f5fa3.jpg", 
                             caption="**⏸ 𝐌𝐮𝐬𝐢𝐜 𝐛𝐞𝐫𝐡𝐞𝐧𝐭𝐢 𝐬𝐞𝐦𝐞𝐧𝐭𝐚𝐫𝐚**"
    )


@Client.on_message(command(["resume", "lanjut"]) & other_filters)
@errors
@authorized_users_only
async def resume(_, message: Message):
    callsmusic.pytgcalls.resume_stream(message.chat.id)
    await message.reply_photo(
                             photo="https://telegra.ph/file/126ebe97a5f318a67e24a.jpg", 
                             caption="**▶️ 𝐌𝐮𝐬𝐢𝐜 𝐝𝐢𝐥𝐚𝐧𝐣𝐮𝐭𝐤𝐚𝐧 **"
    )


@Client.on_message(command(["end", "stop"]) & other_filters)
@errors
@authorized_users_only
async def stop(_, message: Message):
    try:
        callsmusic.queues.clear(message.chat.id)
    except QueueEmpty:
        pass

    callsmusic.pytgcalls.leave_group_call(message.chat.id)
    await message.reply_photo(
                             photo="https://telegra.ph/file/ca39c6b4904288d69a6d9.jpg", 
                             caption="⏹ **𝐌𝐮𝐬𝐢𝐜 𝐭𝐞𝐥𝐚𝐡 𝐝𝐢𝐦𝐚𝐭𝐢𝐤𝐚𝐧**"
    )


@Client.on_message(command(["skip", "next"]) & other_filters)
@errors
@authorized_users_only
async def skip(_, message: Message):
    global que
    chat_id = get_chat_id(message.chat)
    if chat_id not in callsmusic.pytgcalls.active_calls:
        await message.reply_text("❎ 𝐓𝐢𝐝𝐚𝐤 𝐚𝐝𝐚 𝐥𝐚𝐠𝐮 𝐲𝐚𝐧𝐠 𝐝𝐢 𝐬𝐤𝐢𝐩!")
    else:
        callsmusic.queues.task_done(chat_id)

        if callsmusic.queues.is_empty(chat_id):
            callsmusic.pytgcalls.leave_group_call(chat_id)
        else:
            callsmusic.pytgcalls.change_stream(
                chat_id, callsmusic.queues.get(chat_id)["file"]
            )

    qeue = que.get(chat_id)
    if qeue:
        skip = qeue.pop(0)
    if not qeue:
        return
    await message.reply_photo(
                             photo="https://telegra.ph/file/96129f4d0e984d2432e55.jpg", 
                             caption="f- Skipped **{skip[0]}**\n- Now Playing **{qeue[0][0]}**"
    )


@Client.on_message(filters.command(["reload", "refresh"]))
@errors
@authorized_users_only
async def admincache(client, message: Message):
    set(
        message.chat.id,
        (
            member.user
            for member in await message.chat.get_members(filter="administrators")
        ),
    )

    await message.reply_photo(
                              photo="https://telegra.ph/file/d881ea9de7620ecc36d08.jpg",
                              caption="**Reloaded\n ✅ 𝐃𝐚𝐟𝐭𝐚𝐫 𝐚𝐝𝐦𝐢𝐧 𝐭𝐞𝐥𝐚𝐡 𝐝𝐢𝐩𝐞𝐫𝐛𝐚𝐫𝐮𝐢!**"
    )
