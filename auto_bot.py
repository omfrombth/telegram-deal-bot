from telegram import Bot
import asyncio
import random

TOKEN = "8714219900:AAF6g5aPqhlrkarnEa044hKWegNNqxP3Sfs"
CHANNEL = "@lootdealsindia22"

bot = Bot(token=TOKEN)

captions = [
    "🔥 Loot Deal Alert",
    "⚡ Heavy Discount",
    "💥 Limited Time Offer",
    "🛒 Amazon Best Deal",
]

hashtags = [
    "#AmazonDeals #LootDeal",
    "#BestOffer #Discount",
    "#ShoppingDeals #AmazonSale",
]

deal_links = [
    "https://amzn.to/43newb9",
]

async def auto_post():
    while True:
        link = random.choice(deal_links)
        caption = random.choice(captions)
        tags = random.choice(hashtags)

        text = f"{caption}\n\n{link}\n\n{tags}"

        await bot.send_message(
            chat_id=CHANNEL,
            text=text
        )

        print("Posted:", text)

        await asyncio.sleep(30)

asyncio.run(auto_post())
