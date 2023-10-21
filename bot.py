import os
import discord
from dotenv import load_dotenv
from discord.ext import commands, tasks
from hourly_motivation import  generate_quote, load_image, generate_motivational_prompt, get_image
import asyncio


# SETUP
load_dotenv()
DISCORD_KEY = os.getenv("DISCORD_KEY")

intents = discord.Intents.default()
intents.typing = False
intents.presences = False


bot = commands.Bot(command_prefix='!', intents=intents)

@tasks.loop(hours=1)
async def hourly_message():
    channel = bot.get_channel(1157410144334921760)
    if channel:
        quote = generate_quote(f"Generate a motivational quote based on {generate_motivational_prompt()}")
        background_img = get_image()
        await channel.send(f'{load_image(background_img,quote)}')


@bot.event
async def on_ready():
    hourly_message.start()

bot.run(DISCORD_KEY)