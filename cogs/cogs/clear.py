import nextcord
from nextcord.ext import commands

class Clear(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command(aliases=["purge"], brief="Clear a bundle of messages")
  @commands.has_permissions(manage_messages = True)
  async def clear(self, ctx, amount=2):
    await ctx.message.delete()
    await ctx.channel.purge(limit = amount)

  # Error Handling

  @clear.error
  async def clear_error(self, ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
      embed = nextcord.Embed(
          title = "Invalid Syntax",
          description = "``<> Required, [] Optional``",
          color = nextcord.Color.red()
      )
      embed.add_field(name = "Usage", value = "``.clear <msg_amount>``", inline = False)
      embed.add_field(name = "Example", value = "``.clear 5``", inline = False)
      await ctx.send(embed=embed)

    elif isinstance(error, commands.MissingPermissions):
      embed = nextcord.Embed(
        title = "No Permissions",
        description = "You are missing the ``MANAGE_MESSAGES`` permission.",
        color = nextcord.Color.red()
      )
      await ctx.send(embed=embed)

def setup(client):
  client.add_cog(Clear(client))