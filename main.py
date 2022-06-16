from distutils import extension
import glob
import discord
from discord.ext import commands
import sys

sys.dont_write_bytecode = True

intents = discord.Intents().all()

client = commands.Bot(command_prefix="t.",owner_id = "",help_command=None,intents=intents)

@client.command()
@commands.is_owner()
async def load(ctx, extension):
    for file in glob.glob('cogs\**\*.py'):
        if extension in file:
            file = (file.replace("\\", "."))[5:-3]
            client.load_extension(f'cogs.{file}')
            await ctx.send(f"loaded {extension}")

@client.command()
@commands.is_owner()
async def unload(ctx, extension):
    for file in glob.glob('cogs\**\*.py'):
        if extension in file:
            file = (file.replace("\\", "."))[5:-3]
            client.unload_extension(f'cogs.{file}')
            await ctx.send(f"unloaded {extension}")

@client.command()
@commands.is_owner()
async def reload(ctx, extension):
    for file in glob.glob('cogs\**\*.py'):
        if extension in file:
            file = (file.replace("\\", "."))[5:-3]
            client.unload_extension(f'cogs.{file}')
            client.load_extension(f'cogs.{file}')
            await ctx.send(f"reloaded {extension}")

@client.command()
@commands.is_owner()
async def reload_all(ctx):
    for file in glob.glob('cogs\**\*.py'):
        try:
            file = (file.replace("\\", "."))[5:-3]
            client.unload_extension(f'cogs.{file}')
            client.load_extension(f'cogs.{file}')
            await ctx.send(f"reloaded {file}")
        except:
            pass

for filename in glob.glob('cogs\**\*.py'):
    try:
        if "View" not in filename:
            filename = (filename.replace("\\", "."))[5:-3]
            client.load_extension(f'cogs.{filename}')
            print(f'loaded {filename}')
    except Exception as e:
        print(e)

client.run("")