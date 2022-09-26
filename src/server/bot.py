from dis import disco
import discord
from discord.ext import commands
import random
from constants.env import *


"""
https://stackoverflow.com/questions/51234778/what-are-the-differences-between-bot-and-client#:~:text=Bot%20is%20an%20extended%20version,Bot%20can%20do%20it%20too.
"""

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='?', intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

@bot.command()
async def saying(ctx):
    """sayingOK"""
    await ctx.send("OK")
    
    