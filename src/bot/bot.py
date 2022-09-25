import discord

class SonHMBot(discord.Client):
    def __init__(self, intents):
        super().__init__(intents=intents)
        
    async def on_ready(self):
        print(f'{self.user} has connected to discord!')
        
    async def on_member_join(self,member):
        await member.create_dm()
        await member.dm_channel.send(
            f'Hi {member.name}, chào mừng bạn đến với discord server của mình!'
        )
        


