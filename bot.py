import discord
from discord.ext import commands
import random
from messages import *

# bot = commands.Bot(command_prefix='.')

client = commands.Bot(command_prefix='.')

@client.event
async def on_ready():
    print("I am ready!")

# @client.event
# async def on_message(message):

#     msg = message.content

#     if message.author == client.user:
#         return
#     if msg in greetings:
#         await message.channel.send('Hello!')
#     elif any(word in msg for word in health):
#         await message.channel.send(random.choice(happy))
#     elif msg in activities:
#         await message.channel.send(random.choice(activity_answers))
#     elif msg.startswith("Tell me a fact"):
#         await message.channel.send(random.choice(facts))

@client.command()
async def ping(ctx):
    await ctx.send("pong")

@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)

client.run("NzY4NDk4NTIwNDc0MjU1Mzgx.X5BWBQ.lswZPYzR1vlghbIT063S2WQeiHE")
# bot.run("NzY4NDk4NTIwNDc0MjU1Mzgx.X5BWBQ.lswZPYzR1vlghbIT063S2WQeiHE")