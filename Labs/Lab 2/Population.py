import random


def Population(n):
    child = ''
    for i in range(n):
        temp = str(random.randint(0, 1))
        child += temp

    return child


print(Population(8))