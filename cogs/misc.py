import discord
from discord.ext import commands
from scrambles import scramble1

class Misc(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def test(self, ctx):
        await ctx.send("Python: <:peponice:693014841614663700>")

    # @commands.command()
    # async def users(self, ctx):
    #     memberCount = 0
    #     for guild in self.client.guilds:
    #         memberCount += len(guild.members)
    #     await ctx.send("Total users: " + str(memberCount))

    @commands.command()
    async def avg(self, ctx):
        times = ctx.message.content.split(' ')[2:]
        times = [int(i) for i in times]
        average = (sum(times) - min(times) - max(times)) / (len(times) - 2)
        await ctx.send("{:.2f}".format(float(average)))
    
    @commands.command(aliases=['1','1x1'])
    async def _1(self, ctx, amount: int = 1):
        if amount > 5: amount = 5
        for i in range(amount):
            await ctx.send(scramble1()) 

def setup(client):
    client.add_cog(Misc(client))

