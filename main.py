import os

from discord.ext import commands
from pymongo import MongoClient

from utils.functions import get_prefix
from utils.pagination import Embed

bot = commands.Bot(
  case_insensitive=True,
  command_prefix=get_prefix
)

client = MongoClient(os.getenv("MongoDB"))
economy = client["myFirstDatabase"]["users"]

@bot.event
async def on_ready():
  print("Ready!")

  bot.Embed = Embed
  bot.economy = economy
  bot.menus = {}

for filename in os.listdir("./cogs"):
  if filename.endswith(".py"):
    bot.load_extension(f"cogs.{filename[:-3]}")

bot.run(os.getenv("TOKEN"))