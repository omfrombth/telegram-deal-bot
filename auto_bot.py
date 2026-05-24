from telethon import TelegramClient, events
from telegram import Bot
import re
import asyncio

# =========================
# TELEGRAM API
# =========================

API_ID = 35571564
API_HASH = "957f6327bae6d5a7821e6ca165415245"

BOT_TOKEN = "8714219900:AAF6g5aPqhlrkarEnEa044hKwegNNqxP3Sfs"

# =========================
# CHANNEL SETTINGS
# =========================

TARGET_CHANNEL = "lootdealsindia22"

SOURCE_CHANNELS = [
    "https://t.me/+FpXKV70NYNY0NzQ1"
]

AFFILIATE_TAG = "lootdealsi067-21"

# =========================

bot = Bot(token=BOT_TOKEN)

client = TelegramClient(
    "session",
    API_ID,
    API_HASH
)

# Replace Amazon links
def replace_amazon_links(text):

    links = re.findall(r'https?://amzn\.to/\S+', text)

    for link in links:

        if "tag=" not in link:
            new_link = f"{link}?tag={AFFILIATE_TAG}"
            text = text.replace(link, new_link)

    return text

# Listen new posts
@client.on(events.NewMessage(chats=SOURCE_CHANNELS))
async def handler(event):

    try:

        text = event.raw_text

        if not text:
            return

        new_text = replace_amazon_links(text)

        await bot.send_message(
            chat_id=f"@{TARGET_CHANNEL}",
            text=new_text
        )

        print("Posted Successfully")

    except Exception as e:
        print("Error:", e)

async def main():

    print("Bot Started")

    await client.start()

    await client.run_until_disconnected()

asyncio.run(main())
