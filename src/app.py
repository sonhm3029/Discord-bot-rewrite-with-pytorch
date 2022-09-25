import discord
from constants.env import *
from bot.bot import *

intents = discord.Intents.default()
intents.message_content = True

client = SonHMBot(intents=intents)

client.run(token)
