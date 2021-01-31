import discord
import random
import threading 

TOKEN = "NzczNTk2OTQ2MDkzOTY1MzYz.X6LiTA.oWRCeYSh9pK9bESHv-9TSe9-Pio"
client = discord.Client()
general = None
prefix = "$"
repeat = False
rythm_repeat_interval = 0

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
            await message.add_reaction("🥚")
        if "$repeat" in message.content:
            try:
                await Rep(message.channel, float(message.content[8:]))
            except:
                await message.channel.send("Invalid Format")

message = None
@client.event
async def on_message_edit(before, after):
    message = after
    if not message.author.bot:
        await message.channel.send(after.author.name + " Sent this:")
        await message.channel.send(before.content)
        await message.channel.send("then edited to this:")
        await message.channel.send(after.content)
async def Rep(c, t):
  await c.send("!rewind " + int(t) )

message = None
@client.event
async def on_message_delete(message):
    await message.channel.send(message.author.name + " Sent this then deleted:")
    await message.channel.send(message.content)
client.run(TOKEN)

