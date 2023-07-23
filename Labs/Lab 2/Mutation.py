import random
import re


def Mutation(child):
    x = random.randrange(1, 7)
    print(x)

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


child = ['01000100', '01111000', '00001011', '10000101']
print(Mutation(child))
