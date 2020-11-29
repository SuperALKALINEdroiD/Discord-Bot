import discord
from CalC import add, subtract, multiply, division, remainder
from twilio_message import *

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

token_file = open("discord_token.txt", "r")
token = token_file.read()


@client.event
async def on_ready():
    print( str(client.user) + " is Ready!!")


@client.event
async def on_message(message):
    if client.user == message.author:
        pass
    elif message.content.startswith("add"):
        addResult = add(message.content)
        await message.channel.send(addResult.getResult())
    elif message.content.startswith("sub"):
        subResult = subtract(message.content)
        await message.channel.send(subResult.get_result())
    elif message.content.startswith("multiply"):
        mul_result = multiply(message.content)
        await message.channel.send(mul_result.get_result())
    elif message.content.startswith("div"):
        divResult = division(message.content)
        await message.channel.send(divResult.get_result())
    elif message.content.startswith("rem"):
        remResult = remainder(message.content)
        await message.channel.send(remResult.get_result())
    elif message.content.startswith("sms"):
        sms = twilio_message(message.content)
        await message.channel.send(sms.send_sms())

    


@client.event
async def on_member_join(member):
    for channel in member.guild.channels:
        if str(channel) == "member-log":
            await channel.send(f"{member.mention} Joined, Have a good time here!")


@client.event
async def on_member_remove(member):
    for channel in member.guild.channels:
        if str(channel) == "member-log":
            await channel.send(f'{member.mention} left, You won\'t be missed(Probably  xD)!')


client.run(token)
