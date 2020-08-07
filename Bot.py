import discord
client = discord.Client()
@client.event
async def on_message(message):
    add_result = 0
    if message.author.bot:
        pass
    elif  message.content.startswith("add"):
        user_msg = message.content
        message_content = user_msg.split()
        if len(message_content) == 2:
            await message.channel.send("addition requires more than one operands")
        else:
            for i in range(1, len(message_content)):
                add_result = add_result + int(message_content[i])
            await message.channel.send(add_result)
client.run("Token")