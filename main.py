from discord.ext import commands
import logging
import os
from pathlib import Path

cwd = Path(__file__).parents[0]
cwd = str(cwd)

bot = commands.Bot(command_prefix = "$", case_insensitive = False)
bot.config_token = os.getenv('TOKEN')
logging.basicConfig(level = logging.INFO)

@bot.command()
async def hi(ctx):
  await ctx.send(f"Hi {ctx.author.name}!")

@bot.command()
async def echo(ctx, *, message = None):
  message = message or "Please provide the message to be repeated."
  await ctx.send(message)

'''@bot.event
async def on_command_error(ctx, error):
  ignored = (commands.CommandNotFound, commands.UserInputError)
  if isinstance(error, ignored):
    return '''

if __name__ == '__main__':
  for file in os.listdir(cwd + '/cogs'):
    if file.endswith(".py") and not file.startswith("_"):
      bot.load_extension(f"cogs.{file[:-3]}")

bot.run(bot.config_token)
