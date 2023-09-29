import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
from hourly_motivation import generate_image, generate_quote, load_image


# SETUP
load_dotenv()
DISCORD_KEY = os.getenv("DISCORD_KEY")
client = discord.Client(intents=discord.Intents.default())


quote = generate_quote("Generate a motivational quote, without quoting anyone from history.")
background_img = generate_image("Beautiful Nature Background")



@client.event
async def on_ready():
    print(f'Logged in as {client.user.name} (ID: {client.user.id})')
    print('---------------')
    channel = client.get_channel(1157410144334921760)
    if channel:
        await channel.send(f'{load_image(background_img,quote)}')

client.run(DISCORD_KEY)
