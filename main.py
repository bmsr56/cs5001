# CS5001 HW2
# Ben Simpson
# 12-12-2018

import numpy as np



# GLOBAL
gamma = 0.8 # discount rate
Qnext = [[[0 for k in range(4)] for j in range(10)] for i in range(10)]
Qprev = [[[0 for k in range(4)] for j in range(10)] for i in range(10)]

up = 0
down = 1   
left = 2
right = 3

directionModifiers = {
    0: (-1, 0) 
}

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
                # for each each action (assumiug always 4)
                for a in range(4):    
                    valtmp = 0.0
                    for 




            # for each newLocation reachable after action a (3 actions, cant go back) 
                valtmp += Prob(location, action, newLocation) * Value(newLocation)
            Qnext[][][] = ExpReward(location, action) + gamma * valtmp

    return

def Prob(location, action, newLocation):
    """ params:
        returns: the probability of reaching newLocation from location if action is taken
    """
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

    if location in cake:
        res = 10.0
    elif location in donut:
        res = 3.0
    elif location in fire:
        res = -5.0
    elif location in monster:
        res = -10.0
    elif (location in walls # checks for walls
            or location[0] in {0, 9}
            or location[1] in {0, 9}):
        res = -1.0
    else:
        print('+++++ Error in Reward +++++')

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