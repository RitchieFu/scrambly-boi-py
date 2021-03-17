import discord
from discord.ext import commands
from clockimage import *
from megaimage import *
from pyraminximage import *
from scrambleupdate import *
from skewbimage import *
from squareoneimage import *



class ShowScramble(commands.Cog):
    def __init__(self, client):
        self.client = client

    
    @commands.command()
    async def show(self, ctx, puzzle):

        puzzles = ["pyra", "pyraminx", "mega", "megaminx", "skoob", "skewb", "sq1", "squareone", "squan", "cloncc", "clock", '2', '2x2', '3', '3x3', '4', '4x4', '5', '5x5', '6', '6x6', '7', '7x7']

        scrambleGen = {
            "pyra": pyraimage, "pyraminx": pyraimage, 
            "mega": megaimage, "megaminx": megaimage, 
            "skoob": skewbimage, "skewb": skewbimage,
            "sq1": squanimage, "squareone": squanimage, "squan": squanimage, 
            "cloncc": clockimage, "clock": clockimage,
        }

        if puzzle in puzzles:
            if any(i.isdigit() for i in puzzle):
                layers = puzzle[0]
            else:
                layers = False
        else:
            return

        scramble = " ".join(ctx.message.content.split()[3:])

        try:
            if layers:
                file = scrambleimage(int(layers), scramble)
            elif layers == False:
                file = scrambleGen[puzzle](scramble)
            file.save("showscramble.png")
            await ctx.send(scramble)
            await ctx.send(file = discord.File("showscramble.png"))
        except:
            await ctx.send("something went wrong")


def setup(client):
    client.add_cog(ShowScramble(client))
