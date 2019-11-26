import numpy as np
from population import Population
from ga import GA
import matplotlib.pyplot as plt
import time

GENERATIONS = 2000
MUTATION_RATE = 0.01
CROSSOVER_RATE = 0.5
POPULATION_SIZE = 6
OPENAI_EVALUATIONS = 1000

# Create First Population
population = Population(POPULATION_SIZE)
genetic_algorithm = GA(MUTATION_RATE, CROSSOVER_RATE, OPENAI_EVALUATIONS)


def populate_fitness(population):
    '''Calculate the fitness for all members of the population'''
    for ind in population:
        ind.fitness = genetic_algorithm.calculate_fitness(ind.weights)


def get_best_individue(population):
    '''Get the best individue and its fitness'''
    return population[np.argmax([x.fitness for x in population])]


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
    mean.append(sum([x.fitness for x in population.get()]) / POPULATION_SIZE)
    populate_fitness(population.get())
    print(i, best_individue.fitness)
    if best_individue.fitness == OPENAI_EVALUATIONS:
        break

start = time.time()
genetic_algorithm.openAI.run_result(best_individue.weights)
end = time.time()
print(end - start, ' seconds')

# Plot evaluation data
plt.figure()
plt.axhline(y=OPENAI_EVALUATIONS, color='r', linestyle='dashed')
plt.plot([x.fitness for x in best_individues], color='b', linestyle='solid')
plt.plot(mean, color='g', linestyle='dotted')

plt.ylabel('Fitness Value')
plt.xlabel('Generation')
plt.legend(['Maximum', 'Best', 'Mean'])
plt.show(block=True)

# mean.append(sum([pair[0] for pair in population.get()]) / POPULATION_SIZE)
