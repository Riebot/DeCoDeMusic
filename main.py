import requests
from Client.callsmusic import run
from config import API_HASH, API_ID, BG_IMAGE, BOT_TOKEN
from pyrogram import Client as Bot
from pytgcalls import idle

response = requests.get(BG_IMAGE)
with open("./etc/foreground.png", "wb") as file:
    file.write(response.content)


bot = Bot(
    ":memory:", API_ID, API_HASH, bot_token=BOT_TOKEN, plugins=dict(root="plugins")
)

bot.start()
run()
idle()
