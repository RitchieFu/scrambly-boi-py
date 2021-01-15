import numpy as np
from PIL import Image, ImageDraw

wh = np.repeat("Wh", 11)
gr = np.repeat("Gr", 11)
re = np.repeat("Re", 11)
bl = np.repeat("Bl", 11)  
ye = np.repeat("Ye", 11) 
pu = np.repeat("Pu", 11)

ra = np.repeat("Ra", 11) 
be = np.repeat("Be", 11)
pi = np.repeat("Pi", 11) 
lg = np.repeat("Lg", 11) 
ro = np.repeat("Or", 11) 
lb = np.repeat("Lb", 11) 


def megaimage(scramble):
    scramble = scramble.split()

    colors = {
        "Wh": (255, 255, 255), 
        "Gr": (0, 102, 0),
        "Re": (221, 0, 0),
        "Bl": (0,0,187),
        "Ye": (255,204,0),
        "Pu": (136,17,255),

        "Ra": (112,128,144),
        "Be": (225, 198, 153),
        "Pi": (255, 153, 255),
        "Lg": (119, 238, 0),
        "Or": (255,136,51),
        "Lb": (136, 221, 255)
    }

    grRot = (1,2,4,5,7,8,9,10)
    lbRot = (3,4,6,7,5,8,9,10)
    roRot = (7,10,6,9,1,0,5,8)
    yeRot = (9,8,4,7,1,0,3,6)
    whRot = (1,2,6,3,9,10,7,4)

    beRot = (0,1,2,5,6,3,8,9,10,7,4)
    lgRot = (4,7,10,3,6,9,2,1,0,5,8)
    blRot = (2,5,10,1,4,9,0,3,6,7,8)
    dRot = (3,4,5,6,7,8,9,10)

    pgTurn = (8,5,0,1,2,9,6,3,10,7,4)

    def R():
        global pi
        for i in range(8):
            gr[grRot[i]], lb[lbRot[i]], ro[roRot[i]], ye[yeRot[i]], wh[whRot[i]] = lb[lbRot[i]], ro[roRot[i]], ye[yeRot[i]], wh[whRot[i]], gr[grRot[i]]

        for i in range(11):
            re[i], be[beRot[i]], ra[beRot[i]], lg[lgRot[i]], bl[blRot[i]] = be[beRot[i]], ra[beRot[i]], lg[lgRot[i]], bl[blRot[i]], re[i]

        pi = [pi[i] for i in pgTurn]

    def D():
        global ra
        for i in range(8):
            gr[dRot[i]], re[dRot[i]], bl[dRot[i]], ye[dRot[i]], pu[dRot[i]] = pu[dRot[i]], gr[dRot[i]], re[dRot[i]], bl[dRot[i]], ye[dRot[i]]
        
        for i in range(11):
            be[i], pi[i], lg[i], ro[i], lb[i] = lb[i], be[i], pi[i], lg[i], ro[i]

        ra = [ra[i] for i in pgTurn]

    def U():
        global wh
        for i in range(3):
            gr[i], re[i], bl[i], ye[i], pu[i] = re[i], bl[i], ye[i], pu[i], gr[i] 

        wh = [wh[i] for i in pgTurn]

    moveMap = {
        "R":R, "D":D, "U":U
    }

    for move in scramble:
        if move[1:] == "++":
            spec = 2
        elif move[1:] == "--":
            spec = 3
        elif move[1:] == "'":
            spec = 4
        else:
            spec = 1

        move = move[0]

        for i in range(spec):
            moveMap[move]()

    pointyFaces = [list(array) for array in [wh, be, pi, lg, ro, lb, ra]]

    def draw_face(face, rDegrees: int = 0):
        
        def draw_edge(fill, degrees):
            width = 250
            height = 250
            img = Image.new('RGBA', (width, height), (255, 255, 255, 0))
            draw = ImageDraw.Draw(img)
            draw.polygon((159.4,50,125,75,172,109,184,68), fill=fill, outline="black")
            return img.rotate(degrees)

        def draw_corner(fill, degrees):
            width = 250
            height = 250
            img = Image.new('RGBA', (width, height), (255, 255, 255, 0))
            draw = ImageDraw.Draw(img)
            draw.polygon((125,25,90.6,50,125,75,159,50), fill=fill, outline="black")
            return img.rotate(degrees)
            
        width = 250
        height = 250
        img = Image.new('RGBA', (width, height), (255, 255, 255, 0))
        draw = ImageDraw.Draw(img)

        if list(face) in pointyFaces:
            order = (0,1,2,3,4,7,10,9,8,5,6)
        else:
            order = (0,1,2,5,10,9,8,7,6,3,4)
        
        face = [face[i] for i in order]

        corners = list(face[:-1:2])
        edges = list(face[1:-1:2])

        draw.regular_polygon((125,125,50), 5, fill=colors[face[-1]], outline="black")

        degrees = 0
        for i in corners:
            img.paste(draw_corner(colors[i], degrees), (0,0), mask=draw_corner(colors[i], degrees))
            degrees -= 72
            
        degrees = 0
        for i in edges:
            img.paste(draw_edge(colors[i], degrees), (0,0), mask=draw_edge(colors[i], degrees))
            degrees -= 72

        return img.rotate(rDegrees)


    width = 1050
    height = 600
    img = Image.new('RGBA', (width, height), (255, 255, 255, 0))
    img.paste(draw_face(wh, 72), (200,200), mask=draw_face(wh, 72))
    img.paste(draw_face(gr, 36), (200,360), mask=draw_face(gr, 36))
    img.paste(draw_face(pu, -36), (46,250), mask=draw_face(pu, -36))
    img.paste(draw_face(re, 108), (354,250), mask=draw_face(re, 108))
    img.paste(draw_face(bl, 180), (295,70), mask=draw_face(bl, 180))
    img.paste(draw_face(ye, -108), (105,70), mask=draw_face(ye, -108))

    img.paste(draw_face(lb, 288), (757,380), mask=draw_face(lb, 288))
    img.paste(draw_face(be, 216), (567,380), mask=draw_face(be, 216))
    img.paste(draw_face(pi, 144), (508,200), mask=draw_face(pi, 144))
    img.paste(draw_face(lg, 72), (662,90), mask=draw_face(lg, 72))
    img.paste(draw_face(ro, 0), (816,200), mask=draw_face(ro, 0))
    img.paste(draw_face(ra, 252), (662,250), mask=draw_face(ra, 252))

    img = img.crop((60, 100, width, height))
    
    return img