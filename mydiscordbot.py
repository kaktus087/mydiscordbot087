import discord
from discord.ext import commands
from sympy import *
import os
x = symbols('x')

client = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
	print("Bot connected")

@client.command()
async def bot( ctx, message ):
	await ctx.send(diff(message))



TOKEN = os.environ.get('BOT_TOKEN')
client.run(str(TOKEN))
