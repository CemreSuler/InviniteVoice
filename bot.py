#bot.py
#loading in the dependencies
import os
import discord
from discord.utils import get
from dotenv import load_dotenv

channelsToDelete = []

#NEED TO FIX THIS WITH A BETTER ENV FILE!!
TOKEN = "NzEzNDQwMzMxODY5MzIzMjc0.XshM-w.V3YRYNwS0I1-u0HRGbekqjqILDY"
client = discord.Client()

@client.event
#Tells to the console the bot is ready
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
#Command to test creating voice channels
async def on_message(message):
    if message.content == "iv!testchannel":
        await message.guild.create_voice_channel("testchannel")

@client.event
async def on_voice_state_update(member,before,after):
    overwrites = {
        member.guild.get_role(713839595661295677): discord.PermissionOverwrite(connect=False)
    }
    if before.deaf == after.deaf and before.mute == after.mute and before.self_mute == after.self_mute and before.self_deaf == after.self_deaf and before.self_stream == after.self_stream and before.self_video == after.self_video and before.afk == after.afk:
        try:
            if len(after.channel.members) == 1:
                await member.guild.create_voice_channel(after.channel.name,category=after.channel.category,user_limit=after.channel.user_limit,position=after.channel.position, overwrites=overwrites)
                await after.channel.edit(name=(after.channel.name).replace('Create New ',''), overwrites=None)
                channelsToDelete.append(after.channel.id)
        except:
            if (before.channel.id in channelsToDelete) and len(before.channel.members) == 0:
                await before.channel.delete()
                channelsToDelete.remove(before.channel.id)
    for g in channelsToDelete:
        channelToCheck = client.get_channel(g)
        if len(channelToCheck.members) == 0:
            await channelToCheck.delete()
            channelsToDelete.remove(g)
    for duo in before.channel.category.voice_channels:
        duoToCheck = discord.utils.get(before.channel.category.voice_channels, name="Duo")
        if(duoToCheck):
            if len(duoToCheck.members) == 0:
                await duoToCheck.delete()
                duoToCheck.remove(before.channel.id)

    for trio in before.channel.category.voice_channels:
        trioToCheck = discord.utils.get(before.channel.category.voice_channels,name="Trio")
        if(trioToCheck):
            if len(trioToCheck.members) == 0:
                await trioToCheck.delete()
                trioToCheck.remove(before.channel.id)
    
    for squad in before.channel.category.voice_channels:
        squadToCheck = discord.utils.get(before.channel.category.voice_channels,name="Squad")
        if(squadToCheck):
            if len(squadToCheck.members) == 0:
                await squadToCheck.delete()
                squadToCheck.remove(before.channel.id)
client.run(TOKEN)
