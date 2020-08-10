import discord
client = discord.Client()
@client.event
async def on_message(message):
    result = 0                                                                           # operation result
    md_result = 1
    if message.author.bot:
        pass
    elif message.content.startswith("add"):
        user_msg = message.content
        message_content = user_msg.split()
        if len(message_content) == 2:                                                       # case of 1 operand
            await message.channel.send("addition requires more than one operands")
        else:
            for i in range(1, len(message_content)):
                result = result + int(message_content[i])
            await message.channel.send(result)
    elif message.content.startswith("sub"):
        user_msg = message.content
        message_content = user_msg.split()
        if len(message_content) == 2:                                                        # case of 1 operand
            await message.channel.send("Subtraction requires more than one operands")
        else:
            result = int(message_content[1])
            for i in range(2, len(message_content)):
                result = result - int(message_content[i])
            await message.channel.send(result)
    elif message.content.startswith("multiply"):
        user_msg = message.content
        message_content = user_msg.split()
        if len(message_content) == 2:                                                       # case of 1 operand
            await message.channel.send("Multiplication requires more than one operands")
        else:
            for i in range(1, len(message_content)):
                md_result = md_result * int(message_content[i])
            await message.channel.send(md_result)
    elif message.content.startswith("div"):
        user_msg = message.content
        message_content = user_msg.split()
        if len(message_content) == 2:                                                       # case of 1 operand
            await message.channel.send("Division requires more than one operands")
        else:
            md_result = int(message_content[1])
            for i in range(2, len(message_content)):
                md_result = md_result / int(message_content[i])
            await message.channel.send(md_result)


client.run("Token")