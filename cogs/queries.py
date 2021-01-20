from bs4 import BeautifulSoup
import discord
from discord.ext import commands
import requests


class Queries(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def tcs(self, ctx):
        links = []
        query = "+".join(ctx.message.content.split()[2:])
        if not query:
            await ctx.send("Make sure to enter a search query.")
            return

        page = requests.get("https://www.thecubicle.com/search?type=product&q=" + query)
        soup = BeautifulSoup(page.content, 'html.parser')
        
        try:
            await ctx.send("https://www.thecubicle.com/" + soup.find('a', class_='product-grid-item')['href'])
        except TypeError:
            await ctx.send("No results found...")

    @commands.command()
    async def scss(self, ctx):
        links = []
        query = "+".join(ctx.message.content.split()[2:])
        if not query:
            await ctx.send("Make sure to enter a search query.")
            return

        page = requests.get("https://www.speedcubeshop.com/search?type=product&q=" + query)
        soup = BeautifulSoup(page.content, 'html.parser')
        
        try:
            await ctx.send("https://www.speedcubeshop.com/" + soup.find('a', class_='product-title')['href'])
        except TypeError:
            await ctx.send("No results found...")

    @commands.command()
    async def wcaid(self, ctx):
        name = "+".join(ctx.message.content.split()[2:])
        if not name:
            await ctx.send("Be sure to enter a name to search up")
        else:
            url = ("https://www.worldcubeassociation.org/search?q=" + str(name)).replace(" ","%20")
            page = requests.get(url)

            soup = BeautifulSoup(page.content, 'html.parser')

            try:
                query = soup.find("table",{"class":"table table-nonfluid table-vertical-align-middle"}).a["href"]
                await ctx.send("https://www.worldcubeassociation.org" + query)
            except:
                await ctx.send("No results found...")


def setup(client):
    client.add_cog(Queries(client))

