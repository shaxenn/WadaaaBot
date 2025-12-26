import discord
from discord.ext import commands
import random
import requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!w ", intents=intents)

GIPHY_API_KEY = ""


@bot.event
async def on_ready():
    print(f"Aktif: {bot.user}")


@bot.command()
async def gif(ctx, *, tur: str):
    url = "https://api.giphy.com/v1/gifs/search"

    params = {"api_key": GIPHY_API_KEY, "q": tur, "limit": 25, "rating": "pg"}

    response = requests.get(url, params=params)
    data = response.json()

    if not data["data"]:
        await ctx.send("Bu türde GIF bulamadım 😢")
        return

    gif = random.choice(data["data"])
    gif_url = gif["images"]["original"]["url"]

    await ctx.send(gif_url)


bot.run(
    "DISCORD_TOKEN")
