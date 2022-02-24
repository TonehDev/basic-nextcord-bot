import nextcord #pip install nextcord
from nextcord.ext import commands
import os #pip install os

bot  = commands.Bot(command_prefix = "!")
testingServerID = 946310802250530846

@bot.command(brief="Load a command")
async def load(ctx, extension):
  bot.load_extension(f'cogs.{extension}')
  embed = nextcord.Embed(
    title = "Loaded 1 command",
    description = "Successfully loaded 1 command!",
    color = nextcord.Color.blurple()
  )
  await ctx.send(embed=embed)

@bot.command(brief="Unload a command")
async def unload(ctx, extension):
  bot.unload_extension(f'cogs.{extension}')
  embed = nextcord.Embed(
    title = "Unloaded 1 command",
    description = "Successfully unloaded 1 command!",
    color = nextcord.Color.blurple()
  )
  await ctx.send(embed=embed)

@bot.command(brief="Reload a command")
async def reload(ctx, extension):
  bot.unload_extension(f'cogs.{extension}')
  bot.load_extension(f'cogs.{extension}')
  embed = nextcord.Embed(
    title = "Reloaded 1 command",
    description = "Successfully reloaded 1 command!",
    color = nextcord.Color.blurple()
  )
  await ctx.send(embed=embed)

for filename in os.listdir('./cogs'):
  if filename.endswith('.py'):
    bot.load_extension(f'cogs.{filename[:-3]}')
  
bot.run('insert your bot token here')

# A simple Discord bot base made in Python by Toneh#3391 on Discord