import nextcord
from nextcord.ext import commands

class NCVersion(commands.Cog):
    def __init__(self, client):
        self.client = client 

    @commands.command(aliases=["ncv"], brief="Displays Nextcord version")
    async def nextcord(self, ctx):
        embed = nextcord.Embed(
            description = f"Nextcord is currently on version ``{nextcord.__version__}``",
            color = nextcord.Color.yellow()
        )
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(NCVersion(client))