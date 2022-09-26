import discord
from constants.env import *

# Embed helper command bot
greeting_embed = discord.Embed(title='Help on BOT', description='Some useful commands')
greeting_embed.add_field(name='$help', value="See channel help")
# greeting_embed.add_field(name='$statistic', value='See server statistic')

# channels
channels = ['chatting', "music", 'chung']

def initEmbed():
    embed =  discord.Embed(title='Help on BOT', description='Some useful commands')
    embed.add_field(name='$help', value="See channel help")
    return  embed

# Switcher on bot command
async def chung_helper(channel):
    chung_embed = initEmbed()
    chung_embed.add_field(name='$statistic', value='See server statistic')
    await channel.send(content=None, embed=chung_embed)

async def music_helper(channel):
    music_embed = initEmbed()
    await channel.send(content=None, embed = music_embed)

async def chat_helper(channel):
    chat_embed = initEmbed()
    await channel.send(content=None, embed = chat_embed)

help_command = {
    'chung':chung_helper,
    'music': music_helper,
    'chatting':chat_helper
}

class SonHMBot(discord.Client):
    def __init__(self, intents):
        super().__init__(intents=intents)
        
    async def on_ready(self):
        print(f'{self.user} has connected to discord!')
        
    async def on_member_join(self,member):
        guild = member.guild
        if guild.system_channel is not None:
            to_send = f"Chào mừng {member.mention} đến với {guild.name}"
            await guild.system_channel.send(to_send)
            await guild.system_channel.send(content=None, embed=greeting_embed)
        
        
    async def on_message(self, msg):
        # Get server guide
        guide = self.get_guild(int(server_id))
        channel = msg.channel
        if msg.content == '$help' and (str(channel) in channels):
            await help_command[str(channel)](channel)
        
        


