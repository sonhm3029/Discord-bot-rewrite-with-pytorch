import discord
from constants.env import *
from server.client import *
# from server.bot import bot

intents = discord.Intents.default()
intents.message_content = True
intents.members = True


client = SonHMBot(intents=intents)

client.run(token)
# bot.run(token)
