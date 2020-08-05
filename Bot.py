import discord
import string

client = discord.Client()
@client.event
async def on_message(message):
    if message.author.bot:
        pass
    elif  message.content.startswith("add"):
        user_msg = message.content
        message_content = user_msg.split()
        try:
            number_1 = (int)(message_content[1])
            number_2 = (int)(message_content[2])
            await message.channel.send(number_1 + number_2)
        except:
            await message.channel.send("Error needed 2 numbers")



client.run("TOken")