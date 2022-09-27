import discord
from constants.env import *
from server.cmdFunc import CHANNEL_COMMAND
from server.embed import chung_helper, music_helper, chat_helper

# Embed helper command bot
greeting_embed = discord.Embed(title='Help on BOT', description='Some useful commands')
greeting_embed.add_field(name='$help', value="See channel help")
# greeting_embed.add_field(name='$statistic', value='See server statistic')

# channels
channels = ['chatting', "music", 'chung']
# Switcher on bot command
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
        if str(channel) in channels and msg.content != '$help' and str(msg.content).startswith('$'):
            try:
                await CHANNEL_COMMAND[str(channel)][str(msg.content)[1:]]['action'](channel, self)
            except KeyError:
                embed_warning = discord.Embed(colour=discord.Colour.brand_red())
                embed_warning.add_field(
                    name="Wrong command!",
                    value="You've send a wrong key, type $help to see list commands", 
                )
                await channel.send(
                    content=None,
                    embed=embed_warning
                )
        
        


