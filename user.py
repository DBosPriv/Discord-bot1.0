import json

async def get_user(ctx):
    with open("users.json", "r") as file:
        data = json.load(file)
        if str(ctx.user.id) in data:
            return data[str(ctx.user.id)]
        else:
            await ctx.respond("User not registered, please use /osuregister")
            return