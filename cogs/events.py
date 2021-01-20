import discord
from discord.ext import commands
from discord.ext.commands import CommandNotFound


class Events(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Bot is online.')

    @commands.Cog.listener()
    async def on_message(self, message):

        if message.author.id == self.client.user.id:
            return

        await self.client.process_commands(message)

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, CommandNotFound): return
        raise error


def setup(client):
    client.add_cog(Events(client))

