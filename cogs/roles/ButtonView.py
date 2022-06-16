from discord.ui import View
import discord
from discord.ext import commands
import random

client = commands.Bot(command_prefix='t.',owner_id = "")

class Roles(View):
    def __init__(self):
        super().__init__(timeout=None)
        self.client = client

    async def button_callback(self,button,interaction):
        member = interaction.user
        role = interaction.guild.get_role(int(button.custom_id))
        if role in member.roles:
            await member.remove_roles(role)
            await interaction.response.send_message(f"{role.name} role has been removed",ephemeral=True)
        else:
            await member.add_roles(role)
            await interaction.response.send_message(f"{role.name} role has been added",ephemeral=True)

    @discord.ui.button(label="Role",style=discord.ButtonStyle.green,custom_id="978594487351795763")
    async def Roles(self,button,interaction):
        await self.button_callback(button,interaction)

class KillChannel(View):
    def __init__(self):
        super().__init__(timeout=None)
        self.client = client

    async def button_callback(self,button,interaction):
        await interaction.channel.delete()
    
    @discord.ui.button(label="Kill channel",style=discord.ButtonStyle.red,custom_id="kill_channel")
    async def KillChannel(self,button,interaction):
        await self.button_callback(button,interaction)

class MentionButton(View):
    def __init__(self):
        super().__init__(timeout=None)
        self.client = client

    async def button_callback(self,button,interaction):
        memberlist=[]
        for member in interaction.guild.members:
            memberlist.append(member)
        await interaction.response.send_message(memberlist[random.randrange(len(memberlist))].mention)

    @discord.ui.button(label="Mention",style=discord.ButtonStyle.red,custom_id="MentionButton")
    async def MentionButton(self,button,interaction):
        await self.button_callback(button,interaction)