import discord
from discord.ext import commands
import math
import os
from keep_alive import keep_alive

bot = commands.Bot(command_prefix='%')

@bot.event 
async def on_ready():
  print('You are now logged in as {0.user}'.format(bot))

@bot.event
async def on_message(message):
  if message.content.startswith('%author'):
    await message.channel.send('Raishu')

  if message.content.startswith('%commands'):
    await message.channel.send('Here''s the list of commands: \n%mathadd \n%mathsub \n%mathmul \n%mathdiv \n%mathmod \n%mathsqrt \n%mathrandom \n%author \n%commands \nInsert first and second number respectively. ex. %mathadd 1 2')

@bot.command()
async def add(ctx, x: float, y: float):
  res = x + y
  await ctx.send(res)

@bot.command()
async def sub(ctx, x: float, y: float):
  res = (x - y)
  await ctx.send(res)

@bot.command()
async def mul(ctx, x: float, y: float):
  res = (x * y)
  await ctx.send(res)

@bot.command()
async def div(ctx, x: float, y: float):
  res = (x / y)
  await ctx.send(res)

@bot.command()
async def mod(ctx, x: float, y: float):
  res = (x % y)
  await ctx.send(res)

@bot.command()
async def sqrt(ctx, x: float):
  res = (math.sqrt(x))
  await ctx.send(res)

keep_alive()
bot.run(os.getenv('')) #insert getenv key