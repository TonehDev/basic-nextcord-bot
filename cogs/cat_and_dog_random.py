import nextcord
from nextcord.ext import commands 
import aiohttp

class CatAndDog(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command(brief="Sends a random cat image.")
  async def cat(self, ctx):
      async with aiohttp.ClientSession() as cs:
        async with cs.get("https://aws.random.cat/meow") as r:
          data = await r.json()

          embed = nextcord.Embed(
            title = "Meowwww!",
            color = nextcord.Color.random()
          )
          embed.set_image(url = data['file'])
          await ctx.send(embed=embed)

  @commands.command(brief="Sends a random dog image.")
  async def dog(self, ctx):
      async with aiohttp.ClientSession() as cs:
        async with cs.get("https://random.dog/woof.json") as r:
          data = await r.json()

          embed = nextcord.Embed(
            title = "Woof woof...",
            color = nextcord.Color.random()
          )
          embed.set_image(url = data['url'])
          await ctx.send(embed=embed)

def setup(client):
  client.add_cog(CatAndDog(client))