import discord
from discord.ext import commands
from discord.ext.commands import CommandNotFound
from scrambles import *
import random

emotes = [
    '🇺','<:redU:718597576122826803>',
    '🇩','<:redD:718598898410717204>',
    '🇷','<:redR:718598898561712248>',
    '🇱','<:redL:718598898507055124>',
    '🇫','<:redF:718598897970446357>',
    '🇧','<:redB:718598898301665403>',
    '⬆️','⬇️','⬅️','➡️','↩️','↪️','🔄'
]

reactiondict = {
    '🇺':'U', '🇩':'D', '🇷':'R', '🇱':'L', '🇫':'F', '🇧':'B',
    '<:redU:718597576122826803>':"U'", '<:redD:718598898410717204>':"D'",
    '<:redR:718598898561712248>':"R'", '<:redL:718598898507055124>':"L'",
    '<:redF:718598897970446357>':"F'", '<:redB:718598898301665403>':"B'",
    '⬆️':'x','⬇️':"x'",'⬅️':'y','➡️':"y'",'↩️':'z','↪️':"z'"
}


class VirtualCubes(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def bro(self, ctx):
        await ctx.send("bro")
        
    @commands.command()
    async def solve2(self, ctx):
        print('command ran')
        w = white
        y = yello
        g = green
        b = bluee
        r = reeed
        o = orang

        themoves = ['']
        while len(themoves) < 10:
                themoves.append(random.choice(URF))
                if themoves[-1] == themoves[-2]:
                    del themoves[-1]

        for t in URF:
                if t not in themoves:
                    themoves[random.randint(1,9)] = t

        themoves = [item.replace('_', str(random.choice(specification))) for item in themoves]
        del themoves[0]

        message = await ctx.send(scramble2(themoves))

        for e in emotes[:18]:
            await message.add_reaction(e)

        def check(reaction, user):
                return (reaction.message.id == message.id) and (user.id == ctx.author.id) and (str(reaction) in emotes)

        orientations = ["x2 z z z", "x z z z", "x' z z z", "y z z z", "y' z z z", "z z z"]

        while True:
            try:
                reaction, user = await self.client.wait_for('reaction_add', check=check, timeout=300)
            except:
                await message.clear_reactions()
                return

            if str(reaction):
                try:
                    themoves.append(reactiondict[str(reaction)])
                    await message.remove_reaction(str(reaction), user)
                except KeyError:
                    return

            checklist = themoves.copy()
            checkmessage = scramble2(checklist).replace("_","").replace("\n","").replace(" ","")  
            if checkmessage == w+w+w+w+o+o+g+g+r+r+b+b+o+o+g+g+r+r+b+b+y+y+y+y:
                await message.edit(content="POGGERS YOU SOLVED THE CUBE!!" + "\n" + scramble2(themoves))
                await message.clear_reactions()
                return

            for moves in orientations:
                for move in moves.split():
                    checklist.append(move)
                    checkmessage = scramble2(checklist).replace("_","").replace("\n","").replace(" ","")  
                    if checkmessage == w+w+w+w+o+o+g+g+r+r+b+b+o+o+g+g+r+r+b+b+y+y+y+y:
                        await message.edit(content="POGGERS YOU SOLVED THE CUBE!!" + "\n" + scramble2(themoves))
                        await message.clear_reactions()
                        return
                checklist = themoves.copy()

            await message.edit(content=str(' '.join(themoves[9:]) + '\n' + scramble2(themoves)))

    @commands.command()
    async def sandbox(self, ctx):
        # moves inputted by the user through reactions
        themoves = []
        message = await ctx.send(input3(themoves))

        # adds reactions
        [await message.add_reaction(e) for e in emotes]

        def check(reaction, user):
            return (reaction.message.id == message.id) and (user.id == ctx.author.id) and (str(reaction) in emotes)

        # constantly checks if a reaction has been added by the user who invoked the command
        while True:
            try:
                reaction, user = await self.client.wait_for('reaction_add', check=check, timeout=300) # 5 min inactivity
            except:
                await message.clear_reactions()
            return
            
            if str(reaction):
                try:
                    themoves.append(reactiondict[str(reaction)]) 
                    await message.remove_reaction(str(reaction), user)
                except KeyError:
                    # had to account for the reset reaction this way because it has to clear the list of moves
                    # this is why this emote is not in the dictionary 
                    if str(reaction) == '🔄':
                        themoves = []
                        await message.remove_reaction('🔄', user)
                    else:
                        return

            await message.edit(content=' '.join(themoves) + '\n' + input3(themoves))

    @commands.command()
    async def solve3(self, ctx):
        print('command ran')

        w = white
        y = yello
        g = green
        b = bluee
        r = reeed
        o = orang
        # very epic 3x3 scrambler (random moves) that is pretty compact and gets the job done
        themoves = ['']
        while len(themoves) < 20:
            gen = random.choice(UD + RL + FB)
            if gen != themoves[-1]: themoves.append(gen)
            for l in UDRLFB:
                if themoves[-1] in l and themoves[-2] in l and len(themoves) < 20:
                    themoves.append(random.choice([item for item in (UD + RL + FB) if item not in l]))
            themoves = [item.replace('_', str(random.choice(specification))) for item in themoves]
            del themoves[0]

        message = await ctx.send(input3(themoves))

        # adds all reactions except for the reset emote
        for e in emotes[:18]:
            await message.add_reaction(e)

        def check(reaction, user):
            return (reaction.message.id == message.id) and (user.id == ctx.author.id) and (str(reaction) in emotes)

        orientations = ["x2 z z z", "x z z z", "x' z z z", "y z z z", "y' z z z", "z z z"]

        while True:
            try:
                reaction, user = await self.client.wait_for('reaction_add', check=check, timeout=300)
            except:
                await message.clear_reactions()
            return

            if str(reaction):
                try:
                    themoves.append(reactiondict[str(reaction)])
                    await message.remove_reaction(str(reaction), user)
                except KeyError:
                    return

            checklist = themoves.copy()
            checkmessage = input3(checklist).replace("_","").replace("\n","").replace(" ","")
            
            if checkmessage == w+w+w+ w+w+w+ w+w+w+ o+o+o+ g+g+g+ r+r+r+ b+b+b+ o+o+o+ g+g+g+ r+r+r+ b+b+b+ o+o+o+ g+g+g+ r+r+r+ b+b+b+ y+y+y+ y+y+y+ y+y+y:
                await message.edit(content="POGGERS YOU SOLVED THE CUBE!!" + "\n" + input3(themoves))
                await message.clear_reactions()
                return  

            for moves in orientations:
                for move in moves.split():
                    checklist.append(move)
                    checkmessage = input3(checklist).replace("_","").replace("\n","").replace(" ","")  
                    if checkmessage == w+w+w+ w+w+w+ w+w+w+ o+o+o+ g+g+g+ r+r+r+ b+b+b+ o+o+o+ g+g+g+ r+r+r+ b+b+b+ o+o+o+ g+g+g+ r+r+r+ b+b+b+ y+y+y+ y+y+y+ y+y+y:
                        await message.edit(content="POGGERS YOU SOLVED THE CUBE!!" + "\n" + input3(themoves))
                        await message.clear_reactions()
                        return
            checklist = themoves.copy()

            await message.edit(content=str(' '.join(themoves[19:]) + '\n' + input3(themoves)))


def setup(client):
    client.add_cog(VirtualCubes(client))
