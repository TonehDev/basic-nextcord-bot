import nextcord 
from nextcord.ext import commands 
import random 

class RollDice(commands.Cog):
    def __init__(self, client):
        self.client = client 

    @commands.command(aliases=["rd", "dice", "roll"])
    async def rolldice(self, ctx):
        dice_sides = [
            "1",
            "2",
            "3",
            "4",
            "5",
            "6"
        ]
        embed = nextcord.Embed(
            description = f"The dice was rolled and landed on {random.choice(dice_sides)}",
            color = nextcord.Color.random()
        )
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(RollDice(client))