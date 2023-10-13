
# wumpy   0
# pit     1
# tresure 2
# breeze  3
# stink   4
# shine   5
# location 6

# Game state
# won  1 
# lost 2
# 
#


mapplayer = [
        [[2,0,0,0,0,0,1],[2,0,0,0,0,0,0],[2,0,0,0,0,0,0],[2,0,0,0,0,0,0],[2,0,0,0,0,0,0]],
        [[2,0,0,0,0,0,0],[2,0,0,0,0,0,0],[2,0,0,0,0,0,0],[2,0,0,0,0,0,0],[2,0,0,0,0,0,0]],
        [[2,0,0,0,0,0,0],[2,0,0,0,0,0,0],[2,0,0,0,0,0,0],[2,0,0,0,0,0,0],[2,0,0,0,0,0,0]],
        [[2,0,0,0,0,0,0],[2,0,0,0,0,0,0],[2,0,0,0,0,0,0],[2,0,0,0,0,0,0],[2,0,0,0,0,0,0]],
        [[2,0,0,0,0,0,0],[2,0,0,0,0,0,0],[2,0,0,0,0,0,0],[2,0,0,0,0,0,0],[2,0,0,0,0,0,0]]]
mapwithele = [
        [[0,0,0,0,0,0,0],[0,0,0,1,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,1,0],[0,0,0,0,0,0,0]],
        [[0,0,0,1,0,0,0],[0,1,0,0,0,0,0],[0,0,0,1,0,1,0],[0,0,1,0,0,0,0],[0,0,0,0,0,1,0]],
        [[0,0,0,0,0,0,0],[0,0,0,1,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,1,1,0],[0,0,0,0,0,0,0]],
        [[0,0,0,0,0,0,0],[0,0,0,1,0,0,0],[0,0,0,0,1,0,0],[1,0,0,0,0,0,0],[0,0,0,0,1,0,0]],
        [[0,0,0,1,0,0,0],[0,1,0,0,0,0,0],[0,0,0,1,0,0,0],[0,0,0,0,1,0,0],[0,0,0,0,0,0,0]]]


def gettileinfo(tile):
    op = ""
    if tile[6] == 1:
        op = op + "I AM HERE "    
    elif tile[0] == 2:
        op = op + "N/Y " 
    if tile[0] == 1:
        op = op + "Has Wumpy " 
    if tile[0] == 3:
        op = op + "Has Dead Wumpy "     
    if tile[1] == 1:
        op = op + "Has pit " 
    if tile[2] == 1:
        op = op + "Has tresure " 
    if tile[3] == 1:
        op = op + "Has breez " 
    if tile[4] == 1:
        op = op + "Has stink " 
    if tile[5] == 1:
        op = op + "Has shine " 
    if tile[0] == 0 and tile[1] == 0 and tile[2] == 0 and tile[3] == 0 and tile[4] == 0 and tile[5] == 0:
        op = op +  "nothing "
    
    
    return op

#check if the move is valid etc trying to go out of the map
def checkmovevalid(r, c):
    global row
    global col
    row2 = row + r
    col2 = col + c
    if row2 < 0 or row2 > 4 or col2 < 0 or col2 > 4:
        return False
    else:
        return True

#makes the move and returns 0 if move is invalid
def mover(move):
    global row
    global col
    if move == "u":
        if checkmovevalid(-1, 0):
            updateplayeroldlocation(row, col)
            row = row + -1
            col = col + 0
            if ifgameOver(row, col) == 1:
                return 1
            elif ifgameOver(row, col) == 0:
                return 5
        else:
            return 0
    elif move == "d":
        if checkmovevalid(1, 0):
            updateplayeroldlocation(row, col)
            row = row + 1
            col = col + 0
            if ifgameOver(row, col) == 1:
                return 1
            elif ifgameOver(row, col) == 0:
                return 5
        else:
            return 0
    elif move == "l":
        if checkmovevalid(0, -1):
            updateplayeroldlocation(row, col)
            row = row + 0
            col = col + -1
            if ifgameOver(row, col) == 1:
                return 1
            elif ifgameOver(row, col) == 0:
                return 5
        else:
            return 0
    elif move == "r":
        if checkmovevalid(0, 1):
            updateplayeroldlocation(row, col)
            row = row + 0
            col = col + 1
            if ifgameOver(row, col) == 1:
                return 1
            elif ifgameOver(row, col) == 0:
                return 5
        else:
            return 0
    elif move == "shoot":
        directionShot = shootdirection()
        returnVal = arrowShoot(directionShot)
        if returnVal == 1:
            return 2
        elif returnVal == 0:
            return 3
        elif returnVal == 2:
            #miss
            return 4
    elif move == "e":
        global gamend
        gamend = True
    else:
        return 0

#To shoot arrow
def arrowShoot(direction):
    global row
    global col
    if direction== "u":
        if checkmovevalid(-1, 0) == False:
            return 0
        else:
            for x in range(row-1, -1, -1):
                if mapwithele[x][col][0] == 1:
                    mapwithele[x][col][0] = 3
                    return 1
    elif direction== "d":
        if checkmovevalid(1, 0) == False:
            return 0
        else:
            for x in range(row+1, 5, 1):
                if mapwithele[x][col][0] == 1:
                    mapwithele[x][col][0] = 3
                    return 1
    elif direction== "l":
        if checkmovevalid(0, -1) == False:
            return 0
        else:
            for x in range(col-1, -1, -1):
                if mapwithele[row][x][0] == 1:
                    mapwithele[row][x][0] = 3
                    return 1
    elif direction== "r":
        if checkmovevalid(0, 1) == False:
            return 0
        else:
            for x in range(col+1, 5, 1):
                if mapwithele[row][x][0] == 1:
                    mapwithele[row][x][0] = 3
                    return 1
    return 2


# direction of arrow to shoot
def shootdirection():
    direction = input("Enter direction: ")
    goodInPut = False
    while goodInPut == False:
        if direction== "u":
            goodInPut = True
        elif direction== "d":
            goodInPut = True
        elif direction== "l":
            goodInPut = True
        elif direction== "r":
            goodInPut = True
        else:
            direction = input("Enter correct direction: ")
    return direction

#if the char is dead
def ifgameOver(r , c):

    if mapwithele[r][c][1] == 1 or mapwithele[r][c][0] == 1:
        return 1
    elif mapwithele[r][c][2] == 1:
        return 0

#shows the map for the player
def showplayermap():
    for row in mapplayer:
        for element in row:
            a = gettileinfo(element)
            print(f"{a:<30}" , end="")
        print()
    

# shows map of where everything is placed
def showelemap():
    for row in mapwithele:
        for element in row:
            a = gettileinfo(element)
            print(f"{a:<30}" , end="")
        print()

#updates the players map
def updateplayermap(r , c):
    mapplayer[r][c] = mapwithele[r][c]
    updateplayernewlocation(r, c)

#new player position
def updateplayernewlocation(r , c):
    mapplayer[r][c][6] = 1
#old player position remove
def updateplayeroldlocation(r , c):
    mapplayer[r][c][6] = 0

gamend = False
row = 0
col = 0
gameState = 0

#### 
def movertogo():
    gamestart = True
    global gamend
    while (gamend == False):
        if gamestart == True:
            showplayermap()
            updateplayermap(row , col)
            gamestart = False

        move = input("Enter move: ")
        mademove = mover(move)

        if mademove == 0:
            print("Invalid move re-enter")
        elif mademove == 1:
            gamend = True
            print("You dead")
        elif mademove == 2:
            #gamend = True
            print("Wumpy Dead")
        elif mademove == 3:
            print("Can't shoot")
        elif mademove == 4:
            print("You miss")
        elif mademove == 5:
            gamend = True
            print("You win")
        else:
            print(str(row) + " " + str(col))

        updateplayermap(row , col)
        showplayermap()



def main():
    movertogo()



main()