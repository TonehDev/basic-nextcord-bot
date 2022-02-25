import nextcord
from nextcord.ext import commands
import random
import datetime

class SusRate(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(brief="How sus are you?")
    async def sus(self, ctx, member : nextcord.Member = None):
        if member == None:
            member = ctx.author
        embed = nextcord.Embed(
            description = f"{member.mention} is **{random.randint(0, 100)}%** sus!",
            timestamp = datetime.utcnow(),
            color = nextcord.Color.random()
        )
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(SusRate(client))