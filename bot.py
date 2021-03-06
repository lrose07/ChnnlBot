import os

import discord
from discord.ext import commands
from discord.utils import find
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
CATEGORY = os.getenv('CATEGORY')

bot = commands.Bot(command_prefix='?')

client = discord.Client()


@client.event
async def on_ready():
    print("Online")


@bot.command(name='tt')
async def test(ctx):
    print("command entered")
    await ctx.send("Message received")


@client.event
async def on_message(message):
    guild = message.channel.guild
    categories = guild.categories

    if message.content[0] == "?":
        if "makechannel" in message.content:
            found_category = None

            for cat in categories:
                if CATEGORY in cat.name:
                    found_category = cat

            if found_category is None:
                found_category = await guild.create_category(CATEGORY)

            contents = message.content.split(" ")
            channel_members = []

            for x in range(2, len(contents)):
                channel_members.append(contents[x])

            overwrites = {
                guild.default_role: discord.PermissionOverwrite(read_messages=False),
                guild.me: discord.PermissionOverwrite(read_messages=True)
            }

            overwrites.update({message.author: discord.PermissionOverwrite(
                read_messages=True,
                send_messages=True
            )})

            for user in channel_members:
                print(user)
                member = find(lambda m: m.name == user, guild.members)
                if member is not None:
                    overwrites.update({member: discord.PermissionOverwrite(
                        read_messages=True,
                        send_messages=True)})
                else:
                    print("Can't find: ", user)
                    await message.channel.send("Cannot find one of the users entered")

            if found_category is not None:
                new_channel = await guild.create_text_channel(
                    name=contents[1],
                    category=found_category,
                    overwrites=overwrites)
                await new_channel.send("Welcome to your private channel!")
                await message.channel.send("New channel created under the private category.")
            else:
                message.channel.send("Something went wrong")
                print("Category not found")

        else:
            await message.channel.send("I don't know what you're talking about!")
            print(message.author)

client.run(TOKEN)
