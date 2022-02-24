import nextcord
from nextcord.ext import commands

class Start(commands.Cog):

  def __init__(self, client):
    self.client = client
  
  @commands.Cog.listener()
  async def on_ready(self):
    await self.client.change_presence(activity=nextcord.Activity(type = nextcord.ActivityType.watching, name = f"{len(self.client.guilds)} servers | .help"))
    print("Ready.")

  @commands.Cog.listener()
  async def on_command_error(self, ctx, error):
    if isinstance(error, commands.CommandNotFound):
      embed = nextcord.Embed(
        description = f"No command named ``{ctx.message.content}`` found.",
        color = nextcord.Color.red()
      )
      await ctx.send(embed=embed)

def setup(client):
  client.add_cog(Start(client))