import discord
from discord.ext import commands
import math
from keep_alive import keep_alive
import os

client = commands.Bot(command_prefix='%')

@client.event
async def on_ready():
  print("Welcome Aboard!")
  print(client.user.name)

@client.command()
async def author(ctx, ):
  embed = discord.Embed(title="Proudly made by Raishu! ", color=5763719)
  await ctx.send(embed=embed)
  
@client.command()
async def commands(ctx, ):
  embed = discord.Embed(title='Here is the list of commands: \n%add \n%sub \n%mul \n%div \n%mod \n%sqrt \n%exp \n%author \n%commands \nInsert first and second number respectively. ex. %add 1 2', color=5763719)
  await ctx.send(embed=embed)

@client.command()
async def add(ctx, x: float, y: float):
  embed = discord.Embed(title="Answer: ", description=x+y, color=5763719)
  embed.set_footer(text="Created by Raishu")
  await ctx.send(embed=embed)

@client.command()
async def sub(ctx, x: float, y: float):
  embed = discord.Embed(title="Answer: ", description=x-y, color=5763719)
  embed.set_footer(text="Created by Raishu")
  await ctx.send(embed=embed)

@client.command()
async def mul(ctx, x: float, y: float):
  embed = discord.Embed(title="Answer: ", description=x*y, color=5763719)
  embed.set_footer(text="Created by Raishu")
  await ctx.send(embed=embed)

@client.command()
async def div(ctx, x: float, y: float):
  embed = discord.Embed(title="Answer: ", description=x/y, color=5763719)
  embed.set_footer(text="Created by Raishu")
  await ctx.send(embed=embed)

@client.command()
async def mod(ctx, x: float, y: float):
  embed = discord.Embed(title="Answer: ", description=x%y, color=5763719)
  embed.set_footer(text="Created by Raishu")
  await ctx.send(embed=embed)

@client.command()
async def sqrt(ctx, x: float):
  embed = discord.Embed(title="Answer: ", description=math.sqrt(x), color=5763719)
  embed.set_footer(text="Created by Raishu")
  await ctx.send(embed=embed)

@client.command()
async def exp(ctx, x: int, y: int):
  embed = discord.Embed(title="Answer: ", description=x**y, color=5763719)
  embed.set_footer(text="Created by Raishu")
  await ctx.send(embed=embed)
keep_alive()
client.run(os.getenv('147178'))
