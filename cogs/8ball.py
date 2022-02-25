import nextcord
from nextcord.ext import commands
import random
import datetime

class Ask(commands.Cog):
  def __init__(self, client):
    self.client = client
    
  @commands.command(aliases=["8ball", "ask"], brief="Ask the 8ball a question")
  async def _8ball(self, ctx, *, question):
      responses = [
      "It is certain.",
      "It is decidedly so.",
      "Without a doubt.",
      "Yes - definitely.",
      "You may rely on it.",
      "As I see it, yes.",
      "Most likely.",
      "Outlook good.",
      "Yes.",
      "Signs point to yes.",
      "Reply hazy, try again.",
      "Ask again later.",
      "Better not tell you now.",
      "Cannot predict now.",
      "Concentrate and ask again.",
      "Don't count on it.",
      "My reply is no.",
      "My sources say no.",
      "Outlook not so good.",
      "Very doubtful."
    ]
      embed = nextcord.Embed(
        timestamp = datetime.utcnow(),
        color = nextcord.Color.random()
      )
      embed.add_field(name = "Question", value = f"{question}", inline = False)
      embed.add_field(name = "Answer", value = f"{random.choice(responses)}", inline = False)
      await ctx.send(embed=embed)

def setup(client):
  client.add_cog(Ask(client))