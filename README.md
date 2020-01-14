# ChnnlBot
Discord bot that creates a private channel on server member request

## User commands:

To create a private channel with a set of members:

- ?makechannel [channelName] [channelMembers]

  - The user doing the bot request is added to the channel automatically.

  - Currently, the usernames queried for added members are Discord usernames, not server nicknames. A fix for this is on the to-do list.

## Usage

To use this bot, you need to:

- Add your own .env file:

```
DISCORD_TOKEN=[yourDiscordToken]
DISCORD_GUILD=[nameOfServer]
CATEGORY=[categoryName]
```

- Host the bot on a python server
  - Start the bot by running `python3 bot.py`. If it started correctly, you should see a terminal message that says Online.
