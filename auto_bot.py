from telethon import TelegramClient, events
import re

# =====================================
# TELEGRAM API DETAILS
# =====================================

API_ID = 35571564

API_HASH = "957f6327bae6d5a7821e6ca165415245"

# =====================================
# BOT TOKEN
# =====================================

BOT_TOKEN = "8714219900:AAF8qQwSiNlm_qRQc673SGLndzEEdUkGBW4"

# =====================================
# SOURCE CHANNEL
# =====================================

SOURCE_CHANNEL = "https://t.me/+FpXKV70NYNY0NzQ1"

# =====================================
# TARGET CHANNEL
# =====================================

TARGET_CHANNEL = "@lootdealsindia22"

# =====================================
# AMAZON AFFILIATE TAG
# =====================================

AMAZON_TAG = "lootdealsi067-21"

# =====================================
# FLIPKART AFFILIATE LINK
# =====================================

FLIPKART_AFFILIATE = "https://fktr.in/mafta9q"

# =====================================
# TELEGRAM CLIENT
# =====================================

client = TelegramClient(
    "bot_session",
    API_ID,
    API_HASH
)

# =====================================
# AMAZON LINK REPLACE
# =====================================

def replace_amazon_link(text):

    amazon_pattern = r'(https?://(?:www\.)?amazon\.in/[^\s]+)'

    matches = re.findall(amazon_pattern, text)

    for link in matches:

        if "tag=" not in link:

            if "?" in link:
                new_link = f"{link}&tag={AMAZON_TAG}"

            else:
                new_link = f"{link}?tag={AMAZON_TAG}"

            text = text.replace(link, new_link)

    return text

# =====================================
# FLIPKART LINK REPLACE
# =====================================

def replace_flipkart_link(text):

    flipkart_pattern = r'(https?://(?:www\.)?flipkart\.com/[^\s]+)'

    matches = re.findall(flipkart_pattern, text)

    for link in matches:

        text = text.replace(link, FLIPKART_AFFILIATE)

    return text

# =====================================
# AUTO REPOST HANDLER
# =====================================

@client.on(events.NewMessage(chats=SOURCE_CHANNEL))
async def handler(event):

    try:

        message = event.message.message

        if not message:
            return

        # Replace affiliate links
        message = replace_amazon_link(message)
        message = replace_flipkart_link(message)

        # Footer
        footer = "\n\n🔥 Best Deals Daily\n🛒 Join Now 👉 @lootdealsindia22"

        final_message = message + footer

        # If media exists
        if event.message.media:

            await client.send_file(
                TARGET_CHANNEL,
                event.message.media,
                caption=final_message
            )

        else:

            await client.send_message(
                TARGET_CHANNEL,
                final_message
            )

        print("Posted Successfully")

    except Exception as e:
        print(e)

# =====================================
# START BOT
# =====================================

async def main():

    await client.start(bot_token=BOT_TOKEN)

    print("Bot Running Successfully...")

    await client.run_until_disconnected()

client.loop.run_until_complete(main())
