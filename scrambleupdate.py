import numpy as np
from PIL import Image, ImageDraw
import random

def scrambleimage(layers, scramble):
    global faceU
    global faceD
    global faceR
    global faceL
    global faceF
    global faceB

    faceU = np.repeat("W", layers**2).reshape(layers, layers)
    faceD = np.repeat("Y", layers**2).reshape(layers, layers)
    faceR = np.repeat("R", layers**2).reshape(layers, layers)
    faceL = np.repeat("O", layers**2).reshape(layers, layers)
    faceF = np.repeat("G", layers**2).reshape(layers, layers)
    faceB = np.repeat("B", layers**2).reshape(layers, layers)

    def xAxis(slice: int = layers - 1):
        inverse = layers - slice - 1
        faceU[:, slice], faceF[:, slice], faceD[:, slice], faceB[:, inverse] = faceF[:, slice], faceD[:, slice], faceB[:, inverse][::-1], faceU[:, slice][::-1].copy()

    def yAxis(slice: int = 0):
        faceF[[slice]], faceR[[slice]], faceB[[slice]], faceL[[slice]] = faceR[[slice]], faceB[[slice]], faceL[[slice]], faceF[[slice]]
        
    def zAxis(slice: int = layers - 1):
        inverse = layers - slice - 1
        faceU[[slice]], faceR[:, inverse], faceD[[inverse]], faceL[:, slice] = faceL[:, slice][::-1], faceU[[slice]], faceR[:, inverse][::-1].copy(), faceD[[inverse]][::-1]

    def R():
        global faceR
        xAxis()
        faceR = np.rot90(faceR, 3)

    def Rp():
        R(), R(), R()

    def R2():
        R(), R()

    def L():
        Lp(), Lp(), Lp()

    def Lp():
        global faceL
        xAxis(0)
        faceL = np.rot90(faceL)

    def L2():
        Lp(), Lp()

    def U():
        global faceU
        yAxis()
        faceU = np.rot90(faceU, 3)

    def Up():
        U(), U(), U()

    def U2():
        U(), U()

    def D():
        Dp(), Dp(), Dp()

    def Dp():
        global faceD
        yAxis(layers-1)
        faceD = np.rot90(faceD)

    def D2():
        Dp(), Dp()

    def F():
        global faceF
        zAxis()
        faceF = np.rot90(faceF, 3)

    def Fp():
        F(), F(), F()

    def F2():
        F(), F()

    def B():
        Bp(), Bp(), Bp()

    def Bp():
        global faceB
        zAxis(0)
        faceB = np.rot90(faceB)

    def B2():
        Bp(), Bp()

    # ----------

    def Rw():
        R(), xAxis(layers-2)

    def Rwp():
        Rw(), Rw(), Rw()

    def Rw2():
        Rw(), Rw()

    def Lw():
        Lwp(), Lwp(), Lwp()

    def Lwp():
        Lp(), xAxis(1)

    def Lw2():
        Lwp(), Lwp()

    def Uw():
        U(), yAxis(1)

    def Uwp():
        Uw(), Uw(), Uw()

    def Uw2():
        Uw(), Uw()

    def Dw():
        Dwp(), Dwp(), Dwp()

    def Dwp():
        Dp(), yAxis(layers-2)

    def Dw2():
        Dwp(), Dwp()

    def Fw():
        F(), zAxis(layers-2)

    def Fwp():
        Fw(), Fw(), Fw()

    def Fw2():
        Fw(), Fw()

    def Bw():
        Bwp(), Bwp(), Bwp()

    def Bwp():
        Bp(), zAxis(1)

    def Bw2():
        Bwp(), Bwp()

    # ------

    def tRw():
        Rw(), xAxis(layers-3)

    def tRwp():
        tRw(), tRw(), tRw()

    def tRw2():
        tRw(), tRw()

    def tLw():
        tLwp(), tLwp(), tLwp()

    def tLwp():
        Lwp(), xAxis(2)

    def tLw2():
        tLwp(), tLwp()

    def tUw():
        Uw(), yAxis(2)

    def tUwp():
        tUw(), tUw(), tUw()

    def tUw2():
        tUw(), tUw()

    def tDw():
        tDwp(), tDwp(), tDwp()

    def tDwp():
        Dwp(), yAxis(layers-3)

    def tDw2():
        tDwp(), tDwp()

    def tFw():
        Fw(), zAxis(layers-3)

    def tFwp():
        tFw(), tFw(), tFw()

    def tFw2():
        tFw(), tFw()

    def tBw():
        tBwp(), tBwp(), tBwp()

    def tBwp():
        Bwp(), zAxis(2)

    def tBw2():
        tBwp(), tBwp()

    # ------

    moveMap = {
        'U': U, "U'": Up, 'U2': U2, 'U2\'': U2,
        'D': D, "D'": Dp, 'D2': D2, 'D2\'': D2,
        'R': R, "R'": Rp, 'R2': R2, 'R2\'': R2,
        'L': L, "L'": Lp, 'L2': L2, 'L2\'': L2,
        'F': F, "F'": Fp, 'F2': F2, 'F2\'': F2,
        'B': B, "B'": Bp, 'B2': B2, 'B2\'': B2,

        "Uw":Uw, "Uw'":Uwp, "Uw2":Uw2, 
        "Dw":Dw, "Dw'":Dwp, "Dw2":Dw2, 
        "Rw":Rw, "Rw'":Rwp, "Rw2":Rw2, 
        "Lw":Lw, "Lw'":Lwp, "Lw2":Lw2, 
        "Fw":Fw, "Fw'":Fwp, "Fw2":Fw2, 
        "Bw":Bw, "Bw'":Bwp, "Bw2":Bw2, 

        "3Uw":tUw, "3Uw'":tUwp, "3Uw2":tUw2, 
        "3Dw":tDw, "3Dw'":tDwp, "3Dw2":tDw2, 
        "3Rw":tRw, "3Rw'":tRwp, "3Rw2":tRw2, 
        "3Lw":tLw, "3Lw'":tLwp, "3Lw2":tLw2, 
        "3Fw":tFw, "3Fw'":tFwp, "3Fw2":tFw2, 
        "3Bw":tBw, "3Bw'":tBwp, "3Bw2":tBw2, 
    }

    [moveMap[move]() for move in scramble.split()]

    # ------

    img = Image.new('RGBA', (1325, 1000), (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)

    colors = {
        "R": (200, 0, 0),
        "O": (241,147,1),
        "W": (255, 255, 255), 
        "Y": (245, 238, 0),
        "G": (81, 227, 0),
        "B": (3, 132, 252)
    }

    width = int(7/layers)+1
    boxSize = 300/layers

    x = 25
    y = 350
    z = 0
    middle = np.concatenate([faceL, faceF, faceR, faceB], axis=None)

    for i in range(4):
        for j in range(layers):
            for k in range(layers):
                draw.rectangle((x,y,x+boxSize,y+boxSize), fill=colors[middle[z]], outline="black", width=width)
                x += boxSize
                z += 1
            x -= 300
            y += boxSize
        x += 325
        y -= 300

    x = 350
    y = 25
    z = 0
    topBottom = np.concatenate([faceU, faceD], axis=None)

    for i in range(2):
        for j in range(layers):
            for k in range(layers):
                draw.rectangle((x,y,x+boxSize,y+boxSize), fill=colors[topBottom[z]], outline="black", width=width)
                x += boxSize
                z += 1
            x -= 300
            y += boxSize
        y += 350

    return img