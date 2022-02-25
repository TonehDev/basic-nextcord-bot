import nextcord
from nextcord.ext import commands 

class Nickname(commands.Cog):
    def __init__(self, client):
        self.client = client 

    @commands.command(aliases=["nick", "nn"], brief="Nick a member")
    @commands.has_permissions(manage_nicknames = True)
    async def nickname(self, ctx, nick, *, member : nextcord.Member):
        await member.edit(nick=nick)
        embed = nextcord.Embed(
            description = f"Successfully changed {member.mention}'s nickname to {nick}!",
            color = nextcord.Color.blue()
        )
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Nickname(client))