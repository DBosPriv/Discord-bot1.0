import discord
from discord.ext import commands
from .ButtonView import Roles, KillChannel, MentionButton

class roles(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        self.client.add_view(Roles())

    @commands.command()
    async def roles(self,ctx):
        await ctx.channel.send("Click to get/remove role", view=Roles())

    @commands.command()
    async def killchannel(self,ctx):
        await ctx.channel.send("Click to get delete channel", view=KillChannel())

    @commands.command()
    async def mentionbutton(self,ctx):
        await ctx.channel.send("Click to mention random member", view=MentionButton())

def setup(client):
    client.add_cog(roles(client))