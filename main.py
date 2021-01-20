import discord
from discord.ext import commands
from dotenv import load_dotenv
from scrambles import *
import keep_alive
import kociemba
import os
from pyTwistyScrambler import scrambler333, scrambler444, scrambler555
import asyncio
import re
import sqlite3

load_dotenv()
bot = commands.Bot(command_prefix = ['plz ', 'Plz ', 'PLZ ']) 
bot.remove_command('help')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

scrambleCommands = {
    'plz 3bld': scrambler333.get_3BLD_scramble,
    'plz 4bld': scrambler444.get_4BLD_scramble,
    'plz 5bld': scrambler555.get_5BLD_scramble,
}


keep_alive.keep_alive()
bot.run(os.getenv("TOKEN"))