import sys
import ffmpeg
from discord.player import AudioSource
sys.path.insert(0, '/videos/')
from videos import video
import discord
import random
import asyncio

repeat = 0
TOKEN = "NzczNTk2OTQ2MDkzOTY1MzYz.X6LiTA.oWRCeYSh9pK9bESHv-9TSe9-Pio"
client = discord.Client()
vc = None
voice_client = None
prefix = "$"
@client.event
async def on_ready():
    global vc
    GUILD = client.guilds[0]
    vc = discord.utils.get(client.guilds[0].voice_channels)
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{GUILD.name}(id: {GUILD.id})'
    )
@client.event
async def on_message(message):
        global voice_client
        if "ههه" in message.content:
            await message.add_reaction("🥚")
        if "$summon" in message.content:
            voice_client = await vc.connect()
            source = await discord.FFmpegOpusAudio.from_probe("p.webm")
            voice_client.play(source)
        if "$leave" in message.content:
            await voice_client.disconnect()
            voice_client = None
        if "$leave" in message.content:
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

