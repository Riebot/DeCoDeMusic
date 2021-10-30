import os
import requests
import aiohttp
import yt_dlp

from pyrogram import Client, filters
from youtube_search import YoutubeSearch
from helpers.errors import capture_err
from config import BOT_USERNAME


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60 ** i for i, x in enumerate(reversed(stringt.split(":"))))


@Client.on_message(filters.command(["song"]))
def song(client, message):

    user_id = message.from_user.id
    user_name = message.from_user.first_name
    rpk = "[" + user_name + "](tg://user?id=" + str(user_id) + ")"

    query = "".join(" " + str(i) for i in message.command[1:])
    print(query)
    m = message.reply("🔎 `𝐒𝐞𝐝𝐚𝐧𝐠 𝐦𝐞𝐧𝐜𝐚𝐫𝐢 𝐥𝐚𝐠𝐮...`")
    ydl_opts = {"format": "bestaudio[ext=m4a]"}
    try:
        results = YoutubeSearch(query, max_results=1).to_dict()
        link = f"https://youtube.com{results[0]['url_suffix']}"
        # print(results)
        title = results[0]["title"][:80]
        thumbnail = results[0]["thumbnails"][0]
        thumb_name = f"thumb{title}.jpg"
        thumb = requests.get(thumbnail, allow_redirects=True)
        open(thumb_name, "wb").write(thumb.content)

        duration = results[0]["duration"]
        url_suffix = results[0]["url_suffix"]
        views = results[0]["views"]

    except Exception as e:
        m.edit(
            ""❎ 𝐋𝐚𝐠𝐮 𝐭𝐢𝐝𝐚𝐤 𝐝𝐢𝐭𝐞𝐦𝐮𝐤𝐚𝐧? 𝐂𝐨𝐛𝐚 𝐜𝐚𝐫𝐢 𝐝𝐞𝐧𝐠𝐚𝐧 𝐣𝐮𝐝𝐮𝐥 𝐥𝐚𝐠𝐮 𝐲𝐚𝐧𝐠 𝐥𝐞𝐛𝐢𝐡 𝐣𝐞𝐥𝐚𝐬\n𝐂𝐨𝐧𝐭𝐨𝐡 » `/play Jentaka`\n\n𝐂𝐡𝐚𝐧𝐧𝐞𝐥 : @infobotmusik"
        )
        print(str(e))
        return
    m.edit("📥 `𝐒𝐞𝐝𝐚𝐧𝐠 𝐦𝐞𝐧𝐝𝐨𝐰𝐧𝐥𝐨𝐚𝐝 𝐥𝐚𝐠𝐮..𝐬𝐚𝐛𝐚𝐫`")
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)
        rep = f"🏷 **𝐍𝐚𝐦𝐚** : [{title[:100]}]({link})\n🎬 **𝐎𝐟𝐟𝐢𝐜𝐢𝐚𝐥** : `𝐘𝐨𝐮𝐭𝐮𝐛𝐞`\n⏱️ **𝐃𝐮𝐫𝐚𝐬𝐢** : `{duration}` `𝐌𝐞𝐧𝐢𝐭`\n👁‍🗨 **𝐕𝐢𝐞𝐰𝐬** : `{views}`\n✨ **𝐒𝐮𝐩𝐩𝐨𝐫𝐭** : @infobotmusik\n🎵 **𝐁𝐲** : @SilenceSpe4ks "
        secmul, dur, dur_arr = 1, 0, duration.split(":")
        for i in range(len(dur_arr) - 1, -1, -1):
            dur += int(dur_arr[i]) * secmul
            secmul *= 60
        message.reply_audio(
            audio_file,
            caption=rep,
            thumb=thumb_name,
            parse_mode="md",
            title=title,
            duration=dur,
        )
        m.delete()
    except Exception as e:
        m.edit("❌ Error")
        print(e)

    try:
        os.remove(audio_file)
        os.remove(thumb_name)
    except Exception as e:
        print(e)
