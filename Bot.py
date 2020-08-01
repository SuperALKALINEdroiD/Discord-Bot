import discord

client = discord.Client()
@client.event
async def on_message(message):
    await message.channel.send("Hi")

client.run("Token Here")