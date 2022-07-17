import guilded
from guilded.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.command()
async def ping(ctx):
    await ctx.send('pong!')

bot.run("ur token")