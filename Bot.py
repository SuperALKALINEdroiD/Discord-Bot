import discord

client = discord.Client()
@client.event
async def on_message(message):
    await message.channel.send("Hi")

client.run("NzA3NTYxMTI2MDExMDc2NzMz.XrKmGQ.G6A1lTqs0zLdYAEvatXJ562nPdU")