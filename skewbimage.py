import numpy as np
from PIL import Image, ImageDraw

def skewbimage(scramble):
    scramble = scramble.split()

    faceU = np.repeat("W", 5)
    faceD = np.repeat("Y", 5)
    faceR = np.repeat("R", 5)
    faceL = np.repeat("O", 5)
    faceF = np.repeat("G", 5)
    faceB = np.repeat("B", 5)

    rR = (1,2,3,4)
    rB = (4,2,0,3)
    lL = (3,2,1,0)
    bB = (0,2,4,1)

    colors = {
        "R": (200, 0, 0),
        "O": (241,147,1),
        "W": (255, 255, 255), 
        "Y": (245, 238, 0),
        "G": (81, 227, 0),
        "B": (3, 132, 252)
    }

    hyp = int(125*(3**.5))


    def R():
        faceU[1], faceF[4], faceL[3] = faceF[4], faceL[3], faceU[1]
        for i in range(4):
            faceR[rR[i]], faceB[rB[i]], faceD[rR[i]] = faceD[rR[i]], faceR[rR[i]], faceB[rB[i]]


    def L():
        faceU[3], faceR[3], faceB[4] = faceB[4], faceU[3], faceR[3]
        for i in range(4):
            faceF[rB[i]], faceD[lL[i]], faceL[rR[i]] = faceL[rR[i]], faceF[rB[i]], faceD[lL[i]]


    def U():
        faceF[0], faceR[1], faceD[3] = faceR[1], faceD[3], faceF[0]
        for i in range(4):
            faceU[lL[i]], faceL[lL[i]], faceB[bB[i]] = faceB[bB[i]], faceU[lL[i]], faceL[lL[i]]


    def B():
        faceU[0], faceF[3], faceR[4] = faceR[4], faceU[0], faceF[3]
        for i in range(4):
            faceL[rB[i]], faceD[rB[i]], faceB[rR[i]] = faceB[rR[i]], faceL[rB[i]], faceD[rB[i]]


    def draw_face(face, degrees: int = 0):
        hyp = int(125*(3**.5))


        def draw_diamond(fill):
            hyp = int(125*(3**.5))
            width = 500
            height = 250
            diamond = Image.new('RGBA', (width, height), (255,255, 255, 0))
            draw = ImageDraw.Draw(diamond)
            draw.polygon((width/2, 0, width/2 - hyp/2, height/4, width/2, height/2, width/2 + hyp/2, height/4), fill=fill, outline="black")
            return diamond

        def draw_rectangle(fill):
            hyp = int(125*(3**.5))
            width = 500
            height = 250
            rectangle = Image.new('RGBA', (width, height), (255,255, 255, 0))
            draw = ImageDraw.Draw(rectangle)
            draw.rectangle((width/2 - hyp/2, height/4, width/2 + hyp/2, height*.75), fill=fill, outline="black")
            return rectangle

        width = 500
        height = 515
        img = Image.new('RGBA', (width, height), (255, 255, 255, 0)) 

        x = 0
        y = 0
        img.paste(draw_diamond(colors[face[0]]), (x, y), mask=draw_diamond(colors[face[0]]))

        x += int(hyp/2)
        y += 63
        img.paste(draw_diamond(colors[face[1]]), (x, y), mask=draw_diamond(colors[face[0]]))

        x -= hyp
        img.paste(draw_diamond(colors[face[3]]), (x, y), mask=draw_diamond(colors[face[0]]))

        x += int(hyp/2)
        y += 63
        img.paste(draw_diamond(colors[face[4]]), (x, y), mask=draw_diamond(colors[face[0]]))
        
        x = 0
        y = 0
        img.paste(draw_rectangle(colors[face[2]]), (x,y), mask=draw_rectangle(colors[face[2]]))

        img = img.rotate(degrees)

        return img

    moveMap = {
        "R": R, "L":L, "U":U, "B":B
    }

    turns = ["U","R","L","B"]
    for move in scramble:
        if move[-1] == "'":
            move = move[:-1]
            spec = 2
        else:
            spec = 1

        for i in range(spec):
            moveMap[move]()

    LFDorder = (3,0,2,4,1)
    faceL = [faceL[i] for i in LFDorder]
    faceF = [faceF[i] for i in LFDorder]
    faceD = [faceD[i] for i in LFDorder]
    faceR = faceR[::-1]
    faceB = faceB[::-1]


    width = 950
    height = 775
    middle = int((width-500)/2)

    img = Image.new('RGBA', (width, height), (255, 255, 255, 0)) 
    draw = ImageDraw.Draw(img)

    img.paste(draw_face(faceU, 0), (middle, 0), mask=draw_face(faceU, 0))

    img.paste(draw_face(faceL, 120), (middle - hyp - 15, -130), mask=draw_face(faceR, 120))
    img.paste(draw_face(faceF, 120), (middle, 0), mask=draw_face(faceF, 120))
    img.paste(draw_face(faceD, 120), (middle, 265), mask=draw_face(faceR, 120))

    img.paste(draw_face(faceR, 240), (middle, 0), mask=draw_face(faceR, 240))
    img.paste(draw_face(faceB, 240), (middle + hyp + 15, -130), mask=draw_face(faceR, 240))

    return img

