import discord
from CalC import add, subtract, multiply, division, remainder
client = discord.Client()

@client.event
async def on_ready():
    print("Ready as " + str(client.user) + "!" )

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
        await message.channel.send( mul_result.get_result())
    elif message.content.startswith("div"):
        divReult = division(message.content)
        await message.channel.send(divReult.get_result())
    elif message.content.startswith("rem"):
        remResult = remainder(message.content)
        await message.channel.send(remResult.get_result())

client.run("Token")