import random

# Lists for scrambling - not random state but it is fast
URF = ['U_', 'R_', 'F_']
UD = ['U_', 'D_']
RL = ['R_', 'L_']
FB = ['F_', 'B_']
UDRLFB = [['U_', 'D_'], ['R_', 'L_'], ['F_', 'B_']]
specification = ['', '\'', '2']
acceptedmoves = ['U','D','R','L','F','B','x','y','z','M','E','S','u','d','r','l','f','b']
XYZ = ['x_', 'y_', 'z_']

# Emotes that make up the scramble images - much nicer than the default color squares emojis
# white = '<:wt:710663779280486440>'
white = ':white_large_square:'
yello = '<:ys:709901846399156324>'
green = '<:gr:710283142396641352>'
bluee = '<:bl:710286003386056716>'
orang = '<:or:710664059741012009>'
reeed = '<:rd:710664221045686273>'

#____________________________________________
def R():
    w[3], g[3], y[3], b[3] = g[3], y[3], b[3], w[3]
    w[6], g[6], y[6], b[6] = g[6], y[6], b[6], w[6]
    w[9], g[9], y[9], b[9] = g[9], y[9], b[9], w[9]

    r[1], r[3], r[9], r[7] = r[7], r[1], r[3], r[9]
    r[2], r[6], r[8], r[4] = r[4], r[2], r[6], r[8]


def Rp():
    R(), R(), R()


def R2():
    R(), R()


def L():
    w[1], g[1], y[1], b[1] = b[1], w[1], g[1], y[1]
    w[4], g[4], y[4], b[4] = b[4], w[4], g[4], y[4]
    w[7], g[7], y[7], b[7] = b[7], w[7], g[7], y[7]

    o[1], o[3], o[9], o[7] = o[7], o[1], o[3], o[9]
    o[2], o[6], o[8], o[4] = o[4], o[2], o[6], o[8]


def Lp():
    L(), L(), L()


def L2():
    L(), L()


def U():
    g[1], r[1], b[9], o[1] = r[1], b[9], o[1], g[1]
    g[2], r[2], b[8], o[2] = r[2], b[8], o[2], g[2]
    g[3], r[3], b[7], o[3] = r[3], b[7], o[3], g[3]

    w[1], w[3], w[9], w[7] = w[7], w[1], w[3], w[9]
    w[2], w[6], w[8], w[4] = w[4], w[2], w[6], w[8]


def Up():
    U(), U(), U()


def U2():
    U(), U()


def D():
    g[7], r[7], b[3], o[7] = o[7], g[7], r[7], b[3]
    g[8], r[8], b[2], o[8] = o[8], g[8], r[8], b[2]
    g[9], r[9], b[1], o[9] = o[9], g[9], r[9], b[1]

    y[1], y[3], y[9], y[7] = y[7], y[1], y[3], y[9]
    y[2], y[6], y[8], y[4] = y[4], y[2], y[6], y[8]


def Dp():
    D(), D(), D()


def D2():
    D(), D()


def F():
    w[7], r[1], y[3], o[9] = o[9], w[7], r[1], y[3]
    w[8], r[4], y[2], o[6] = o[6], w[8], r[4], y[2]
    w[9], r[7], y[1], o[3] = o[3], w[9], r[7], y[1]

    g[1], g[3], g[9], g[7] = g[7], g[1], g[3], g[9]
    g[2], g[6], g[8], g[4] = g[4], g[2], g[6], g[8]


def Fp():
    F(), F(), F()


def F2():
    F(), F()


def B():
    w[1], r[3], y[9], o[7] = r[3], y[9], o[7], w[1]
    w[2], r[6], y[8], o[4] = r[6], y[8], o[4], w[2]
    w[3], r[9], y[7], o[1] = r[9], y[7], o[1], w[3]

    b[1], b[3], b[9], b[7] = b[7], b[1], b[3], b[9]
    b[2], b[6], b[8], b[4] = b[4], b[2], b[6], b[8]


def Bp():
    B(), B(), B()


def B2():
    B(), B()


def M():
    g[2], y[2], b[2], w[2] = w[2], g[2], y[2], b[2]
    g[5], y[5], b[5], w[5] = w[5], g[5], y[5], b[5]
    g[8], y[8], b[8], w[8] = w[8], g[8], y[8], b[8]


def Mp():
    M(), M(), M()


def M2():
    M(), M()


def E():
    g[4], r[4], b[6], o[4] = o[4], g[4], r[4], b[6]
    g[5], r[5], b[5], o[5] = o[5], g[5], r[5], b[5]
    g[6], r[6], b[4], o[6] = o[6], g[6], r[6], b[4]


def Ep():
    E(), E(), E()


def E2():
    E(), E()


def S():
    w[4], r[2], y[6], o[8] = o[8], w[4], r[2], y[6]
    w[5], r[5], y[5], o[5] = o[5], w[5], r[5], y[5]
    w[6], r[8], y[4], o[2] = o[2], w[6], r[8], y[4]


def Sp():
    S(), S(), S()


def S2():
    S(), S()


def X():
    Mp(), R(), Lp()


def Xp():
    M(), Rp(), L()


def X2():
    X(), X()


def Y():
    Ep(), U(), Dp()


def Yp():
    E(), Up(), D()


def Y2():
    Y(), Y()


def Z():
    S(), F(), Bp()


def Zp():
    Sp(), Fp(), B()


def Z2():
    Z(), Z()


def uw():
    U(), Ep()


def up():
    Up(), E()


def u2():
    uw(), uw()


def dw():
    D(), E()


def dp():
    Dp(), Ep()


def d2():
    dw(), dw()


def rw():
    R(), Mp()


def rp():
    Rp(), M()


def r2():
    rw(), rw()


def lw():
    L(), M()


def lp():
    Lp(), Mp()


def l2():
    lw(), lw()


def fw():
    F(), S()


def fp():
    Fp(), Sp()


def f2():
    fw(), fw()


def bw():
    B(), Sp()


def bp():
    Bp(), S()


def b2():
    bw(), bw()


def no():
    pass


sequence = {
    'U': U, "U'": Up, 'U2': U2, 'U2\'': U2,
    'D': D, "D'": Dp, 'D2': D2, 'D2\'': D2,
    'R': R, "R'": Rp, 'R2': R2, 'R2\'': R2,
    'L': L, "L'": Lp, 'L2': L2, 'L2\'': L2,
    'F': F, "F'": Fp, 'F2': F2, 'F2\'': F2,
    'B': B, "B'": Bp, 'B2': B2, 'B2\'': B2,
    'M': M, "M'": Mp, 'M2': M2, 'M2\'': M2,
    'E': E, "E'": Ep, 'E2': E2, 'E2\'': E2,
    'S': S, "S'": Sp, 'S2': S2, 'S2\'': S2,
    'x': X, "x'": Xp, 'x2': X2, 'x2\'': X2,
    'y': Y, "y'": Yp, 'y2': Y2, 'y2\'': Y2,
    'z': Z, "z'": Zp, 'z2': Z2, 'z2\'': Z2,
    'u': uw, "u'": up, 'u2': u2, 'u2\'': u2,
    'd': dw, "d'": dp, 'd2': d2, 'd2\'': d2,
    'r': rw, "r'": rp, 'r2': r2, 'r2\'': r2,
    'l': lw, "l'": lp, 'l2': l2, 'l2\'': l2,
    'f': fw, "f'": fp, 'f2': f2, 'f2\'': f2,
    'b': bw, "b'": bp, 'b2': b2, 'b2\'': b2,
    ' ': no
}


def cubestring(msg):
    global w
    global o
    global g 
    global r 
    global b
    global y
    w = ['', 'U', 'U', 'U',
             'U', 'U', 'U',
             'U', 'U', 'U']
    y = ['', 'D', 'D', 'D',
             'D', 'D', 'D',
             'D', 'D', 'D']
    g = ['', 'F', 'F', 'F',
             'F', 'F', 'F',
             'F', 'F', 'F']
    b = ['', 'B', 'B', 'B',
             'B', 'B', 'B',
             'B', 'B', 'B']
    o = ['', 'L', 'L', 'L',
             'L', 'L', 'L',
             'L', 'L', 'L']
    r = ['', 'R', 'R', 'R',
             'R', 'R', 'R',
             'R', 'R', 'R']

    [sequence[z]() for z in msg]
    return (w+r+g+y+o+b[::-1])

def bld3(msg):
    global w
    global o
    global g 
    global r 
    global b
    global y
    w = ['', 'A', 'a', 'B',
             'd', '1', 'b',
             'D', 'c', 'C']
    o = ['', 'E', 'e', 'F',
             'h', '2', 'f',
             'H', 'g', 'G']
    g = ['', 'I', 'i', 'J',
             'l', '3', 'j',
             'L', 'k', 'K']
    r = ['', 'M', 'm', 'N',
             'p', '4', 'n',
             'P', 'o', 'O']
    b = ['', 'S', 's', 'T',
             'r', '5', 't',
             'R', 'q', 'Q']
    y = ['', 'U', 'u', 'V',
             'x', '6', 'v',
             'X', 'w', 'W']

    [sequence[z]() for z in msg]
    return (w+o+g+r+b+y)

 
def input3(msg):
    global w
    global o
    global g 
    global r 
    global b
    global y
    w = ['',white, white, white,
            white, white, white,
            white, white, white]
    y = ['',yello, yello, yello,
            yello, yello, yello,
            yello, yello, yello]
    g = ['',green, green, green,
            green, green, green,
            green, green, green]
    b = ['',bluee, bluee, bluee,  
            bluee, bluee, bluee,
            bluee, bluee, bluee]
    o = ['',orang, orang, orang,
            orang, orang, orang,
            orang, orang, orang]
    r = ['',reeed, reeed, reeed,
            reeed, reeed, reeed,
            reeed, reeed, reeed]

    [sequence[z]() for z in msg]
    thescramble3 = (
    '_ _                  '+ w[1]+ w[2]+ w[3]+'\n'
    '                   '+ w[4]+ w[5]+ w[6]+'\n'
    '                   '+ w[7]+ w[8]+ w[9]+'\n'
    + o[1]+ o[2]+ o[3]+' '+g[1]+ g[2]+ g[3]+' '+r[1]+ r[2]+ r[3]+' '+b[9]+ b[8]+ b[7]+'\n'
    + o[4]+ o[5]+ o[6]+' '+g[4]+ g[5]+ g[6]+' '+r[4]+ r[5]+ r[6]+' '+b[6]+ b[5]+ b[4]+'\n'
    + o[7]+ o[8]+ o[9]+' '+g[7]+ g[8]+ g[9]+' '+r[7]+ r[8]+ r[9]+' '+b[3]+ b[2]+ b[1]+'\n' 
    '                   ' +y[1]+ y[2]+ y[3]+'\n'
    '                   ' +y[4]+ y[5]+ y[6]+'\n'
    '                   ' +y[7]+ y[8]+ y[9]+'\n'
    )
    return thescramble3

def scramble2(msg):
  w = ['',white, white, white, white]
  y = ['',yello, yello, yello, yello]
  g = ['',green, green, green, green]
  b = ['',bluee, bluee, bluee, bluee]
  o = ['',orang, orang, orang, orang]
  r = ['',reeed, reeed, reeed, reeed]
  def R():
    w[2], g[2], y[2], b[2] = g[2], y[2], b[2], w[2] 
    w[4], g[4], y[4], b[4] = g[4], y[4], b[4], w[4]

    r[1], r[2], r[4], r[3] = r[3], r[1], r[2], r[4]

  def Rp():
    R(), R(), R()

  def R2():
    R(), R()

  def L():
    w[1], g[1], y[1], b[1] = b[1], w[1], g[1], y[1]
    w[3], g[3], y[3], b[3] = b[3], w[3], g[3], y[3]

    o[1], o[2], o[4], o[3] = o[3], o[1], o[2], o[4]
    
  def Lp():
    L(), L(), L()

  def U():
    g[1], r[1], b[4], o[1] = r[1], b[4], o[1], g[1]
    g[2], r[2], b[3], o[2] = r[2], b[3], o[2], g[2]

    w[1], w[2], w[4], w[3] = w[3], w[1], w[2], w[4]

  def Up():
    U(), U(), U()

  def U2():
    U(), U()

  def D():
    g[3], r[3], b[2], o[3] = o[3], g[3], r[3], b[2]
    g[4], r[4], b[1], o[4] = o[4], g[4], r[4], b[1]
    
    y[1], y[2], y[4], y[3] = y[3], y[1], y[2], y[4]

  def Dp():
    D(), D(), D()

  def F():
    w[3], r[1], y[2], o[4] = o[4], w[3], r[1], y[2]
    w[4], r[3], y[1], o[2] = o[2], w[4], r[3], y[1]

    g[1], g[2], g[4], g[3] = g[3], g[1], g[2], g[4]

  def Fp():
    F(), F(), F()

  def F2():
    F(), F()

  def B():
    w[1], r[2], y[4], o[3] = r[2], y[4], o[3], w[1]
    w[2], r[4], y[3], o[1] = r[4], y[3], o[1], w[2]

    b[1], b[2], b[4], b[3] = b[3], b[1], b[2], b[4]

  def Bp():
    B(), B(), B()

  def X():
    R(), Lp()

  def Xp():
    Rp(), L()

  def X2():
    X(), X()

  def Y():
    U(), Dp()

  def Yp():
    Up(), D()

  def Y2():
    Y(), Y()

  def Z():
    F(), Bp()
  
  def Zp():
    Fp(), B()
  
  def Z2():
    Z(), Z()

  sequence = {
    'U':U, "U'":Up, 'U2':U2,
    'D':D, "D'":Dp,
    'R':R, "R'":Rp, 'R2':R2,
    'L':L, "L'":Lp,
    'F':F, "F'":Fp, 'F2':F2,
    'B':B, "B'":Bp,
    'x':X, "x'":Xp, "x2":X2,
    'y':Y, "y'":Yp, "y2":Y2,
    'z':Z, "z'":Zp, "z2":Z2
    } 

  [sequence[z]() for z in msg]
  return (
        '_ _            '    +w[1]+ w[2]+
  '\n'+ '_ _            '    +w[3]+ w[4]+
  '\n'+      o[1]+ o[2]+' '+g[1]+ g[2]+' '+r[1]+ r[2]+' '+b[4]+ b[3]+ 
  '\n'+      o[3]+ o[4]+' '+g[3]+ g[4]+' '+r[3]+ r[4]+' '+b[2]+ b[1]+
  '\n'+ '_ _            '    +y[1]+ y[2]+
  '\n'+ '_ _            '    +y[3]+ y[4] )
  

def scramble1():
  w  = [white] 
  o  = [orang] 
  g  = [green] 
  b  = [bluee] 
  r  = [reeed] 
  ye = [yello]

  def y(): 
    g[0], r[0], b[0], o[0] = r[0], b[0], o[0], g[0]

  def yp():
    y(), y(), y()

  def y2():
    y(), y()

  def x():
    w[0], g[0], ye[0], b[0] = g[0], ye[0], b[0], w[0]

  def xp():
    x(), x(), x()

  def x2():
    x(), x()

  def z():
    w[0], r[0], ye[0], o[0] = o[0], w[0], r[0], ye[0]

  def zp():
    z(), z(), z()

  def z2():
    z(), z()

  sequence = {
    'y':y, "y'":yp, 'y2':y2, 
    'x':x, "x'":xp, 'x2':x2,
    'z':z, "z'":zp, 'z2':z2}

  fs = ['']
  while len(fs) < 10:
    fs.append(random.choice(XYZ))
    if fs[-1] == fs[-2]:
      del fs[-1]

  for t in XYZ:
    if t not in fs:
      fs[random.randint(1,10)] = t

  del fs[0]
  fs = [item.replace('_', str(random.choice(specification))) for item in fs]

  [sequence[m]() for m in fs]
  thescramble1 = (
    '_ _     ' + w[0] + '\n' +
    o[0] + g[0] + r[0] + b[0] + '\n' +
    '_ _     ' + ye[0]
  )

  return ' '.join(fs) + '\n' +  thescramble1