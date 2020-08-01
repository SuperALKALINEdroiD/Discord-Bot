import discord

client = discord.Client()
@client.event
async def on_message(message):
    await message.channel.send(message.content)

client.run("Token")