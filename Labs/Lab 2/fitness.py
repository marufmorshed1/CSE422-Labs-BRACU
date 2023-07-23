import random
import re


def Fitness(memory, combination, goal):
    for i in combination:
        sum = 0
        for j in range(len(memory)):
            if i[j] == "1":
                sum = sum + int(memory[j][1])
            else:
                continue
        if sum == goal:
            return i, True
        else:
            continue

    return -1, False


child = ['01101', '10101', '00001', '10000']
memory = [['Tamim', '120'], ['Shoumyo', '90'], ['Shakib', '70'], ['Afif', '65'], ['Mushfiq', '80']]
goal = 240


x = Fitness(memory, child, goal)
print(x[0])