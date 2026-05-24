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
# CHANNELS
# =========================

TARGET_CHANNEL = "lootdealsindia22"

SOURCE_CHANNELS = [
    "https://t.me/+FpXKV70NYNY0NzQ1"
]

# =========================
# AFFILIATE
# =========================

AMAZON_TAG = "lootdealsi067-21"

FLIPKART_LINK = "https://fktr.in/mafta9q"

# =========================

bot = Bot(token=BOT_TOKEN)

client = TelegramClient(
    "session",
    API_ID,
    API_HASH
)

# Convert all links
def convert_links(text):

    urls = re.findall(r'https?://\S+', text)

    for url in urls:

        # Amazon
        if "amazon" in url or "amzn" in url:

            if "tag=" not in url:
                new_url = f"{url}?tag={AMAZON_TAG}"
            else:
                new_url = url

            text = text.replace(url, new_url)

        # Flipkart
        elif "flipkart" in url or "fkrt" in url:

            text = text.replace(url, FLIPKART_LINK)

    return text

# Listen messages
@client.on(events.NewMessage(chats=SOURCE_CHANNELS))
async def handler(event):

    try:

        text = event.raw_text

        if not text:
            return

        new_text = convert_links(text)

        # Stylish footer
        new_text += "\n\n🔥 Best Deal Alert\n🛒 Hurry Up"

        await bot.send_message(
            chat_id=f"@{TARGET_CHANNEL}",
            text=new_text
        )

        print("Posted Successfully")

    except Exception as e:
        print("Error:", e)

async def main():

    print("Bot Running...")

    await client.start()

    await client.run_until_disconnected()

asyncio.run(main())
