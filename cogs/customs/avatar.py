import discord
from discord.ext import commands

class avatar(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.command()
    @commands.is_owner()
    async def avatar(self, ctx, user:discord.User):
        image = user.avatar
        image = await image.read()
        await self.client.user.edit(avatar=image)
        await ctx.send(f"I changed my avatar to this {user.avatar}")

def setup(client):
    client.add_cog(avatar(client))