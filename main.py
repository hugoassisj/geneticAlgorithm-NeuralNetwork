import numpy as np
from population import Population
from ga import GA
import matplotlib.pyplot as plt
import time

GENERATIONS = 500
MUTATION_RATE = 0.1
CROSSOVER_RATE = 0.7
POPULATION_SIZE = 8
OPENAI_EVALUATIONS = 500


def populate_fitness(population):
    '''Calculate the fitness for all members of the population'''
    for ind in population:
        ind.fitness = genetic_algorithm.calculate_fitness(ind.weights)


def get_best_individue(population):
    '''Get the best individue and its fitness'''
    return population[np.argmax([x.fitness for x in population])]


def run_best(file):
    weights = np.load('best/' + str(file) + '.npy', allow_pickle=True)
    genetic_algorithm.openAI.run_result(weights)


# Create First Population
population = Population(POPULATION_SIZE)
genetic_algorithm = GA(MUTATION_RATE, CROSSOVER_RATE, OPENAI_EVALUATIONS)

# run_best('1575216646.5449824np_294')

populate_fitness(population.get())

best_individue = None
best_individues = []
mean = []
for i in range(1, GENERATIONS):
    best_individue = get_best_individue(population.get())
    best_individues.append(best_individue)
    new_poulation = genetic_algorithm.generation(population.get())
    new_poulation.get()[0] = best_individue
    population = new_poulation
    populate_fitness(population.get())
    print(i,best_individue.fitness)
    if best_individue.fitness == OPENAI_EVALUATIONS:
        np.save('best/' + str(time.time()) + 'np_' + '.npy', best_individue.weights)
        genetic_algorithm.openAI.run_result(best_individue.weights)
        break

# start = time.time()
# genetic_algorithm.openAI.run_result(best_individue.weights)
# end = time.time()
# print(end - start, ' seconds')

# Plot evaluation data
# if best_individue.fitness > 300:
#     #     plt.figure()
#     #     plt.axhline(y=OPENAI_EVALUATIONS, color='r', linestyle='dashed')
#     #     plt.plot([x.fitness for x in best_individues], color='b', linestyle='solid')
#     #     # plt.plot(mean, color='g', linestyle='dotted')
#     #
#     #     plt.ylabel('Fitness Value')
#     #     plt.xlabel('Generation')
#     #     plt.legend(['Maximum', 'Best individue'])
#     #     plt.savefig('imgs/' + str(time.time()) + '_' + str(kkk) + '.png')
# plt.show(block=False)

