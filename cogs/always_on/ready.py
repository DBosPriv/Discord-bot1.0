import discord
from discord.ext import commands
import time

class ready(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print(self.client.user.name,'is ready')

def setup(client):
    client.add_cog(ready(client))