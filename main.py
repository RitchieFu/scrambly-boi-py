import discord
from discord.ext import commands
from dotenv import load_dotenv
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

noobdict = {
  'U':'top', 'D':'bottom', 'R':'right', 'L':'left', 'F':'front', 'B':'back'
}

scrambleCommands = {
    'plz 3bld': scrambler333.get_3BLD_scramble,
    'plz 4bld': scrambler444.get_4BLD_scramble,
    'plz 5bld': scrambler555.get_5BLD_scramble,
}

@bot.event
async def on_message(message):

    if message.author.id == bot.user.id:
        return
    await bot.process_commands(message)

    channel = message.channel
    messageSplit = message.content.lower().split()

    if message.author.id == bot.user.id:
        return

    try:
        scrambleCommands[(messageSplit[0] + ' ' + messageSplit[1])]
    except:
        return

    if len(messageSplit) > 2:
        amt = int(messageSplit[-1])
        if amt > 5: amt = 5
    else:
        amt = 1

    for i in range(amt):
        embed = discord.Embed(title = '', description = scrambleCommands[(messageSplit[0] + ' ' + messageSplit[1])](), color = 0x43a8ff)
        await channel.send(embed = embed)




@bot.command()
async def custom(ctx):

    msg = ctx.message.content.split()

    class Cuber:
        def __init__(self, id, corners, edges, CB, EB):
            self.id = id
            self.corners = corners
            self.edges = edges
            self.CB = CB
            self.EB = EB

    try:    
        cuber = Cuber(ctx.message.author.id, msg[2], msg[3], msg[4], msg[5])
    except IndexError:
        await ctx.send("Here is the format: **plz custom [letters for corners] [letters for edges] [corner buffer] [edge buffer]**\n_All elements need to be separated by a space. Do not include brackets like in the example._")
        return

    conn = sqlite3.connect('custom.db')

    c = conn.cursor()

    # c.execute("""CREATE TABLE cubers (
    #             id integer,
    #             cornerScheme text,
    #             edgeScheme text,
    #             cornerBufferTarget text,
    #             edgeBufferTarget text
    #             )""")

    def insert_cuber(cuber):
        with conn:
            c.execute("INSERT INTO cubers VALUES (?, ?, ?, ?, ?)", (cuber.id, cuber.corners, cuber.edges, cuber.CB, cuber.EB))
            conn.commit()

    def get_preferences(id):
        c.execute("SELECT * FROM cubers WHERE id=:id", {'id': id})
        return c.fetchone()

    def update_preferences(cuber):
        with conn:
            c.execute("""UPDATE cubers SET cornerScheme = ?, edgeScheme = ?, cornerBufferTarget = ?, edgeBufferTarget = ? WHERE id = ?""", (cuber.corners, cuber.edges, cuber.CB, cuber.EB, cuber.id))
            conn.commit()

    def validLetterScheme(letters):
        return letters.upper().isalpha() and len(letters) == 24 and len(set(letters)) == len(letters)
    
    def validCorners(buffer):
        return len(buffer) == 1 and buffer in cuber.corners

    def validEdges(buffer):
        return len(buffer) == 1 and buffer in cuber.edges
        
    errors = ["Error(s):"]

    if not validLetterScheme(cuber.corners) or not validLetterScheme(cuber.edges):
        errors.append("Letter schemes must contain 24 English letters and must not contain any repeats.")

    if not validCorners(cuber.CB) or not validEdges(cuber.EB):
        errors.append("Buffers must appear in their respective letter schemes.")

    if len(errors) > 1:
        await ctx.send('\n- '.join(errors))
    else:
        if get_preferences(ctx.message.author.id):          
            update_preferences(cuber)
        else:
            insert_cuber(cuber)
        await ctx.send("Your settings have been updated.")
    
    conn.close()


def get_preferences(id):  
    conn = sqlite3.connect('custom.db')
    c = conn.cursor()
    c.execute("SELECT * FROM cubers WHERE id = ?", (id,))
    return c.fetchone()
    conn.close()
    

@bot.command()
async def settings(ctx):
    pref = get_preferences(ctx.message.author.id)
    try:
        await ctx.send("**Corners**: {}\n**Edges**: {}\n**Corner Buffer**: {}\n**Edge Buffer**: {}".format(pref[1].upper(), pref[2].upper(), pref[3].upper(), pref[4].upper()))
    except:
        #await ctx.send('User not in database.')
        await ctx.send("**Corners**: ABCDEFGHIJKLMNOPQRSTUVWX\n**Edges**: ABCDEFGHIJKLMNOPQRSTUVWX\n**Corner Buffer**: A\n**Edge Buffer**: B")


@bot.command()
async def reset(ctx):

  def remove_cuber(id):
    conn = sqlite3.connect('custom.db')
    c = conn.cursor()
    with conn:
        c.execute("DELETE from cubers WHERE id = :id",
                  {'id': id})
    conn.commit()
    conn.close()

  if get_preferences(ctx.message.author.id):
    remove_cuber(ctx.message.author.id)
    await ctx.send("Your settings have been reset.")
  else:
    await ctx.send("User not in database.")


@bot.command()
async def memo(ctx):

    orientations = {
        12: "y",    13: "",     14: "y'",    15: "y2",
        21: "z' x", 23: "z'",   25: "z' x2", 26: "z' x",
        31: "z2 x", 32: "z y",  34: "z' y'", 36: "x'",
        41: "z x",  43: "z",    45: "z x2",  46: "z x'",
        51: "x",    52: "z' y", 54: "z y'",  56: "z2 x'",
        62: "z2 y", 63: "z2",   64: "z2 y'", 65: "x2"
    }

    translator = {
        12: "UFRBLD", 13: "ULFRBD", 14: "UBLFRD", 15: "URBLFD",
        21: "FULDRB", 23: "RUFDBL", 25: "LUBDFR", 26: "BURDLF",
        31: "FRULDB", 32: "LFUBDR", 34: "RBUFDL", 36: "BLURDF",
        41: "FDRULB", 43: "LDFUBR", 45: "RDBUFL", 46: "BDLURF",
        51: "FLDRUB", 52: "RFDBUL", 54: "LBDFUR", 56: "BRDLUF",
        62: "DFLBRU", 63: "DRFLBU", 64: "DBRFLU", 65: "DLBRFU"
    }

    try:
        moves = ((' '.join(ctx.message.content.split()[2:])).replace("Rw", 'r').replace(
            "Lw", 'l').replace("Uw", 'u').replace("Dw", 'd').replace("Fw", 'f').replace("Bw", 'b')).split()
    except IndexError:
        return

    finalO = moves[-1]
    finalOBool = False
    if finalO[0] == '-' and finalO.count('-') == 1:
        try:
            finalO = int(finalO.replace('-', '').replace('W', '1').replace('O', '2').replace(
                'G', '3').replace('R', '4').replace('B', '5').replace('Y', '6'))
        except ValueError:
            return

        finalOBool = True
        del moves[-1]

    try:
        returnedBLD3 = ''.join(bld3(moves))
    except KeyError:
        return

    topFront = int(returnedBLD3[4] + returnedBLD3[22])
    if not finalOBool:
        finalO = topFront

    try:
        tMoves = list(translator[finalO])
    except KeyError:
        return

    for rotation in orientations[topFront].split():
        moves.append(rotation)

    kSolve = kociemba.solve(''.join(cubestring(moves))).replace(' ', '')

    acceptedMoves = ['U', 'D', 'R', 'L', 'F', 'B']
    inversedString = []
    k = len(kSolve) - 1

    while k > -1:
        if kSolve[k] == "'":
            inversedString.append(kSolve[k-1])
            k -= 2
        elif kSolve[k] == "2":
            inversedString.append(kSolve[k-1] + kSolve[k])
            k -= 2
        elif kSolve[k] in acceptedMoves:
            inversedString.append(kSolve[k] + "'")
            k -= 1
        else:
            break
    
    inversedString = ' '.join(inversedString).translate(str.maketrans('ULFRBD', ''.join(tMoves)))
    newBLD3 = ''.join(bld3(inversedString.split()))
    allLetters = ''.join([i for i in newBLD3 if i.isalpha()])
    
    # Corners ----
    cCorrect = 'ABDCEFHGIJLKMNPOSTRQUVXW'
    cMemo = []
    cMsg = re.findall('([A-Z])', allLetters)
    cPriority = list('POMLNHTUCFBDISKVGJWXQ')
    cReplace = {
        0:(4,18), 4:(18,0), 18:(0,4), 
        1:(19,13), 19:(13,1), 13:(1,19),
        3:(12,9), 12:(9,3), 9:(3,12), 
        2:(8,5), 8:(5,2), 5:(2,8), 
        20:(7,10), 7:(10,20), 10:(20,7), 
        21:(11,14), 11:(14,21), 14:(21,11), 
        23:(15,17), 15:(17,23), 17:(23,15), 
        22:(16,6), 16:(6,22), 6:(22,16)
    }

    preferences = get_preferences(ctx.message.author.id)

    def toCorrectCornerString(corners):
        correctedString = [] 
        splitEveryFour = re.findall('....', corners)
        for substring in splitEveryFour:
            substring = substring[:2] + substring[-1] + substring[2]
            correctedString.append(substring)
        correctedString[4] = correctedString[4][::-1]
        return ''.join(correctedString)

    cBuffer1 = 0
    cBuffer2 = 4
    cBuffer3 = 18
    if preferences:
        correctCornerString = toCorrectCornerString(preferences[1])
        cBuffer1 = correctCornerString.index(preferences[3])
        cBuffer2 = cReplace[cBuffer1][0]
        cBuffer3 = cReplace[cBuffer1][1]

    def swapCorners(current):
        swap0 = cCorrect.index(current)
        swap1 = cReplace[swap0][0]
        swap2 = cReplace[swap0][1]

        cMsg[cBuffer1], cMsg[swap0] = cMsg[swap0], cMsg[cBuffer1]
        cMsg[cBuffer2], cMsg[swap1] = cMsg[swap1], cMsg[cBuffer2]
        cMsg[cBuffer3], cMsg[swap2] = cMsg[swap2], cMsg[cBuffer3]

    while ''.join(cMsg) != cCorrect:
        current = cMsg[cBuffer1]

        if current == cCorrect[cBuffer1] or current == cCorrect[cBuffer2] or current == cCorrect[cBuffer3]:
            cCopy = cMsg.copy()
            cCopy = [i for i in cCopy if cCopy.index(
                i) != list(cCorrect).index(i)]
            cCopy = [i for i in cPriority if i in cCopy]
            current = cCopy[0]

        cMemo.append(current)
        swapCorners(current)

    # Edges ----
    eCorrect = 'adbcehfgiljkmpnosrtquxvw'
    eMemo = []
    eMsg = re.findall('([a-z])', allLetters)
    ePriority = list('dlrxfhpntjuwvegaciqkso')
    eReplace = {
        0:19, 19:0, 2:12, 12:2, 
        3:8, 8:3, 1:4, 4:1, 
        6:9, 9:6, 10:13, 13:10, 
        14:18, 18:14, 17:5, 5:17, 
        11:20, 20:11, 15:22, 22:15, 
        16:23, 23:16, 7:21, 21:7
    }

    def toCorrectEdgeString(edges):

        correctedString = [] 
        splitEveryFour = re.findall('....', edges)
        for substring in splitEveryFour:
            substring = substring[0] + substring[-1] + substring[1:-1]
            correctedString.append(substring)
        correctedString[4] = correctedString[4][::-1]
        return ''.join(correctedString)

    eBuffer1 = 2
    eBuffer2 = 12
    if preferences:
        correctEdgeString = toCorrectEdgeString(preferences[2])
        eBuffer1 = correctEdgeString.index(preferences[4])
        eBuffer2 = eReplace[eBuffer1]

    def swapEdges(current):
        swap0 = eCorrect.index(current)
        swap1 = eReplace[swap0]

        eMsg[eBuffer1], eMsg[swap0] = eMsg[swap0], eMsg[eBuffer1]
        eMsg[eBuffer2], eMsg[swap1] = eMsg[swap1], eMsg[eBuffer2]

    while ''.join(eMsg) != eCorrect:
        current = eMsg[eBuffer1]

        if current == eCorrect[eBuffer1] or current == eCorrect[eBuffer2]:
            eCopy = eMsg.copy()
            eCopy = [i for i in eCopy if eCopy.index(
                i) != list(eCorrect).index(i)]
            eCopy = [i for i in ePriority if i in eCopy]
            current = eCopy[0]

        eMemo.append(current)
        swapEdges(current)
    
    # Final output ----
    cMemo = ' '.join(cMemo)
    eMemo = ' '.join(eMemo).upper()

    if preferences:
      cMemo = cMemo.translate(str.maketrans('ABCDEFGHIJKLMNOPQRSTUVWX', str(preferences[1])))
      eMemo = eMemo.translate(str.maketrans('ABCDEFGHIJKLMNOPQRSTUVWX', str(preferences[2])))

    parityBool = 'no' if len(cMemo.split()) % 2 == 0 else 'yes'
    await ctx.send('```yaml\n' +
                   'Corners: ' + cMemo +
                   '\nEdges: ' + eMemo +
                   '\nParity: '+ parityBool +
                   '\n```')





@bot.command(pass_context=True)
async def show(ctx):
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
      reaction, user = await bot.wait_for('reaction_add', timeout = 1, check=check)
    except:
      await base.edit(content= str(' '.join(msg[:movecounter-1])) + ' ' + "**{}**".format(''.join(str(msg[movecounter-1]))) + ' ' + str(' '.join(msg[movecounter:])) + ' ' + '\n' + input3(msg[:movecounter]))
      movecounter += 1
    else:
      await base.edit(content = ' '.join(msg) + '\n' + input3(msg))
      await base.clear_reactions()
      return

  await base.clear_reactions()

   
@bot.command(pass_context=True)
async def setup(ctx):
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

@bot.command()
@commands.cooldown(1, 10, commands.BucketType.guild)
async def noob3(ctx):
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
    reaction, user = await bot.wait_for('reaction_add', timeout=10, check=check)
  except:
    await n.clear_reactions()
  else:
    await ctx.send(input3(msg.split()))
    await n.clear_reactions()


keep_alive.keep_alive()
bot.run(os.getenv("TOKEN"))