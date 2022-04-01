import nextcord #pip install nextcord
from nextcord.ext import commands
import os #pip install os

bot  = commands.Bot(command_prefix = "your desired prefix")

@bot.command(brief="Load a command")
@commands.is_owner() #checks if the user owns the application
async def load(ctx, extension):
  bot.load_extension(f'cogs.{extension}') #loads cog

  embed = nextcord.Embed(
    description = f"Loaded ``{extension}`` successfully",
    color = nextcord.Color.red()
  )

  await ctx.send(embed=embed)

@bot.command(brief="Unload a command")
@commands.is_owner()
async def unload(ctx, extension):
  bot.unload_extension(f'cogs.{extension}')

  embed = nextcord.Embed(
    description = f"Unloaded ``{extension}`` successfully",
    color = nextcord.Color.red()
  )

  await ctx.send(embed=embed)

@bot.command(brief="Reload a command")
@commands.is_owner()
async def reload(ctx, extension):
  bot.unload_extension(f'cogs.{extension}')
  bot.load_extension(f'cogs.{extension}')

  embed = nextcord.Embed(
    description = f"Reloaded ``{extension}`` successfully",
    color = nextcord.Color.red()
  )

  await ctx.send(embed=embed)

for filename in os.listdir('./cogs'):
  if filename.endswith('.py'):
    bot.load_extension(f'cogs.{filename[:-3]}')

bot.run("replace this message with your bot token")

# A simple Discord bot base made in Python by Toneh#3391 on Discord