import discord
from discord.ext import commands
import json
from tokengen import osuapi
from user import get_user
import datetime
import time

class osu(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.slash_command(
        name="osuregister",
        description="register your osu ID to the bot"
    )
    async def osuregister(self, ctx, playerid:int):
        params = {
            'key': 'id'
        }
        link = f"users/{playerid}"
        data = osuapi(params, link)
        
        if data.status_code != 200:
            await ctx.respond("player id is invalid.")
            return

        with open("users.json") as file:
            listObj = json.load(file)

        listObj[str(ctx.user.id)] = playerid

        with open("users.json", 'w') as json_file:
            json.dump(listObj, json_file, indent=2)

        await ctx.respond(f"your profile is set to {data.json()['username']}")
    
    @commands.slash_command(
        name="topplay",
        description="Get the pp value of your top play in osu"
    )
    async def topplay(self, ctx):
        playerid = await get_user(ctx)
        params = {
            'mode': 'osu',
            'limit': 1
        }
        link = f"users/{playerid}/scores/best"
        data = osuapi(params, link).json()
        print(json.dumps(data, indent=2))
        embed = discord.Embed(
            description = f'{data[0]["weight"]["pp"]}pp\nplay set at <t:{round((time.mktime(datetime.datetime.strptime(data[0]["created_at"], "%Y-%m-%dT%H:%M:%S%z").timetuple())))}>\n[Map Link]({data[0]["beatmap"]["url"]})',
            )
        embed.set_author(name = f"{data[0]['beatmapset']['title']} [{data[0]['beatmap']['version']}]",
                         url = data[0]['beatmap']['url'])
        await ctx.respond(embed=embed)

    @commands.slash_command(
    name="recent",
    description="Get the pp value of your most recent play in osu"
    )
    async def recent(self, ctx):
        playerid = await get_user(ctx)
        params = {
            'mode': 'osu',
            'limit': 1
        }
        link = f"users/{playerid}/scores/recent"
        data = osuapi(params, link).json()
        print(json.dumps(data, indent=2))
        embed = discord.Embed(
            description = f'{data[0]["pp"]}pp\nplay set at <t:{round((time.mktime(datetime.datetime.strptime(data[0]["created_at"], "%Y-%m-%dT%H:%M:%S%z").timetuple())))}>',
            )
        embed.set_author(name = f"{data[0]['beatmapset']['title']} [{data[0]['beatmap']['version']}]",
                         url = data[0]['beatmap']['url'])
        await ctx.respond(embed=embed)

def setup(client):
    client.add_cog(osu(client))