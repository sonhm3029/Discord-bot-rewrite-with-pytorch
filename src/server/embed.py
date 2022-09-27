import discord
from server.cmdFunc import CHANNEL_COMMAND

def initEmbed():
    embed =  discord.Embed(title='Help on BOT', description='Some useful commands', colour=discord.Colour.blue())
    return  embed

def processEmbed(channel_commands, embed):
    for command in channel_commands.keys():
        description = channel_commands[command]['description']
        embed.add_field(name=f'${command}', value=description)

async def chung_helper(channel):
    chung_embed = initEmbed()
    # chung_embed.add_field(name='$statistic', value='See server statistic')
    processEmbed(CHANNEL_COMMAND['chung'], chung_embed)
    await channel.send(content=None, embed=chung_embed)

async def music_helper(channel):
    music_embed = initEmbed()
    processEmbed(CHANNEL_COMMAND['music'], music_embed)
    await channel.send(content=None, embed = music_embed)

async def chat_helper(channel):
    chat_embed = initEmbed()
    processEmbed(CHANNEL_COMMAND['chatting'], chat_embed)
    await channel.send(content=None, embed = chat_embed)