import nextcord
from nextcord.ext import commands
import random
import datetime

class GayRate(commands.Cog):

    def __init__(self, client):
        self.client = client 

    @commands.command(brief="How gay are you?")
    async def gay(self, ctx, member : nextcord.Member = None):
        if member == None:
            member = ctx.author
        embed = nextcord.Embed(
            description = f"{member.mention} is **{random.randint(0, 100)}%** gay!",
            timestamp = datetime.utcnow(),
            color = nextcord.Color.random()
        )
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(GayRate(client))