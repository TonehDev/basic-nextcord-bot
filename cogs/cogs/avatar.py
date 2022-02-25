import nextcord
from nextcord.ext import commands

class Avatar(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command(aliases=["av"], brief="Sends your or another member's avatar")
  async def avatar(self, ctx, *, member : nextcord.Member = None):
      if member == None:
        member = ctx.author
      embed = nextcord.Embed(
        description = f"**{member}**'s avatar", 
        color = nextcord.Color.blue()
      )
      embed.set_image(url = member.avatar.url)
      await ctx.send(embed=embed)

def setup(client):
  client.add_cog(Avatar(client))