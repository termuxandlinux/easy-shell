#!/bin/bash

mkdir $HOME/dbot

pip install discord.py

echo "Do you use Client/Bot? (Type 'Client' or 'Bot')"
read answer

if [ "$answer" == "Client" ]; then
    echo "What is your Bot token?"
    read token
    cat <<EOF >$HOME/dbot/dbot.py
import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == 'ping':
            await message.channel.send('pong')

intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run('$token')
EOF

elif [ "$answer" == "Bot" ]; then
    echo "What is your Bot token?"
    read token
    cat <<EOF >$HOME/dbot/dbot.py
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='>', intents=intents)

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

bot.run('$token')
EOF

else
    echo "Invalid input. Please type 'Client' or 'Bot'."
    exit 1
fi
