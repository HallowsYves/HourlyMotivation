import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
from hourly_motivation import  generate_quote, load_image, generate_motivational_prompt, get_image


# SETUP
load_dotenv()
DISCORD_KEY = os.getenv("DISCORD_KEY")
client = discord.Client(intents=discord.Intents.default())


ppromt = generate_motivational_prompt()
quote = generate_quote(f"Generate a motivational quote based on {ppromt}")
#background_img = generate_image("Beautiful Nature Background")

background_img = get_image()

# input different word  or adjetive to make the prompt different instead of it repeating
# dictionary add to it 

@client.event
async def on_ready():
    print(f'Logged in as {client.user.name} (ID: {client.user.id})')
    print('---------------')
    channel = client.get_channel(1157410144334921760)
    if channel:
        await channel.send(f'{load_image(background_img,quote)}')

client.run(DISCORD_KEY)
