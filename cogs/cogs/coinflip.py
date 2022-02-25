import nextcord
from nextcord.ext import commands 
import random

class CoinFlip(commands.Cog):
    def __init__(self, client):
        self.client = client 

    @commands.Cog(aliases=["cf", "flip", "coin"], brief="Flip a coin")
    async def coinflip(self, ctx):
        sides = [
            "Tails",
            "Heads"
        ]
        embed = nextcord.Embed(
            description = f"The coin landed on **{random.choice(sides)}**!",
            color = nextcord.Color.random()
        )
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(CoinFlip(client))