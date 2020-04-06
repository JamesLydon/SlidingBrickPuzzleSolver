# Native Python libraries
import random  # used for random walk
import time  # used for calculating time
import copy  # used for deep copying datasets so that reference data is not overwritten


def main():
    file = "SBP-level0.txt"  # import files from local dir
    gamestate = loadFromDisk(file)
    print("Calculating " + str(file) + " solutions....")
    runSimulation(gamestate)
    file = "SBP-level1.txt"  # import files from local dir
    gamestate = loadFromDisk(file)
    print("\nCalculating " + str(file) + " solutions....")
    runSimulation(gamestate)
    file = "SBP-level2.txt"  # import files from local dir
    gamestate = loadFromDisk(file)
    print("\nCalculating " + str(file) + " solutions....")
    runSimulation(gamestate)
    file = "SBP-level3.txt"  # import files from local dir
    gamestate = loadFromDisk(file)
    print("\nCalculating " + str(file) + " solutions....")
    runSimulation(gamestate)


def runSimulation(file):
    gamestate = file
    print("Beginning state:")  # show the state we loaded from file
    displayState(gamestate)

    # Randomly makes legal moves on the gamestate by some 'count' number of times, or until it finds a solution
    randomWalk(gamestate, 3)

    # Checks layer by layer (breadth) of a tree searching for a solution
    # The answer is always guaranteed, but memory needed to find the solution may be relatively large
    bfs(gamestate)

    # Goes downward (depth) down the length of a tree searching for a solution
    # The answer is guaranteed in this implementation of DFS because it checks for infinite loops.
    # Memory used is relatively more efficient than BFS.
    dfs(gamestate)

    # Iteratively checks the nodes of the tree up to a certain depth (iteratively deepening)
    # The solution is guaranteed with this implementation of IDS
    # Memory used is relatively efficient, unlike BFS. But processing time is extremely long,
    # because many nodes are checked many times. This is particularly true in very large trees.
    ids(gamestate)


# very simple fucnction for loading a file from disk and
# adding it to a list format line by line
def loadFromDisk(file):
    try:
        with open(file) as f:
            gamestate = []
            line = f.readline()
            while line:
                thisline = line.strip().split(',')
                thisline.pop()
                gamestate.append(thisline)
                line = f.readline()
        f.close()
        return gamestate
    except FileNotFoundError:
        print("No such file: " + str(file))


# prints the gamestate in the format specified under the instructions
def displayState(gamestate):
    for gamestatelist in gamestate:
        print(str(gamestatelist).strip("[]").replace("'", "").replace(" ", "") + ",")


# makes a deep copy of the gamestate and returns the copy
def cloneState(gamestate):
    gamestateclone = copy.deepcopy(gamestate)  # a deep copy is used because otherwise reference data might be shared
    return gamestateclone


# given a state, checks if the state has won or not
def puzzleCompleteCheck(gamestate):
    if "-1" in str(gamestate):
        return "False"
    else:
        return "True"


# given a state and a block, calculates what legal moves can be made on the board for that block
def moveOptions(gamestate2, blocknumber):
    gamestate = cloneState(gamestate2)  # gets a fresh new deep clone of the gamestate
    maxwidth = gamestate[0][0]  # gets the width of the board from the first digit in the gamestate
    maxwidth = int(maxwidth) - 1
    maxheight = gamestate[0][1]  # gets the height of the board from the second digit in the gamestate
    maxheight = int(maxheight) - 1
    gamestate.pop(0)  # get rid of the width and height for a second so that they don't get confused as blocks
    movelist = []
    blocklocations = []
    count = 0

    # loop through the locations of each block in the list to calculate the positions of everything
    for blocklocationslist in gamestate:
        for i in range(0, len(blocklocationslist)):
            if int(blocklocationslist[i]) == int(blocknumber):
                blocklocations.append([count, i])
        count += 1

    # loop through the blocks in the list and check where legal moves can be made one by one
    for blocklocationslist in blocklocations:
        height = blocklocationslist[0]
        width = blocklocationslist[1]
        # check north
        if height == 0 or int(gamestate[(height - 1)][width]) == 1:  # checks the north direction first
            northlist = [height, width, 'northfalse']
            movelist.append(northlist)
        elif int(gamestate[(height - 1)][width]) == int(blocknumber) or int(gamestate[(height - 1)][width]) == 0:
            northlist = [height, width, 'north']
            movelist.append(northlist)
        elif int(gamestate[(height - 1)][width]) == -1 and blocknumber == 2:
            northlist = [height, width, 'north']
            movelist.append(northlist)
        else:
            northlist = [height, width, 'northfalse']
            movelist.append(northlist)
        # check south
        if height == maxheight or int(gamestate[(height + 1)][width]) == 1:  # checks the south direction next
            southlist = [height, width, 'southfalse']
            movelist.append(southlist)
        elif int(gamestate[(height + 1)][width]) == int(blocknumber) or int(gamestate[(height + 1)][width]) == 0:
            southlist = [height, width, 'south']
            movelist.append(southlist)
        elif int(gamestate[(height + 1)][width]) == -1 and blocknumber == 2:
            southlist = [height, width, 'south']
            movelist.append(southlist)
        else:
            southlist = [height, width, 'southfalse']
            movelist.append(southlist)
        # check west
        if width == 0 or int(gamestate[height][width - 1]) == 1:  # checks the west direction next
            westlist = [height, width, 'westfalse']
            movelist.append(westlist)
        elif int(gamestate[height][width - 1]) == int(blocknumber) or int(gamestate[height][width - 1]) == 0:
            westlist = [height, width, 'west']
            movelist.append(westlist)
        elif int(gamestate[height][width - 1]) == -1 and blocknumber == 2:
            westlist = [height, width, 'west']
            movelist.append(westlist)
        else:
            westlist = [height, width, 'westfalse']
            movelist.append(westlist)
        # check east
        if height == maxwidth or int(gamestate[height][width + 1]) == 1:  # checks the east direction last
            eastlist = [height, width, 'eastfalse']
            movelist.append(eastlist)
        elif int(gamestate[height][width + 1]) == int(blocknumber) or int(gamestate[height][width + 1]) == 0:
            eastlist = [height, width, 'east']
            movelist.append(eastlist)
        elif int(gamestate[height][width + 1]) == -1 and blocknumber == 2:
            eastlist = [height, width, 'east']
            movelist.append(eastlist)
        else:
            eastlist = [height, width, 'eastfalse']
            movelist.append(eastlist)

    north = 'north'
    south = 'south'
    west = 'west'
    east = 'east'
    # do this to simply check whether or not a direction is INVALID or not
    for blocklocationslist in movelist:
        if 'northfalse' in blocklocationslist:
            north = 'northfalse'
        if 'southfalse' in blocklocationslist:
            south = 'southfalse'
        if 'westfalse' in blocklocationslist:
            west = 'westfalse'
        if 'eastfalse' in blocklocationslist:
            east = 'eastfalse'

    return [north, south, west, east]


# given a gamestate, calculates all of the moveoptions for every single block on the board
def allMoveOptions(gamestate1):
    gamestate = cloneState(gamestate1)  # gets a fresh new deep clone of the gamestate
    maxwidth = gamestate[0][0]  # gets the width of the board from the first digit in the gamestate
    maxwidth = int(maxwidth)
    maxheight = gamestate[0][1]  # gets the height of the board from the first digit in the gamestate
    maxheight = int(maxheight)
    gamestate.pop(0)

    mastermovelist = []
    blocknumbers = []

    # loop through the positions in the board one by one to find the blocks
    ycount = 0
    while ycount < maxheight:
        xcount = 0
        while xcount < maxwidth:
            if int(gamestate[ycount][xcount]) > 1 and int(gamestate[ycount][xcount]) not in blocknumbers:
                blocknumbers.append(int(gamestate[ycount][xcount]))
            xcount += 1
        ycount += 1
    # calculate the move options for each block that's on the board
    for block in blocknumbers:
        blockMoveOptions = moveOptions(gamestate1, block)
        for move in blockMoveOptions:
            if 'false' in str(move):
                continue
            else:
                mastermovelist.append([block, move])
    return mastermovelist
    # return a full list of all of the moves


# given a move, applies the move to the move's gamestate and returns the gamestate
def applyMove(move):
    gamestate1 = move.gamestate  # get the gamestate from the move class move passed in
    gamestate = cloneState(gamestate1)  # make a fresh new deep clone of the gamestate
    gamestateHeightWidth = gamestate[0]  # temporarily take out the height/width of the board
    gamestate.pop(0)
    blocklocations = []
    count = 0
    for blocklocationslist in gamestate:  # get the set of blocks from the gamestate one by one
        for i in range(0, len(blocklocationslist)):
            if int(blocklocationslist[i]) == int(move.block):
                blocklocations.append([count, i])
        count += 1
    # for each of the possible directions the move is, apply that direction and overwrite the space it's moving from
    if move.direction == "north":
        for blocklocationslist in blocklocations:
            height = blocklocationslist[0]
            width = blocklocationslist[1]
            gamestate[(height - 1)][width] = int(move.block)
            gamestate[height][width] = 0
    if move.direction == "south":
        for blocklocationslist in reversed(blocklocations):
            height = blocklocationslist[0]
            width = blocklocationslist[1]
            gamestate[(height + 1)][width] = int(move.block)
            gamestate[height][width] = 0
    if move.direction == "west":
        for blocklocationslist in blocklocations:
            height = blocklocationslist[0]
            width = blocklocationslist[1]
            gamestate[height][width - 1] = int(move.block)
            gamestate[height][width] = 0
    if move.direction == "east":
        for blocklocationslist in reversed(blocklocations):
            height = blocklocationslist[0]
            width = blocklocationslist[1]
            gamestate[height][width + 1] = int(move.block)
            gamestate[height][width] = 0
    gamestate.insert(0, gamestateHeightWidth)
    return gamestate


# the move class represents a legal move that can be made on the board
# it contains a block, a direction to move, and the gamestate configuration before the move is performed
class move:
    def __init__(self, block, direction, gamestate):
        self.block = block
        self.direction = direction
        self.gamestate = gamestate

    def change_block(self, block):
        self.block = block

    def change_gamestate(self, gamestate):
        self.gamestate = gamestate

    def change_direction(self, direction):
        self.direction = direction


# given two gamestates, check if they're equivalent or not
def StateComparison(gamestatea, gamestateb):
    gamestate1 = cloneState(gamestatea)
    gamestate2 = cloneState(gamestateb)  # get fresh new copies of each gamestate

    maxwidth1 = gamestate1[0][0]
    maxwidth1 = int(maxwidth1) - 1
    maxheight1 = gamestate1[0][1]
    maxheight1 = int(maxheight1) - 1  # get heights and widths of both gamestates
    maxwidth2 = gamestate2[0][0]
    maxwidth2 = int(maxwidth2) - 1
    maxheight2 = gamestate2[0][1]
    maxheight2 = int(maxheight2) - 1
    if maxheight1 != maxheight2 or maxwidth1 != maxwidth2:  # right away we can discard the comparison if the heights
        # and widths are different
        return "false"
    gamestate1.pop(0)
    gamestate2.pop(0)  # pop the first line off the gamestate temporarily so that they don't get in the way

    ycount = 0  # iteratively check each place in the gamestate for discrepancies
    while ycount < maxheight1:
        xcount = 0
        while xcount < maxwidth1:
            if int(gamestate1[ycount][xcount]) != int(gamestate2[ycount][xcount]):
                return "false"
            xcount += 1
        ycount += 1
    return "true"


# "Normalizes" a gamestate. That is, converts the gamestate into an equivalent gamestate represented
# by some universal pattern
def normalization(gamestate1):
    gamestate = cloneState(gamestate1)  # get a fresh new copy of this state
    maxwidth = gamestate[0][0]  # get the width and height from the first line
    maxwidth = int(maxwidth)
    maxheight = gamestate[0][1]
    maxheight = int(maxheight)
    gamestateHeightWidth = gamestate[0]
    gamestate.pop(0)

    # start at 3, because 0's are walls, -1's are goal states, and 2's are the goal block
    nextIdx = 3
    ycount = 0
    # iteratively move through the board and rename each block to an iterative index, left to right, top to bottom
    while ycount < maxheight:
        xcount = 0
        while xcount < maxwidth:
            if int(gamestate[ycount][xcount]) == nextIdx:
                nextIdx += 1
            elif int(gamestate[ycount][xcount]) > nextIdx:
                gamestate = swapIdx(nextIdx, int(gamestate[ycount][xcount]), gamestate, maxheight, maxwidth)
                nextIdx += 1
            xcount += 1
        ycount += 1
    gamestate.insert(0, gamestateHeightWidth)
    return gamestate


# used by the normalize function, straightforwardly swaps the index of a block with its neighbor
def swapIdx(idx1, idx2, gamestate, maxheight, maxwidth):
    ycount = 0
    while ycount < maxheight:
        xcount = 0
        while xcount < maxwidth:
            if int(gamestate[ycount][xcount]) == idx1:
                gamestate[ycount][xcount] = idx2
            elif int(gamestate[ycount][xcount]) == idx2:
                gamestate[ycount][xcount] = idx1
            xcount += 1
        ycount += 1
    return gamestate


# Randomly makes legal moves on the gamestate by some 'count' number of times, or until it finds a solution
def randomWalk(gamestate1, count):
    print("\nRandom walk with maximum " + str(count) + " moves performed:")
    originalcount = count  # keep the original count in memory to determine how many moves were made in total later
    gamestate = cloneState(gamestate1)  # get fresh new copy of the gamestate
    while True:
        if count == 0:
            print("Ran out of all " + str(originalcount) + " moves without finding a solution.")  # print lose screen
            displayState(gamestate)
            break
        elif puzzleCompleteCheck(gamestate) == "True":  # print win screen with number of moves made
            print("You won!! And it only took " + str(originalcount - count) + " moves!")
            displayState(gamestate)
            break
        else:  # get all of the possible legal moves. randomly choose one
            availableMoves = allMoveOptions(gamestate)
            randomBlock = random.choice(availableMoves)
            randomMove = [randomBlock[0], randomBlock[1]]
            if 'false' in randomMove[1]:
                continue
            else:
                movetomake = move(randomMove[0], randomMove[1], gamestate)
                print(str(randomMove))
                gamestate = applyMove(movetomake)  # apply the randommove to the board
                count -= 1


# Checks layer by layer (breadth) of a tree searching for a solution
# The answer is always guaranteed, but memory needed to find the solution may be relatively large
def bfs(gamestate1):
    print("\nBreadth-first search Calculating...")
    start_time = time.time()  # start counting time so we know how long this search took later
    checked = []  # list keeps track of which normalized gamestates we've already seen
    nodespathcounter = 0  # counter that increments for each new node we find. helps in uniquely ID'ing nodes
    nodespath = {}  # list keeps track of every single node we've found and who its parent node is
    queue = []  # queue is used in breadth first searching to check the nodes in a FIFO fashion
    gamestate = cloneState(gamestate1)  # make a fresh new gamestate clone
    gamestate = normalization(gamestate)  # normalize it to be safe in gamestate comparisons
    checked.append(gamestate)  # add this starting state to the list of checked configurations
    nodespath[nodespathcounter] = [-1, -1]  # give the root node dummy data so we know if we hit it later
    availableMoves = allMoveOptions(gamestate)  # calculate the beginning moves for the gamestate
    parentnodecount = 0
    thisnodenumber = 0
    while availableMoves:  # add each of the available moves at the beginning state to the queue
        tempmove = availableMoves.pop(0)
        tempgamestate = cloneState(gamestate)
        queuemove = move(tempmove[0], tempmove[1], tempgamestate)
        nodespathcounter += 1
        queue.append([queuemove, parentnodecount, nodespathcounter])
        nodespath[nodespathcounter] = [queuemove, parentnodecount]

    while True:
        if puzzleCompleteCheck(gamestate) == "True":
            # before doing anything with the current gamestate, check if we've won now
            stepsToWin = []
            stepsToWinCounter = 0
            while True:
                nodeParentandAction = nodespath.get(thisnodenumber)  # get the winning node number
                nodeMove = nodeParentandAction[0]  # check if the parent was the root
                if nodeMove == -1:
                    break
                else:  # trace our way back to the top of the tree to figure out which moves got us to this goal
                    action = [nodeMove.block, nodeMove.direction]
                    parentnodecount = int(nodeParentandAction[1])
                    thisnodenumber = parentnodecount
                    stepsToWin.append(action)
                    stepsToWinCounter += 1
            for actions in reversed(stepsToWin):  # print the winning moves
                print(str(actions))
            displayState(gamestate)  # print the final gamestate
            print("Explored " + str(nodespathcounter) + " nodes in " + str(time.time() - start_time) + " seconds. "
                                                                                                       "Solution "
                                                                                                       "takes " +
                  str(stepsToWinCounter) + " steps.")
            break

        else:
            path = queue.pop(0)  # get the first node in the queue
            thisnodenumber = path[2]  # get the number of the node we're working with in this iteration
            pathmove = path[0]  # get the move this node wants to make
            tempgamestate = cloneState(gamestate)  # get a fresh new gamestate to work with
            tempgamestate = pathmove.gamestate  # copy the move's gamestate to it
            tempgamestate = applyMove(path[0])  # apply the move's move to the gamestate
            normalizedgamestate = normalization(tempgamestate)  # normalize this gamestate so that we can compare it
            # to gamestates we might have previously encountered
            copystate = "false"
            for eachgamestate in checked:  # compare this gamestate to every gamestate we've seen before
                copy = StateComparison(normalizedgamestate, eachgamestate)
                if copy == "true":
                    copystate = "true"
                    del nodespath[thisnodenumber]  # delete this node if it's just a copy
            if copystate == "true":
                continue  # get out of this iteration and move on to the next one
            gamestate = pathmove.gamestate
            gamestate = applyMove(path[0])  # apply the move to this non-normalized gamestate
            availableMoves = allMoveOptions(gamestate)  # calculate the new available moves now
            parentnodecount = thisnodenumber  # make a note of who the parent of these new nodes will be
            while availableMoves:  # iteratively add all of these new nodes to the tree
                tempmove = availableMoves.pop(0)
                tempgamestate = cloneState(gamestate)
                queuemove = move(tempmove[0], tempmove[1], tempgamestate)
                nodespathcounter += 1
                queue.append([queuemove, parentnodecount, nodespathcounter])
                nodespath[nodespathcounter] = [queuemove, parentnodecount]
            checked.append(normalizedgamestate)


# Goes downward (depth) down the length of a tree searching for a solution
# The answer is guaranteed in this implementation of DFS because it checks for infinite loops.
# Memory used is relatively more efficient than BFS.
def dfs(gamestate1):
    print("\nDepth-first search Calculating...")
    start_time = time.time()  # start counting time so we know how long this search took later
    checked = []  # list keeps track of which normalized gamestates we've already seen
    nodespathcounter = 0  # counter that increments for each new node we find. helps in uniquely ID'ing nodes
    nodespath = {}  # list keeps track of every single node we've found and who its parent node is
    stack = []  # stack is used in depth first searching to check the nodes in a LIFO fashion
    gamestate = cloneState(gamestate1)  # make a fresh new gamestate clone
    gamestate = normalization(gamestate)  # normalize it to be safe in gamestate comparisons
    checked.append(gamestate)  # add this starting state to the list of checked configurations
    nodespath[nodespathcounter] = [-1, -1]  # give the root node dummy data so we know if we hit it later
    availableMoves = allMoveOptions(gamestate)  # calculate the beginning moves for the gamestate
    parentnodecount = 0
    while availableMoves:
        tempmove = availableMoves.pop(0)  # add each of the available moves at the beginning state to the queue
        tempgamestate = cloneState(gamestate)
        stackmove = move(tempmove[0], tempmove[1], tempgamestate)
        stack.append([stackmove, nodespathcounter, parentnodecount])
        nodespathcounter += 1
        nodespath[nodespathcounter] = [stackmove, parentnodecount]

    while True:
        if puzzleCompleteCheck(gamestate) == "True":
            # before doing anything with the current gamestate, check if we've won now
            stepsToWin = []
            stepsToWinCounter = 0
            while True:
                nodeParentandAction = nodespath.get(parentnodecount)  # get the winning node number
                nodeMove = nodeParentandAction[0]  # check if the parent was the root
                if nodeMove == -1:
                    break
                else:  # trace our way back to the top of the tree to figure out which moves got us to this goal
                    action = [nodeMove.block, nodeMove.direction]
                    parentnodecount = int(nodeParentandAction[1])
                    stepsToWin.append(action)
                    stepsToWinCounter += 1
            for actions in reversed(stepsToWin):  # print the winning moves
                print(str(actions))
            displayState(gamestate)  # print the final gamestate
            print("Explored " + str(nodespathcounter) + " nodes in " + str(time.time() - start_time) + " seconds. "
                                                                                                       "Solution "
                                                                                                       "takes " +
                  str(stepsToWinCounter) + " steps.")
            break
        else:
            path = stack.pop(-1)  # get the last node in the stack
            pathmove = path[0]  # get the move this node wants to make
            tempgamestate = cloneState(gamestate)  # get a fresh new gamestate to work with
            tempgamestate = pathmove.gamestate  # copy the move's gamestate to it
            tempgamestate = applyMove(path[0])  # apply the move's move to the gamestate
            normalizedgamestate = normalization(tempgamestate)  # normalize this gamestate so that we can compare it
            # to gamestates we might have previously encountered
            copystate = "false"
            for eachgamestate in checked:  # compare this gamestate to every gamestate we've seen before
                copy = StateComparison(normalizedgamestate, eachgamestate)
                if copy == "true":
                    copystate = "true"
                    del nodespath[nodespathcounter]  # delete this node if it's just a copy
                    nodespathcounter -= 1
            if copystate == "true":
                continue  # get out of this iteration and move on to the next one
            gamestate = pathmove.gamestate
            gamestate = applyMove(path[0])  # apply the move to this non-normalized gamestate
            availableMoves = allMoveOptions(gamestate)  # calculate the new available moves now
            parentnodecount = nodespathcounter  # make a note of who the parent of these new nodes will be
            while availableMoves:  # iteratively add all of these new nodes to the tree
                tempmove = availableMoves.pop(0)
                tempgamestate = cloneState(gamestate)
                stackmove = move(tempmove[0], tempmove[1], tempgamestate)
                stack.append([stackmove, nodespathcounter])
                nodespathcounter += 1
                nodespath[nodespathcounter] = [stackmove, parentnodecount]
            checked.append(normalizedgamestate)


# Iteratively checks the nodes of the tree up to a certain depth (iteratively deepening)
# The solution is guaranteed with this implementation of IDS
# Memory used is relatively efficient, unlike BFS. But processing time is extremely long,
# because many nodes are checked many times. This is particularly true in very large trees.
def ids(gamestate1):
    print("\nIterative Deepening search Calculating...")
    depth = 1  # start counting time so we know how long this search took later
    start_time = time.time()  # list keeps track of which normalized gamestates we've already seen
    found = "false"  # keep track of whether or not we've found a solution
    while found == "false":  # loop forever until a solution is found
        checked = []  # list keeps track of which normalized gamestates we've already seen
        nodespathcounter = 0  # counter that increments for each new node we find. helps in uniquely ID'ing nodes
        nodespath = {}  # list keeps track of every single node we've found and who its parent node is
        stack = []  # stack is used in iterative deepening search to check the nodes in a LIFO fashion
        gamestate = cloneState(gamestate1)  # make a fresh new gamestate clone
        gamestate = normalization(gamestate)  # normalize it to be safe in gamestate comparisons
        checked.append(gamestate)  # add this starting state to the list of checked configurations
        nodespath[nodespathcounter] = [-1, -1]  # give the root node dummy data so we know if we hit it later
        availableMoves = allMoveOptions(gamestate)  # calculate the beginning moves for the gamestate
        parentnodecount = 0
        thisnodenumber = 0
        while availableMoves:  # add each of the available moves at the beginning state to the queue
            tempmove = availableMoves.pop(0)
            tempgamestate = cloneState(gamestate)
            stackmove = move(tempmove[0], tempmove[1], tempgamestate)
            nodespathcounter += 1
            stack.append([stackmove, parentnodecount, nodespathcounter, depth - 1])
            nodespath[nodespathcounter] = [stackmove, parentnodecount]

        while True:
            if puzzleCompleteCheck(gamestate) == "True":
                # before doing anything with the current gamestate, check if
                # we've won now
                stepsToWin = []
                stepsToWinCounter = 0
                while True:
                    nodeParentandAction = nodespath.get(thisnodenumber)  # get the winning node number
                    nodeMove = nodeParentandAction[0]  # check if the parent was the root
                    if nodeMove == -1:
                        break
                    else:  # trace our way back to the top of the tree to figure out which moves got us to this goal
                        action = [nodeMove.block, nodeMove.direction]
                        parentnodecount = int(nodeParentandAction[1])
                        thisnodenumber = parentnodecount
                        stepsToWin.append(action)
                        stepsToWinCounter += 1
                for actions in reversed(stepsToWin):  # print the winning moves
                    print(str(actions))
                displayState(gamestate)  # print the final gamestate
                print("Explored " + str(nodespathcounter) + " nodes in " + str(time.time() - start_time) + " seconds. "
                                                                                                           "Solution "
                                                                                                           "takes " +
                      str(stepsToWinCounter) + " steps.")
                found = "true"
                break
            else:
                try:
                    path = stack.pop(-1)  # get the last node in the stack
                    thisnodenumber = path[2]  # get the number of the node we're working with in this iteration
                    currentdepth = path[3]  # keep track of what the current depth is
                    if int(currentdepth) < 0:  # if our depth is further than we want to check at this point,
                        # continue to the next node
                        continue
                    pathmove = path[0]  # get the move this node wants to make
                    tempgamestate = cloneState(gamestate)  # get a fresh new gamestate to work with
                    tempgamestate = pathmove.gamestate  # copy the move's gamestate to it
                    tempgamestate = applyMove(path[0])  # apply the move's move to the gamestate
                    normalizedgamestate = normalization(tempgamestate)  # normalize this gamestate so that we can
                    # compare it to gamestates we might have previously encountered
                    copystate = "false"
                    for eachgamestate in checked:  # compare this gamestate to every gamestate we've seen before
                        copy = StateComparison(normalizedgamestate, eachgamestate)
                        if copy == "true":
                            copystate = "true"
                            del nodespath[thisnodenumber]  # delete this node if it's just a copy
                    if copystate == "true":
                        continue  # get out of this iteration and move on to the next one
                    gamestate = pathmove.gamestate
                    gamestate = applyMove(path[0])  # apply the move to this non-normalized gamestate
                    availableMoves = allMoveOptions(gamestate)  # calculate the new available moves now
                    parentnodecount = thisnodenumber  # make a note of who the parent of these new nodes will be
                    while availableMoves:  # iteratively add all of these new nodes to the tree
                        tempmove = availableMoves.pop(0)
                        tempgamestate = cloneState(gamestate)
                        stackmove = move(tempmove[0], tempmove[1], tempgamestate)
                        nodespathcounter += 1
                        stack.append([stackmove, parentnodecount, nodespathcounter, currentdepth - 1])
                        nodespath[nodespathcounter] = [stackmove, parentnodecount]
                    checked.append(normalizedgamestate)
                # if the stack is empty, we know we've checked all of the nodes in the tree up to this depth
                except IndexError:
                    break
        # iterate through again going incrementally deeper
        depth += 1


main()
