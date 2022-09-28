from constants.env import *
import discord

async def say_hi(channel, client, following_vars = []):
    await channel.send(content="Hello mother fucker !!!")

async def statistic(channel, client, following_vars = []):
    guide = client.get_guild(int(server_id))

    num_online = 0
    
    for member in guide.members:
        listStatus = [
            member.status,
            member.mobile_status,
            member.web_status,
            member.desktop_status
        ]
        if discord.Status.offline not in listStatus:
            num_online +=1
    
    statisticShow = f"Number of members: {guide.member_count}\nCurrently online: {num_online}"
    await channel.send(statisticShow)

async def playMusic(channel, client, following_vars = []):
    guild = client.get

async def pauseMusic(channel, client, following_vars = []):
    pass

async def stopMusic(channel, client, following_vars = []):
    pass

async def resumeMusic(channel, client, following_vars = []):
    pass

async def leaveChannel(channel, client, following_vars = []):
    pass

CHANNEL_COMMAND = {
    'chung' : {
        'help': {
            'name':"help",
            'description':"See channel help"
        },
        'say_hi': {
            'description':"Bot say hi to you.",
            'action':say_hi    
        },
        'statistic': {
            'description':"See server statistic.",
            'action':statistic
        }
    },
    
    'music' : {
        'help': {
            'description':"See channel help"
        },
        'play': {
            'description':"Play channel music",
            'action': playMusic
        },
        'pause': {
            'description':"Pause current playing music",
            'action':pauseMusic
        },
        'stop': {
            'description': "Stop current playing music",
            'action': stopMusic
        },
        'resume': {
            'description': "Resume current paused music",
            'action': resumeMusic
        },
        'leave': {
            'description': "Leave music channel",
            'action': leaveChannel
        }
    },

    'chatting' : {
        'help': {
            'description':"See channel help"
        },
    }
}