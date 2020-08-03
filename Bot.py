import discord

client = discord.Client()
@client.event
async def on_message(message):
    if message.author.bot:
        pass
    else:
        await message.channel.send(message.content)

client.run("Token")