import os
import discord
from dotenv import load_dotenv
from discord.ext import commands

# SETUP
load_dotenv()
DISCORD_KEY = os.getenv("DISCORD_KEY")
bot = discord.Client(intents=discord.Intents.default())
 

@bot.event
async def on_ready():
    print("READY")

@bot.event
async def on_message(message):
    await message.channel.send("Hello, world!")
bot.run(DISCORD_KEY)

## POSTPONED