# CS5001 HW2
# Ben Simpson
# 12-12-2018

import numpy as np
import copy
import pprint

# GLOBAL

gamma = 0.8 # discount rate

# Actions will be stored in this order in the k dimension: UP RIGHT DOWN LEFT
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
    1: (0, 1), # right
    2: (1, 0), # down
    3: (0, -1) # left
}

directions = {
    0: '^',
    1: '>',
    2: 'v',
    3: '<'
}

def move(location, direction):
    global directionModifier
    return tuple(x + y for x, y in zip(location, directionModifier[direction]))

def ValueIterate(n):
    """ params: number of iterations
        returns: valtmp, a real number
    """
    for _ in range(n):
        global obstacles
        global Qnext
        global Qprev
        global gamma

        # for each valid r,c in grid (8x8 to avoid starting on a wall)
        for r in range(1, 9):

            for c in range(1, 9):

                location = (r, c)

                # make sure we are not starting on an obstacle
                if (r, c) in obstacles:
                    continue

                # for each new location from each action, generate all r'c' states
                for action in range(4):
                    valtmp = 0.0
                    # determine possible action directions with given action
                    possible_actions = [action]

                    if action % 2 == 0:
                        possible_actions.append(1)
                        possible_actions.append(3)
                    else:
                        possible_actions.append(0)
                        possible_actions.append(2)
                        
                    for p_action in possible_actions:
                        location_prime = move(location, p_action)
                        valtmp += Prob(action, p_action) * Value(location_prime)

                    Qnext[r][c][action] = ExpReward(location, action, possible_actions) + gamma * valtmp
        Qprev = copy.deepcopy(Qnext)
    
    return

def Prob(action, p_action):
    """ params:
        returns: the probability of reaching a new location from location if an action is taken
    """
    p = 0.09
    if p_action == action:
        p = 0.82
    return p

def Value(location):
    """ params:
        returns: a decimal value
    """
    v = -1337
    for a in range(4):
        v = max(v, Qprev[location[0]][location[1]][a])
    return v

def ExpReward(location, action, possible_actions):
    """ params:
        returns: reward value
    """
    res = 0.0
    for p_action in possible_actions:
        newLocation = move(location, p_action)
        res += Prob(action, p_action) * Reward(newLocation)
    return res

def Reward(location):
    """ params:
        returns: reward value
    """
    res = 0.0
    global cake
    global donut
    global fire
    global monster
    global walls

    if location in cake:
        res = 10.0
    elif location in donut:
        res = 3.0
    elif location in fire:
        res = -5.0
    elif location in monster:
        res = -10.0
    elif location in walls:
        res = -1.0
    return res

def GetPolicy(location):
    """ Accepts: <r,c> location tuple
        Returns: action
    """
    global Qprev
    v = -1337
    for r in range(1,9):
        for c in range(1,9):        
            for a in range(4):
                if Qprev[r][c][a] > v:
                    policy_action = a
                    v = Qprev[r][c][a]
    return policy_action

def printFrame(data):
    print('+-------+-------+-------+-------+-------+-------+-------+-------+')
    for i in data:
            print('|{}\t|{}\t|{}\t|{}\t|{}\t|{}\t|{}\t|{}\t|'.format(i[0],i[1],i[2] ,i[3],i[4],i[5],i[6],i[7]))
    print('+-------+-------+-------+-------+-------+-------+-------+-------+\n')
    return

def printResults(qtable, option):
    global cake
    global donut
    global fire
    global monster
    global walls

    rowsToPrint = []
    for r in range(1, 9):
        tmpRow = []
        for c in range(1, 9):
            if (r, c) in cake:
                tmpRow.append('CAKE')
            elif (r, c) in donut:
                tmpRow.append('DONUT')
            elif (r, c) in monster:
                tmpRow.append('DEMON')
            elif (r, c) in walls:
                tmpRow.append('XXX')
            elif (r, c) in fire:
                tmpRow.append('FIRE')
            elif option == 'v':
                tmpRow.append(round(max(qtable[r][c]), 3))
            elif option == 'p':
                i = qtable[r][c].index(max(qtable[r][c]))
                tmpRow.append(directions[i])
        rowsToPrint.append(tmpRow)

    printFrame(rowsToPrint)

def main():
    global Qprev
    count = 0
    iterations = 1
    # capture input
    while iterations > 0:
        print('Enter No of Iterations: ')
        iterations = int(input())
        if iterations == 0:
            break
        count = count + iterations
        print('Value after {} iterations:\n'.format(count))
        ValueIterate(iterations)
        printResults(Qprev, 'v')
    # print the policy
    print('Policy:\n')
    printResults(Qprev, 'p')
    return

if __name__ == '__main__':
    print('CS-5001: HW2')
    print('Programmer: Ben Simpson')
    print('Discount Gamma = {}'.format(gamma))

    main()