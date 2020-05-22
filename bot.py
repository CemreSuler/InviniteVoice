#bot.py
#loading in the dependencies
import os
import discord
from discord.utils import get
from dotenv import load_dotenv

channelsToCheck = []
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
    if before.deaf == after.deaf and before.mute == after.mute and before.self_mute == after.self_mute and before.self_deaf == after.self_deaf and before.self_stream == after.self_stream and before.self_video == after.self_video and before.afk == after.afk:
        memberCount = 0
        oldMemberCount = 0
        channelWasEmpty = False
        try:
            for a in before.channel.members:
                oldMemberCount = oldMemberCount + 1
        except:
            channelWasEmpty = True

        for i in after.channel.members:
            memberCount = memberCount + 1
        #If that count is equal (or higher) than the user cap, create another channel.
        if channelWasEmpty == True and memberCount == 1:
            await member.guild.create_voice_channel(after.channel.name + "+",category=after.channel.category,user_limit=after.channel.user_limit) 
        if "+" in after.channel.name and memberCount == 0:
            mainChannelMembers = 0
            mainChannelString = (after.channel.name).replace('+','')
            print(mainChannelString)
            mainChannel = discord.utils.find(lambda c: c.name == mainChannelString, after.channel.guild.voice_channels)
            for b in mainChannel.members:
                mainChannelMembers = mainChannelMembers + 1
                print(mainChannelMembers)
            if mainChannelMembers == 0:
                await after.channel.delete()

client.run(TOKEN)
