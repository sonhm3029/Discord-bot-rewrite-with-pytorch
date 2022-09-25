import discord
from discord.ext.commands import Bot
import os
import json
import time
import asyncio

# discord bot token
token = os.environ['token']
server_id = os.environ['server_id']

intents = discord.Intents.default()
intents.message_content = True
messages = joined = 0

client = discord.Client(intents=intents)


async def update_stats():
    await client.wait_until_ready()
    global messages, joined

    while not client.is_closed():
        try:
            with open("stats.txt", "a") as f:
                f.write(f"Time: {int(time.time())}, Messages: {messages}, Members joined: {joined}\n")
            messages = 0
            joined = 0

            await asyncio.sleep(5)
        except Exception as e:
            print(e)
            await asyncio.sleep(5)


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_member_join(member):
    global joined
    joined += 1
    for channel in member.server.channels:
        if str(channel) == "chung":
            await client.send_message(f"""Welcome to my server {member.mention}""")


@client.event
async def on_message(msg):
    global messages
    messages += 1
    guide = client.get_guild(int(server_id))
    channels = ["chung"]
    valid_users = ["sonhm#7995"]

    if str(msg.channel) in channels:
        if msg.content == "$help":
            embed = discord.Embed(title='Help on BOT', description='Some useful commands')
            embed.add_field(name='$hello', value="Greets the user")
            embed.add_field(name='$users', value="Number of users")
            await msg.channel.send(content=None, embed=embed)

        if msg.content.find("$hello") != -1:
            await msg.channel.send("Hi!")
        elif msg.content == "$users":
            await msg.channel.send(f"""# of Members {guide.member_count}""")
    else:
        print(f"""User: {msg.author} tried to do command {msg.content}, in channel {msg.channel}""")


@client.event
async def setup_hook():
    client.loop.create_task(update_stats())


client.run(token)
