import numpy as np
import random

def cross(population, cross_probability):
    new_pop = []
    pop_len = len(population)
    for index in range(0, pop_len):
        if random.uniform(0, 1) < cross_probability:
            locus = random.randint(0, len(population[index]))
            index2 = -len(population) + index + 1
            offspring = np.concatenate((population[index][0:locus], population[index2][locus::]))
            new_pop.append(offspring)
        else:
            offspring = population[index]
            new_pop.append(offspring)
    return np.array(new_pop)
