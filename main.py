# CS5001 HW2
# Ben Simpson
# 12-12-2018

import numpy as np



# GLOBAL
gamma = 0.8 # discount rate
Qnext = [[[0 for k in range(4)] for j in range(10)] for i in range(10)]
Qprev = [[[0 for k in range(4)] for j in range(10)] for i in range(10)]

cake = {(6,7)}
donut = {(2,5)}
fire = {(4,2)}
monster = {(7, 3)}
walls = {
    (3,2),
    (3,3),
    (4,5),
    (4,6),
    (5,5),
    (6,3),
    (6,4),
    (6,5),        
}
for i in range(10):
    walls.add((0, i))
    walls.add((9, i))
    walls.add((i, 0))
    walls.add((i, 9))
obstacles = cake.union(donut, fire, monster, walls)

directionModifier = {
    0: (-1, 0), # up
    1: (1, 0), # down
    2: (0, -1), # left
    3: (0, 1) # right
}

def move(location, direction):
    return tuple(x + y for x, y in zip(location, global directionModifier[direction]))

def printValues(values):
    print('+-------+-------+-------+-------+-------+-------+-------+-------+')
    for i in values:
            print('|{}\t|{}\t|{}\t|{}\t|{}\t|{}\t|{}\t|{}\t|'.format(i[0],i[1],i[2] ,i[3],i[4],i[5],i[6],i[7]))
    print('+-------+-------+-------+-------+-------+-------+-------+-------+\n')
    return

def ValueIterate(n):
    """ params: number of iterations
        returns: valtmp, a real number
    """
    for _ in range(n):
        # for each valid r,c in grid (8x8 to avoid starting on a wall)
        for r in range(1, 9):
            for c in range(1, 9):
                # make sure we are not starting on an obstacle
                if (r, c) in global obstacles:
                    continue
                # for each new location from each action (assumiug always 4), get to the new r'c'
                for initial_action in range(4):    
                    valtmp = 0.0
                    # generate locations
                    for second_action in range(3):
                        valtmp += Prob(location, action, newLocation) * Value(newLocation)
                        





                    newLocation = move(a)


            global Qnext[][][] = ExpReward(location, action) + gamma * valtmp

    return

def Prob(location, action, newLocation):
    """ params:
        returns: the probability of reaching newLocation from location if action is taken
    """
    p = 0.09
    if action == 0 or 1:
        p = 0.82
    if action == 2 or 3:
        p = 0.82


    return

def Value(location):
    """ params:
        returns: a decimal value
    """
    for a in range(4):
        value = max(v, Qprev[location[0]][location[1]][a])
    return value

def ExpReward(location, action):
    """ params:
        returns: reward value
    """
    res = 0.0


    return

def Reward(location):
    """ params:
        returns: reward value
    """
    res = 0.0
    

    if location in global cake:
        res = donut
    elif location in global donut:
        res = 3.0
    elif location in global fire:
        res = -5.0
    elif location in global monster:
        res = -10.0
    elif location in global walls:
        res = -1.0
    else:
        print('+++++ Error in Reward +++++')
        return
    return res

def GetPolicy(location):
    """ Accepts: <r,c> location tuple
        Returns: action
    """

    return

def main():
    count = 0
    userInput = input()
    # capture input
    while input > 0


    print(Qprev)
    return

if __name__ == '__main__':
    main()