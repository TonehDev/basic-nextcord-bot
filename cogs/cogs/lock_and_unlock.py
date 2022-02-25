import nextcord
from nextcord.ext import commands

class Lock(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command(aliases=["lock", "lockchannel"], brief="Lock a channel")
  @commands.has_permissions(manage_channels = True)
  async def lockdown(self, ctx, *, reason = "No reason provided."):
      await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False)
      embed = nextcord.Embed(
        description = f"{ctx.channel.mention} has been locked!\nReason: ``{reason}``",
        color = nextcord.Color.green()
      )
      await ctx.send(embed=embed)

  @commands.command(brief="Lock a channel")
  @commands.has_permissions(manage_channels = True)
  async def unlock(self, ctx):
    await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)
    embed = nextcord.Embed(
      description = f"{ctx.channel.mention} has been unlocked!",
      color = nextcord.Color.green()
    )
    await ctx.send(embed=embed)

  # Error Handling
  
  @lockdown.error
  async def lockdown_error(self, ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
      embed = nextcord.Embed(
          title = "Invalid Syntax",
          description = "``<> Required, [] Optional``",
          color = nextcord.Color.red()
      )
      embed.add_field(name = "Usage", value = "``.lock``", inline = False)
      embed.add_field(name = "Example", value = "``.lock``", inline = False)
      await ctx.send(embed=embed)

    elif isinstance(error, commands.MissingPermissions):
      embed = nextcord.Embed(
        description = "You are missing the ``MANAGE CHANNELS`` permission.",
        color = nextcord.Color.red()
      )
      await ctx.send(embed=embed)

  @unlock.error
  async def unlock_error(self, ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
      embed = nextcord.Embed(
          title = "Invalid Syntax",
          description = "``<> Required, [] Optional``",
          color = nextcord.Color.red()
      )
      embed.add_field(name = "Usage", value = "``.unlock``", inline = False)
      embed.add_field(name = "Example", value = "``.unlock``", inline = False)
      await ctx.send(embed=embed)

    elif isinstance(error, commands.MissingPermissions):
      embed = nextcord.Embed(
        description = "You are missing the ``MANAGE CHANNELS`` permission.",
        color = nextcord.Color.red()
      )
      await ctx.send(embed=embed)

def setup(client):
  client.add_cog(Lock(client))