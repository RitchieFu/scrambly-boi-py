import ast
import math
import numpy as np
from PIL import Image, ImageDraw

def squanimage(scramble):
    # defining the colors of the layers and faces
    uFace = np.array([["y2","y2","y1","y2","y2","y1"], ["y2","y2","y1","y2","y2","y1"]])
    dFace = np.array([["w1","w2","w2","w1","w2","w2"], ["w1","w2","w2","w1","w2","w2"]])
    uLayer = np.array([["r","b","b","b","o","o"], ["o","g","g","g","r","r"]])
    dLayer = np.array([["o","o","b","b","b","r"], ["r","r","g","g","g","o"]])
    # colors of the pieces
    colors = {
        "w1": (255, 255, 255), 
        "w2": (255, 255, 255), 
        "y1": (245, 238, 0),
        "y2": (245, 238, 0),
        "g": (81, 227, 0),
        "b": (3, 132, 252),
        "r": (200, 0, 0),
        "o": (241,147,1),
    }
    # swaps the U and D faces and layers just like a normal slice
    def slice():
        temp = np.copy(dFace[1])
        dFace[1] = uFace[1]
        uFace[1] = temp

        temp = np.copy(dLayer[1])
        dLayer[1] = uLayer[1]
        uLayer[1] = temp

    def draw_edge(degrees, topColor, sideColor):
        width = int(500*(2**.5)) # edge height is 250 so its hypotenuse would be 250sqrt2, times 2 is 500sqrt2
        # did this so that corners would stay on canvas when rotated
        img = Image.new('RGBA', (width, width), (255, 255, 255, 0))
        draw = ImageDraw.Draw(img)
        # setting up the canvas and math stuff
        center = width/2 # self explanatory
        edgeHeight = 250 # distance from center to the outside 
        offset = math.tan(15*math.pi / 180) * 250 # distance of half of the base of an edge 

        draw.polygon((center, center, center-offset, center-edgeHeight, center+offset, center-edgeHeight), fill=colors[sideColor], outline="black")
        edgeHeight *= .65
        offset *= .65
        draw.polygon((center, center, center-offset, center-edgeHeight, center+offset, center-edgeHeight), fill=colors[topColor], outline="black")

        return img.rotate(-degrees)

    def draw_corner(degrees, topColor, sideColors):
        width = int(500*(2**.5))
        img = Image.new('RGBA', (width, width), (255, 255, 255, 0))
        draw = ImageDraw.Draw(img)

        center = width/2
        edgeHeight = 250
        offset = math.tan(15*math.pi / 180) * 250

        draw.polygon((center, center, center+offset, center-edgeHeight, center+edgeHeight, center-edgeHeight), fill=colors[sideColors[0]], outline="black")
        draw.polygon((center, center, center+edgeHeight, center-edgeHeight, center+edgeHeight, center-offset), fill=colors[sideColors[1]], outline="black")
        # draws a polygon for each of the side colors of a corner pieces of which there are 2
        edgeHeight *= .65
        offset *= .65
        draw.polygon((center, center, center+offset, center-edgeHeight, center+edgeHeight, center-edgeHeight, center+edgeHeight, center-offset), fill=colors[topColor], outline="black")
        # draws a smaller version of the previous two polygons, combined
        return img.rotate(-degrees)

    numOfSlices = scramble.count("/")
    scramble = [x.strip(' ') for x in scramble.split("/")]

    if not scramble[-1]:
        del scramble[-1]
    else:
        scramble.append("(0,0)")

    for count, move in enumerate(scramble):
        move = ast.literal_eval(move)
        uFace = np.roll(uFace, move[0])
        dFace = np.roll(dFace, move[1])
        uLayer = np.roll(uLayer, move[0])
        dLayer = np.roll(dLayer, move[1])
        slice()

    img = Image.new('RGBA', (1405, 850), (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)

    uFace = uFace.flatten()
    uLayer = uLayer.flatten()
    dFace = dFace.flatten()
    dLayer = dLayer.flatten()

    i = 0 # iterator, used while loop instead of for loop because I needed a way to jump forward two elements
    x = 0 # x position of the pasted images
    y = 0 # y position of the pasted images
    degrees = 180 # starting orientation of upper face drawings
    currentFace = uFace 
    currentLayer = uLayer
    for j in range(2):
        while i < 12:
            if currentFace[i] == "y2" or currentFace[i] == "w2": # draws an edge
                img.paste(draw_corner(degrees, currentFace[i], currentLayer[i:i+2]), (x,y), mask=draw_corner(degrees, currentFace[i], currentLayer[i:i+2]))
                degrees += 60
                i += 2
            else: # draws a corner
                degrees += 30
                img.paste(draw_edge(degrees, currentFace[i], currentLayer[i]), (x,y), mask=draw_edge(degrees, currentFace[i], currentLayer[i]))
                i += 1
        i = 0 
        x = 700
        degrees = 150
        currentFace = dFace
        currentLayer = dLayer

    # draws the middle layer 
    # also I didn't know how to not use "magic numbers" for this because it was kind of just eyeballed to match cstimer
    draw.rectangle((450,700,600,800), fill="red", outline="black")
    if numOfSlices % 2 == 0:
        draw.rectangle((600,700,950,800), fill="red", outline="black")
    else:
        draw.rectangle((600,700,750,800), fill="orange", outline="black")

    return img
