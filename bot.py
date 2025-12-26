import discord
from discord.ext import commands
import requests
import random

# ===== AYARLAR =====
DISCORD_TOKEN = "BOT_TOKEN"
GIPHY_API_KEY = "GIPHY_API_KEY"
PREFIX = "!w"

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=PREFIX, intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} Active!")

@bot.command()
async def gif(ctx, *, gif_turu: str):
    url = "https://api.giphy.com/v1/gifs/search"
    params = {
        "api_key": GIPHY_API_KEY,
        "q": gif_turu,
        "limit": 25,
        "rating": "pg"
    }

    response = requests.get(url, params=params)
    data = response.json()

    if not data["data"]:
        await ctx.send("❌ Bu türde gif bulamadım.")
        return

    secilen_gif = random.choice(data["data"])
    gif_url = secilen_gif["images"]["original"]["url"]

    await ctx.send(gif_url)

bot.run(DISCORD_TOKEN)
