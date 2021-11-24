import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
    print('<ADD SOMTHING>')
    await client.change_presence(activity=discord.Game(
    name= "community moment"))
    
    
    client.command()
    aysnc def hello(ctx):
     await ctx.send('HELLO WORLD")

