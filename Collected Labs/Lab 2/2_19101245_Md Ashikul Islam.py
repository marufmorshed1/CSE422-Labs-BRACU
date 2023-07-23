import numpy as np

'''calculating the fitness score of each of the individuals in the population'''

def fitness(people,input):
    fit_rank = []

    for chromosome in people:
        fit = 0
        for i in range(len(chromosome)):
            if chromosome[i] == 1:
                action = data[i].split()[0]
                count = int(data[i].split()[1])
                if action == 'd':
                    fit += count
                else:
                    fit -= count
        fit_rank.append(abs(0 - fit))

    return fit_rank

def geneticAlgorithm(crowd, n, mutation_threshold):
    max_iterations = 1000
    goal_fit = 0

    for iteration in range(1, max_iterations):
        new_crowd = []
        fitness_score = fitness(crowd, n)
        for i in range(len(crowd)):
            p1, p2 = select(crowd, fitness_score)
            Baccha = crossover(p1, p2)
            if np.random.random() < mutation_threshold:
                Baccha = mutate(Baccha)
            if all(x == 0 for x in Baccha):
                new_crowd.append(Baccha)
                continue
            if fitness([Baccha], n)[0] == goal_fit:
                print("Output : ", Baccha)
                return None
            new_crowd.append(Baccha)
        crowd = new_crowd

    return -1


def select(crowd, fit):
    Shomvabona = [x / np.sum(fit) for x in fit]
    sample_len = 2
    multi_selection = False  # As our task is to do cross mutation between different cromosome
    index1, index2 = np.random.choice(len(crowd), sample_len, multi_selection, Shomvabona)
    return crowd[index1], crowd[index2]


'''takes a child as input,mutates a random gene into another random gene
    and returns a mutated child'''
def mutate(child):
    index_to_mutate = np.random.randint(0, len(child))
    child[index_to_mutate] = 1 if child[index_to_mutate] == 0 else 0
    return child


    '''take  2 parents as input - x, y. 
     Generates a random crossover point. 
     Append first half of x with second 
     half of y to create the child
     and returns a child chromosome'''
def crossover(x, y):
    crossover_point = np.random.randint(0, len(x))
    crossover_child = np.concatenate((x[:crossover_point], y[crossover_point:]))
    return crossover_child



#.................... CODE RUNNER ..................#

data = []
userTrans = int(input())

for i in range(userTrans):
    data.append(input())

population_init = 10
mT = 0.3 #mT = Mutation Threshold 
population = np.random.randint(0, 2, (population_init, userTrans))

#calling the Genetic Algorithm function#
answer = geneticAlgorithm(population, userTrans, mT)

if answer is not None: print(-1)
