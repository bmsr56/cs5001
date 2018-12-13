# CS5001 HW2
# Ben Simpson
# 12-12-2018

import numpy as np



# GLOBAL
gamma = 0.8 # discount rate
# Actions are stored in this order: UP RIGHT DOWN LEFT
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
    1: (0, 1) # right
    2: (1, 0), # down
    3: (0, -1), # left
}

directions = [0, 1, 2, 3] #urdl


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

                location = (r, c)

                valtmp = 0.0

                # make sure we are not starting on an obstacle
                if (r, c) in global obstacles:
                    continue

                # for each new location from each action, generate all r'c' states
                for action in range(4):

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

                    global Qnext[r][c][action] = ExpReward(location, action, possible_actions) + gamma * valtmp

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
    for a in range(4):
        value = max(v, Qprev[location[0]][location[1]][a])
    return value

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
    v = -1337
    for r in range(1,9):
        for c in range(1,9):        
            for a in range(4):
                if global Qprev[r][c][a] > v:
                    policy_action = a
                    v = Qprev[r][c][a]
    return policy_action

def main():
    count = 0
    iterations = input()
    # capture input
    while iterations > 0:
        ValueIterate(iterations)
        count = count + iterations
        # print count
        # print vals
        # print prompt
        iterations = input()



    print(Qprev)
    return

if __name__ == '__main__':
    main()