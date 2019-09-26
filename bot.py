import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
CATEGORY = os.getenv('CATEGORY')

client = discord.Client()


@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            pass


@client.event
async def on_message(message):
    for guild in client.guilds:
        if guild.name == GUILD:
            categories = guild.categories

            for cat in categories:
                if CATEGORY in cat.name:
                    print("yes, it's here")
                    found_category = cat
                    if message.content[0] == "?":
                        if "makechannel" in message.content:
                            contents = message.content.split(" ")

                            overwrites = {
                                guild.default_role: discord.PermissionOverwrite(read_messages=False),
                                guild.me: discord.PermissionOverwrite(read_messages=True)
                            }

                            new_channel = await guild.create_text_channel(
                                name=contents[1],
                                category=found_category,
                                overwrites=overwrites)

                            await new_channel.send("Welcome to your private channel!")

                            # if new channel in list of channels, confirm message in bot-commands
                else:
                    print("not here")
            for item in categories:
                print(item)
                print(type(item.name))

client.run(TOKEN)