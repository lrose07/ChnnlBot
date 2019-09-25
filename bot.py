import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()


@client.event
async def on_ready():
    print(client.guilds[0].name)
    for guild in client.guilds:
        if guild.name == GUILD:
            pass


@client.event
async def on_message(message):
    if message.content[0] == "?":
        print(f'{message.channel}')
        if "makechannel" in message.content:
            contents = message.content.split(" ")
            await process_request(contents)
            for item in contents:
                print(item)


def process_request(list):
    guild = client.guilds[0]
    print("name: ", guild.name)
    print(list[1])
    guild.create_text_channel(list[1])


client.run(TOKEN)