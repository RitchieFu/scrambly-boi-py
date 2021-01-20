import discord
from discord.ext import commands
from scrambles import scramble1, input3
from pyTwistyScrambler import scrambler333

acceptedmoves = ['U', 'D', 'R', 'L', 'F', 'B']

class Misc(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def test(self, ctx):
        await ctx.send("Python: <:peponice:693014841614663700>")

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

    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.guild)
    async def noob3(self, ctx):
        noobdict = {
            'U':'top', 'D':'bottom', 'R':'right', 'L':'left', 'F':'front', 'B':'back'
        }

        memestring = []
        msg = scrambler333.get_WCA_scramble()
        newmsg = msg.replace(' ','')
        m = len(newmsg) - 1
        while m > -1: 
            if newmsg[m] == "'":
                memestring.append('turn the ' + noobdict[newmsg[m-1]] + ' face counterclockwise by 90 degrees')
                m -= 2
            elif newmsg[m] == "2":
                memestring.append('turn the ' + noobdict[newmsg[m-1]] + ' face by 180 degrees')
                m -= 2
            elif newmsg[m] in acceptedmoves:
                memestring.append('turn the ' + noobdict[newmsg[m]] + ' face clockwise by 90 degrees')
                m -= 1
            else:
                return

        memestring = memestring[::-1]
        n = await ctx.send(', '.join(memestring))
        
        await n.add_reaction('🙃') 

        def check(reaction, user):
            return user == ctx.author and str(reaction.emoji) == '🙃'

        try:
            reaction, user = await self.client.wait_for('reaction_add', timeout=10, check=check)
        except:
            await n.clear_reactions()
        else:
            await ctx.send(input3(msg.split()))
            await n.clear_reactions()

    
    @commands.command(pass_context=True)
    async def show(self, ctx):
        formattedstr = []
        removedslash = []
        msg = ctx.message.content[9:]

        for line in msg.splitlines():
            slashes = [i for i in range(len(line)) if line.startswith('//', i)]
            if len(slashes) > 0:
                r = line.replace(line[slashes[0]:],'')
                removedslash.append(r)
            else:
                removedslash.append(line)

        msg = ' '.join(removedslash)
        msg = msg.replace("’", "'").replace("(", '').replace(")", '').replace(' ', '')
        msg = msg.replace('Rw','r').replace("Lw",'l').replace("Uw",'u').replace("Dw",'d').replace("Fw",'f').replace("Bw",'b')
        if len(msg) > 0:
            m = len(msg) - 1
            while m > -1: 
                if msg[m] == "'":
                    if msg[m-1] == "2":
                        formattedstr.append(msg[m-2] + msg[m-1] + msg[m])
                        m -= 3
                    elif msg[m-1] in acceptedmoves:
                        formattedstr.append(msg[m-1] + msg[m])
                        m -= 2
                    else:
                        await ctx.send('invalid notation dud')
                        return
                elif msg[m] == "2":
                    if msg[m-1] in acceptedmoves:
                        formattedstr.append(msg[m-1] + msg[m])
                        m -= 2
                    elif msg[m-1] == 'w':
                        await ctx.send('use lowercase notation for wide moves plz')
                        return
                    else:
                        await ctx.send('invalid notation dud')
                        return
                elif msg[m] in acceptedmoves:
                    formattedstr.append(msg[m])
                    m -= 1
                else:
                    await ctx.send('invalid notation dud')
                    return
        else: 
            await ctx.send("nothing to show bruh (e.g, \"plz show R U R' U'\")")
            return

        msg = formattedstr[::-1]
        msg.append(' ')
        base = await ctx.send(' '.join(msg) + '\n' + input3([]))
        await base.add_reaction('👀')
        
        def check(reaction, user):
            return user == ctx.author and str(reaction.emoji) == '👀'

        movecounter = 1
        for move in msg:
            try:
                reaction, user = await self.client.wait_for('reaction_add', timeout = 1, check=check)
            except:
                await base.edit(content= str(' '.join(msg[:movecounter-1])) + ' ' + "**{}**".format(''.join(str(msg[movecounter-1]))) + ' ' + str(' '.join(msg[movecounter:])) + ' ' + '\n' + input3(msg[:movecounter]))
                movecounter += 1
            else:
                await base.edit(content = ' '.join(msg) + '\n' + input3(msg))
                await base.clear_reactions()
                return

        await base.clear_reactions()

    
    @commands.command(pass_context=True)
    async def setup(self, ctx):
        formattedstr = []
        msg = ctx.message.content[10:]
        msg = msg.replace("’", "'").replace("(", '').replace(")", '').replace(' ', '')

        if len(msg) > 0:
            m = len(msg) - 1
            while m > -1: 
                if msg[m] == "'":
                    if msg[m-1] == "2":
                        formattedstr.append(msg[m-2] + msg[m-1])
                        m -= 3
                    elif msg[m-1] in acceptedmoves:
                        formattedstr.append(msg[m-1])
                        m -= 2
                    else:
                        await ctx.send('invalid notation dud')
                        return
                elif msg[m] == "2":
                    formattedstr.append(msg[m-1] + msg[m])
                    m -= 2
                elif msg[m] in acceptedmoves:
                    formattedstr.append(msg[m] + "'")
                    m -= 1
                else:
                    await ctx.send('invalid notation dud')
                    return
        else: 
            await ctx.send('nothing to show bruh')
            return

        msg = formattedstr
        await ctx.send(' '.join(msg))

def setup(client):
    client.add_cog(Misc(client))

