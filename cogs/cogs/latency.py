import nextcord
from nextcord.ext import commands

class Ping(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command(brief="Shows the client latency.")
  async def ping(self, ctx):
      embed = nextcord.Embed(
        title = "Pong!",
        color = nextcord.Color.blurple()
      )
      embed.add_field(name = "Latency", value = f"{round(self.client.latency * 1000)} ms")
      await ctx.send(embed=embed)

def setup(client):
  client.add_cog(Ping(client))