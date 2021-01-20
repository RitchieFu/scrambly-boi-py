import asyncio
import discord
from discord.ext import commands
from pyTwistyScrambler import scrambler333, scrambler222, scrambler444, scrambler555, pyraminxScrambler,scrambler666,scrambler777,megaminxScrambler,squareOneScrambler,skewbScrambler,clockScrambler
from clockimage import *
from megaimage import *
from pyraminximage import *
from scrambleupdate import *
from skewbimage import *
from squareoneimage import *


class ScrambleImages(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["pyra", "pyraminx", "mega", "megaminx", "skoob", "skewb", "sq1", "squareone", "squan", "cloncc", "clock"])
    async def nonNXN(self, ctx):

        puzzle = ctx.message.content.split()[1]

        scrambleGen = {
            "pyra": (pyraminxScrambler.get_WCA_scramble, pyraimage), 
            "pyraminx": (pyraminxScrambler.get_WCA_scramble, pyraimage), 
            "mega": (megaminxScrambler.get_WCA_scramble, megaimage), 
            "megaminx": (megaminxScrambler.get_WCA_scramble, megaimage), 
            "skoob": (skewbScrambler.get_WCA_scramble, skewbimage), 
            "skewb": (skewbScrambler.get_WCA_scramble, skewbimage),
            "sq1": (squareOneScrambler.get_WCA_scramble, squanimage), 
            "squareone": (squareOneScrambler.get_WCA_scramble, squanimage), 
            "squan": (squareOneScrambler.get_WCA_scramble, squanimage), 
            "cloncc": (clockScrambler.get_WCA_scramble, clockimage), 
            "clock": (clockScrambler.get_WCA_scramble, clockimage)
        }

        scramble = scrambleGen[puzzle][0]()

        msg = await ctx.send(scramble)
        await msg.add_reaction('👀') 

        def check(reaction, user):
            return user == ctx.message.author and str(reaction.emoji) == '👀' and reaction.message.id == msg.id

        try:
            reaction, user = await self.client.wait_for('reaction_add', timeout=15, check=check)
        except asyncio.TimeoutError:
            await msg.clear_reactions()
        else:
            file = scrambleGen[puzzle][1](scramble)
            file.save("scramble.png")
            await ctx.send(file = discord.File("scramble.png"))
            await msg.clear_reactions()

    @commands.command(aliases=['2', '2x2', '3', '3x3', '4', '4x4', '5', '5x5', '6', '6x6', '7', '7x7'])
    async def _xyz(self, ctx):
        layers = ctx.message.content.split()[1][0]

        scrambleGen = {
            "2": scrambler222.get_WCA_scramble, 
            "3": scrambler333.get_WCA_scramble, 
            "4": scrambler444.get_WCA_scramble, 
            "5": scrambler555.get_WCA_scramble, 
            "6": scrambler666.get_WCA_scramble, 
            "7": scrambler777.get_WCA_scramble, 
        }

        scramble = scrambleGen[layers]()

        msg = await ctx.send(scramble)
        await msg.add_reaction('👀') 

        def check(reaction, user):
            return user == ctx.message.author and str(reaction.emoji) == '👀' and reaction.message.id == msg.id

        try:
            reaction, user = await self.client.wait_for('reaction_add', timeout=15, check=check)
        except asyncio.TimeoutError:
            await msg.clear_reactions()
        else:
            file = scrambleimage(int(layers), scramble)
            file.save("scramble.png")
            await ctx.send(file = discord.File("scramble.png"))
            await msg.clear_reactions()


def setup(client):
    client.add_cog(ScrambleImages(client))

