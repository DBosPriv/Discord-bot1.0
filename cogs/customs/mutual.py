import discord
from discord.ext import commands
import time

class mutual(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.slash_command(
        name="mutual",
        description="Fetches mutual servers shared betwen the bot and the specified user"
    )
    @commands.is_owner()
    async def _mutual(self,ctx,user:discord.User):
        if user == self.client.user:
            await ctx.respond(f"I can't check mutual server with myself")
        else:
            userprofile = await self.client.fetch_user(user.id)
            await ctx.respond(f'Mutual servers with {user}')
            for server in userprofile.mutual_guilds:
                await ctx.send('-')
                await ctx.send(f'{userprofile.mutual_guilds.index(server)+1} : {server.name}')
            await ctx.send('Use "/mutual_invite (user) (server number)" for a server invite.')

    @commands.slash_command(
        name="mutual_invite",
        description="Creates an invite for a mutual server shared between the bot and the specified user"
    )
    @commands.is_owner()
    async def mutual_invite(self,ctx,user:discord.User,servernum:int):
        if user == self.client.user:
            return
        else:
            userprofile = await self.client.fetch_user(user.id)
            channels = []
            guilds = []
            for server in userprofile.mutual_guilds:
                guilds.append(server)
            for channel in guilds[servernum-1].channels:
                channels.append(channel)
            for x in range(len(channels)):
                if x-1 <= len(channels):
                    try:
                        channel = channels[x-1]
                        link = await channel.create_invite(max_age = 300)
                        await ctx.respond(f'server invite = {link}')
                        channels.clear()
                        time.sleep(5)
                        break
                    except:
                        continue
                else:
                    print("couldnt make an invite for this server")

def setup(client):
    client.add_cog(mutual(client))