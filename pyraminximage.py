import numpy as np
from PIL import Image, ImageDraw

def pyraimage(scramble):
    scramble = scramble.split()

    gr = np.repeat("G", 9)
    re = np.repeat("R", 9)
    bl = np.repeat("B", 9)
    ye = np.repeat("Y", 9)

    rAxis = (3,6,7,8)
    lAxis = (6,1,5,4)

    rAlt = (8,3,7,6)
    lAlt = (4,6,5,1)

    def U():
        for i in range(4):
            gr[i], re[i], bl[i] = bl[i], gr[i], re[i]

    def Up():
        U(), U()

    def u():
        gr[0], re[0], bl[0] = bl[0], gr[0], re[0]

    def up():
        u(), u()

    def R():
        for i in range(4):
            gr[rAxis[i]], bl[lAxis[i]], ye[lAxis[i]] = ye[lAxis[i]], gr[rAxis[i]], bl[lAxis[i]]

    def Rp():
        R(), R()

    def r():
        gr[8], bl[4], ye[4] = ye[4], gr[8], bl[4]

    def rp():
        r(), r()

    def L():
        for i in range(4):
            gr[lAxis[i]], ye[rAxis[i]], re[rAxis[i]]  = re[rAxis[i]], gr[lAxis[i]], ye[rAxis[i]]

    def Lp():
        L(), L()

    def l():
        gr[4], ye[8], re[8] = re[8], gr[4], ye[4]

    def lp():
        l(), l()

    def B():
        for i in range(4):
            ye[i], bl[rAlt[i]], re[lAlt[i]] = re[lAlt[i]], ye[i], bl[rAlt[i]]

    def Bp():
        B(), B()

    def b():
        ye[0], bl[8], re[4] = re[4], ye[0], bl[8]

    def bp():
        b(), b()

    moveMap = {
        "U":U, "U'":Up, "R":R, "R'":Rp, "L":L, "L'":Lp, "B":B, "B'":Bp,
        "u":u, "u'":up, "r":r, "r'":rp, "l":l, "l'":lp, "b":b, "b'":bp
    }

    [moveMap[move]() for move in scramble]


    def draw_face(face: list, degrees: int):
        width = 400
        height = 400
        img = Image.new('RGBA', (width, height), (255, 255, 255, 0)) 
        draw = ImageDraw.Draw(img)

        colors = {
            "R": (200, 0, 0),
            "G": (81, 227, 0),
            "B": (3, 132, 252),
            "Y": (245, 238, 0)
        }

        def triangle(point: int, fill: str):
            degrees = 0 if point % 2 == 0 else 180
                
            base = 100
            height = int((base*(3**.5))/2)
            sticker = Image.new('RGBA', (base, height), (255, 255, 255, 0))
            draw = ImageDraw.Draw(sticker)
            
            draw.polygon((0,height,base*.5,0,base,height), fill=fill)
            sticker = sticker.rotate(degrees)

            return sticker

        tBase = 100
        tHeight = int((tBase*(3**.5))/2)
        x = int(width/2) - 50
        y = int(((height-(tHeight*3))/2)-tHeight/2)
        z = 1
        alpha = 0 
        beta = 0
        for i in range(3):
            for j in range(z):
                img.paste(triangle(alpha, colors[face[beta]]), (x, y), mask=triangle(alpha, "red"))
                x += int(tBase/2)
                alpha += 1
                beta += 1
            x -= 50*(z+1)
            y += tHeight
            z += 2
            alpha = 0

        outline = Image.open("WireframePyra.png")
        img.paste(outline, (0,0), outline)
        img = img.rotate(-degrees)
        return img
        
    img = Image.new('RGBA', (800, 650), (255, 255, 255, 0)) 
    draw = ImageDraw.Draw(img)

    faces = (re, gr, bl, ye)
    degrees = (60, 0, 300, 180)

    height = int((100*(3**.5))/2)
    coordinates = ((0,-75),(200,height-75),(400,-75),(200,height*3-25))

    for i in range(4):
        img.paste(draw_face(faces[i], degrees[i]), (coordinates[i][0],coordinates[i][1]), mask=draw_face(faces[i], degrees[i]))

    img = img.crop((40, 30, 760, 615))
    return img
