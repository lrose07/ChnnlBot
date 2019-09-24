import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            print(f'{guild.name}(id: {guild.id})')

@client.event
async def on_message(message):
    if message.content[0] == "?":
        print(f'{message.channel}')
        if "makechannel" in message.content:
            contents = message.content.split(" ")
            for item in contents:
                print(item)

client.run(TOKEN)