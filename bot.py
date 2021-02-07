import sys
sys.path.insert(0, '/videos/')
from videos import video
import discord
import random
import asyncio


repeat = 0
TOKEN = "NzczNTk2OTQ2MDkzOTY1MzYz.X6LiTA.oWRCeYSh9pK9bESHv-9TSe9-Pio"
client = discord.Client()
general = None
prefix = "$"
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
                repeat = 1
                await Rep(message.channel, message.content[7:9], message.content[9:11])
            except:
                await message.channel.send("Invalid Format")
                await message.channel.send(message.content[7:9])
                await message.channel.send(message.content[9:11])
        if "$stop" in message.content:
            repeat = 0

message = None
@client.event
async def on_message_edit(before, after):
    message = after
    if not message.author.bot:
        await message.channel.send(after.author.name + " Sent this:")
        await message.channel.send(before.content)
        await message.channel.send("then edited to this:")
        await message.channel.send(after.content)
async def Rep(c, t, times):
  for i in range(int(times)):
    await c.send(";;rewind " + t)
    await asyncio.sleep(int(t))
message = None
@client.event
async def on_message_delete(message):
    await message.channel.send(message.author.name + " Sent this then deleted:")
    await message.channel.send(message.content)
client.run(TOKEN)

