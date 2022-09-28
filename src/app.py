import logging
import discord
from constants.env import *
from server.client import *
from server.bot import bot
from server.log import logger
# import ffmpeg

intents = discord.Intents.default()
intents.message_content = True
intents.members = True


client = SonHMBot(intents=intents)

client.run(token, log_handler=None)
# bot.run(token)
