import random


def Crossover(parents):
    child = ['', '', '', '']
    x = random.randrange(1, 7)
    child[0] = parents[0][0:x] + parents[1][x:]
    child[1] = parents[1][0:x] + parents[0][x:]
    child[2] = parents[2][0:x] + parents[3][x:]
    child[3] = parents[3][0:x] + parents[2][x:]

    return child