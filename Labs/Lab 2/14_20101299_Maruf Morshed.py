import random
import re
import sys

sys.stdin = open("input2.txt", "r")

file = open("input2.txt", 'r')


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

    return 0, False


def Crossover(parents, range):
    child = ['', '', '', '']
    x = random.randrange(1, range-1)
    child[0] = parents[0][0:x] + parents[2][x:]
    child[2] = parents[2][0:x] + parents[0][x:]
    child[1] = parents[1][0:x] + parents[3][x:]
    child[3] = parents[3][0:x] + parents[1][x:]

    return child


def Mutation(child, number):
    x = random.randrange(0, number)

    for i in range(len(child)):
        name = child[i]
        n = re.findall('[01]', name)
        child[i] = n

    temp = child[0][x]
    child[0][x] = child[1][x]
    child[1][x] = temp

    temp1 = child[2][x]
    child[2][x] = child[3][x]
    child[3][x] = temp1

    for i in range(len(child)):
        string = ''
        for j in child[i]:
            string += j
        child[i] = string

    return child


def Population(n):
    child = ''
    for i in range(n):
        temp = str(random.randint(0, 1))
        child += temp

    return child


def Genetic_Algorithm(memory, goal):
    parents = []
    for i in range(4):
        x = Population(len(memory))
        parents.append(x)
    checker = 1000000
    while checker > 0:
        fit = Fitness(memory, parents, goal)
        if fit[1] is True:
            return fit
        else:
            parents = Crossover(parents, len(memory))
            parents = Mutation(parents, len(parents))
            parents = Mutation(parents, len(parents))
            parents = Crossover(parents, len(memory))
        checker -= 1

    return -1, False


# Driver Code


No, Goal = file.readline().split(" ")
Goal = int(Goal)

info = []

for i in range(int(No)):
    x = file.readline().split(" ")
    if i == int(No):
        continue
    else:
        x[1] = x[1][:-1]
    info.append(x)


name = []
for n in info:
    name.append(n[0])
print(name)
x = Genetic_Algorithm(info, Goal)
print(x[0])
