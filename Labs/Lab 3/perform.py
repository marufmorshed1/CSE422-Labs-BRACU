import random

x = '25485465'


shuffle = int(x[3])


id = x[-2] + x[-1]

min = int(x[4])
max = int(int(id) * 1.25)


to_win = int(id[::-1])


values = []
for i in range(8):
    values.append(random.randint(min, max))

print(values)