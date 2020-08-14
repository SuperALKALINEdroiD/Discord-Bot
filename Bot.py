import discord
from BasicCalculator import add, subtract
client = discord.Client()
@client.event
async def on_message(message):
    md_result = 1
    if message.author.bot:
        pass
    elif message.content.startswith("add"):
        addResult = add(message.content)
        plus = addResult.getResult()
        await message.channel.send(plus)
    elif message.content.startswith("sub"):
        subResult = subtract(message.content)
        minus = subResult.get_result()
        await message.channel.send(minus)
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
    elif message.content.startswith("rem"):
        user_msg = message.content
        message_content = user_msg.split()
        if len(message_content) > 3:
            await message.channel.send("Not Supported yet, Unsure what would it mean to do")
        else:
            number1 = int(message_content[1])
            number2 = int(message_content[2])
            md_result = number1 % number2
            await message.channel.send(md_result)



client.run("Token")