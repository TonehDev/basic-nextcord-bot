import nextcord
from nextcord.ext import commands

class Links(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command(brief="All links related")
  async def links(self, ctx):
    embed = nextcord.Embed(
      title = "Links",
      description = "[Text](https://example-link.com/)",
      color = nextcord.Color.blurple()
    )
    await ctx.send(embed=embed)

def setup(client):
  client.add_cog(Links(client))