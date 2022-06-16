import discord
from discord.ext import commands

class error(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_command_error(self,ctx,error):
        if isinstance(error,commands.NotOwner):
            await ctx.send("You're not the owner of this bot")
        elif isinstance(error,commands.MissingRequiredArgument):
            await ctx.send("give more argument")
        elif isinstance(error,commands.TooManyArguments):
            await ctx.send("give less argument")
        else:
            print(error)

    @commands.Cog.listener()
    async def on_application_command_error(self,ctx,error):
        if isinstance(error,commands.NotOwner):
            await ctx.respond("You're not the owner of this bot",ephemeral=True)
        elif isinstance(error,commands.MissingRequiredArgument):
            await ctx.respond("give more argument",ephemeral=True)
        elif isinstance(error,commands.TooManyArguments):
            await ctx.respond("give less argument",ephemeral=True)
        else:
            print(error)

def setup(client):
    client.add_cog(error(client))