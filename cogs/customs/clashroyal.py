import discord
from discord.ext import commands
import requests
import json

token = ""

class clashroyal(commands.Cog):

    def __init__(self, client):
        self.client = client

    
    @commands.slash_command(
        name="crchest",
        description="Shows your upcoming chests in clash royale"
    )
    @commands.is_owner()
    async def crchest(self, ctx, crtag):
        r=requests.get(f"https://api.clashroyale.com/v1/players/%23{crtag.upper()}/upcomingchests", headers={"Accept":"application/json", "authorization": token}, params = {"limit":20})
        await ctx.respond(json.dumps(r.json(), indent = 2))


    @commands.slash_command(
        name="crmatch",
        description="Shows your changed trophies in the last clash royale match"
    )
    @commands.is_owner()
    async def crmatch(self, ctx, crtag, match:int):
        r=requests.get(f"https://api.clashroyale.com/v1/players/%23{crtag.upper()}/battlelog", headers={"Accept":"application/json", "authorization":token}, params = {"limit":match})
        r = json.dumps(r.json(), indent=2)
        print(r)
        await ctx.respond(r[match-1]["team"][0]["trophyChange"])

    @commands.slash_command(
    name="crinfo",
    description="Shows your changed trophies in the last clash royale match"
    )
    @commands.is_owner()
    async def crinfo(self, ctx, crtag):
        r=requests.get(f"https://api.clashroyale.com/v1/players/%23{crtag.upper()}/battlelog", headers={"Accept":"application/json", "authorization":token}, params = {})
        r = json.dumps(r.json(), indent=2)
        print(r)
        await ctx.respond(r)

def setup(client):
    client.add_cog(clashroyal(client))