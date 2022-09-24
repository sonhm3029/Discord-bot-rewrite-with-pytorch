import discord
import os
import json

# discord bot token
token = os.environ['token']

intents = discord.Intents.default()
intents.message_content = True


client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(msg):
    if msg.content.find("!hello") != -1:
        await msg.channel.send("Hi")


client.run(token)
