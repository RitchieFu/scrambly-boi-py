from PIL import Image, ImageDraw # only import

def clockimage(scramble): # scramble goes here and is split here
    scramble = scramble.split()
        
    front = [0,0,0,0,0,0,0,0,0] 
    back = [0,0,0,0,0,0,0,0,0] # lists for the front and back faces of the clock
    current, other = front, back # variables to help determine which face is the "current" one with moves being done to it

    corners = [0,2,6,8]
    mirrored = [2,0,8,6] 
    # lists for the corners to update them after each move, as they are connected in the real puzzle
    # the reason why there are two is because the corners are mirrored
    # maybe mirror everything after instead of this solution??
    UL = [0,1,3,4]
    U = [0,1,2,3,4,5]
    UR = [1,2,4,5]
    R = [1,2,4,5,7,8]
    DR = [4,5,7,8]
    D = [3,4,5,6,7,8]
    DL = [3,4,6,7]
    L = [0,1,3,4,6,7]
    ALL = [0,1,2,3,4,5,6,7,8] # lists for which mini-clocks are affected by the turns

    moveMap = {
        "UL":UL, "U":U, "UR":UR, "R":R, "DR":DR, "D":D, "DL":DL, "L":L, "ALL":ALL
    }
    # dictionary for which list to use for the turn
    pins = {
        "UL":False, "UR":False, "DL":False, "DR":False
    }
    # used to determine the state of the pins (up/down)
    # maybe there is better way of doing this??
    for move in scramble:
        if len(move) == 2: # if the move is either y2 or one of the the pins going up/down
            if move == "y2":
                if current == front:
                    current, other = back, front # switches the current face from back to front and vice versa
                else:
                    current, other = front, back
            else:
                pins[move] = True 
                # this assumes that a pin was the move and it is now being pressed up
                # need to account for multiple pin moves as it will not stay True or False
                # currently not an issue due to the way the scrambles are for clocks
            continue
        
        dial = move[:-2] # which dials one would rotate for the move
        turn = int(move[-2]) # how many hours to turn
        direction = move[-1] # which direction to turn those hours
        if direction == "-": turn = -turn # did this so I didn't have to do -= decrement later
        
        for a in moveMap[dial]: # for each mini-clock in corresponding move/dials, turn by correct amount of hours
            current[a] += turn

        for i in range(len(current)): # keeps the numbers between [1, 12]
            while current[i] < 0:
                current[i] += 12
            while current[i] > 12:
                current[i] -= 12
            
        for i in range(4): # updates the corners as they are connected
            other[corners[i]] = 12 - current[mirrored[i]]

    def hour_hand(degrees: int, fill: str, outline: str): 
        # function to draw the hour hand for the image
        # did this so I didn't have to do math to determine exact coordinates as this just rotates the image and pastes it to final image
        hour = Image.new('RGBA', (150, 150), (255, 255, 255, 0))
        draw = ImageDraw.Draw(hour)

        draw.ellipse((0,0,150,150), fill=fill, outline=outline, width=65)
        draw.polygon((65,75,75,0,85,75), fill=fill)

        hour = hour.rotate(-degrees) # default goes counter clockwise so I needed to change it to clockwise
        return hour

    img = Image.new('RGBA', (1125, 550), (255, 255, 255, 0)) # setting up canvas
    draw = ImageDraw.Draw(img)

    x, y, z = 25, 25, 0 # mini-clock 1 on front side starts at 25, 25; z is an iterator
    handColor, bgColor, face = "black", "white", current # color of the hour hand, color of background, face being iterated
    for i in range(2): # does twice because there are two faces
        for j in range(3): # three rows
            for k in range(3): # three columns
                img.paste(hour_hand(face[z]*30, handColor, bgColor), (x,y,x+150,y+150)) # each mini-clock is 150x150
                x += 175 # gap between mini-clocks of 25
                z += 1 # increments to next element in current face
            x -= 525 # resets x to 25
            y += 175 # drops down a row
        x, y, z = 600, 25, 0 # coordinates of second clock face
        handColor, bgColor, face = "white", "black", other # swaps colors and face

    # drawing the pins
    x, y, z = 165, 165, 0 # starts at 165, 165
    pinBool = True # if pin is True/up, it will be colored white with outline of black and vice versa
    pinVals = list(pins.values()) # list of the states of the pins
    for i in range(2):
        for j in range(2):
            for k in range(2):
                if pinVals[z] is pinBool:
                    inner, outer = "white", "black"
                else:
                    inner, outer = "black", "white"
                draw.ellipse((x,y,x+45,y+45), fill=inner, outline=outer, width=2)
                x += 175 # same gap as between mini-clocks
                z += 1
            x -= 350 # resets x to 165
            y += 175 # drops down a row
        x, y, z = 740, 165, 0 # coordinates of other face's pins
        pinBool = False # pins must be inverted in colors
        pinVals[0], pinVals[1] = pinVals[1], pinVals[0]
        pinVals[2], pinVals[3] = pinVals[3], pinVals[2] # pins must also be flipped along the y-axis
        
    return img # show the image