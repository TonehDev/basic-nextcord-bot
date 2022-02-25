import nextcord
from nextcord.ext import commands
import random
import datetime

class HornyRate(commands.Cog):
    
    def __init__(self, client):
        self.client = client

    @commands.command(brief="How horny are you?")
    async def horny(self, ctx, member : nextcord.Member = None):
        embed = nextcord.Embed(
            description = f"{member.mention} is **{random.randint(101)}%** horny!",
            timestamp = datetime.utcnow(),
            color = nextcord.Color.random()
        )
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(HornyRate(client))