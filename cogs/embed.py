import nextcord
from nextcord.ext import commands

class CustomEmbed(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command(brief="Send a custom embed")
  async def embed(self, ctx, *, msg):
    embed = nextcord.Embed(
      description = f"{msg}",
      color = nextcord.Color.random()
    )
    await ctx.send(embed=embed)

  # Error Handling
  @embed.error
  async def embed_error(self, ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
      embed = nextcord.Embed(
        title = "Invalid Syntax",
        description = "``<> Required, [] Optional``",
        color = nextcord.Color.red()
      )
      embed.add_field(name = "Usage", value = "``.embed <description>``", inline = False)
      embed.add_field(name = "Example", value = "``.embed Damn dude, cats do be amazing``", inline = False)
      await ctx.send(embed=embed)

def setup(client):
  client.add_cog(CustomEmbed(client))