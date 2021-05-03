import numpy as np
import random


def mutate(pop, pm):
    new_pop = []
    for individual in pop:
        new_individual = []
        for bit in individual:
            if pm < random.uniform(0, 1):
                if bit == 0:
                    new_individual.append(1)
                else:
                    new_individual.append(0)
            else:
                new_individual.append(bit)
        new_pop.append(new_individual)

    new_pop = np.array(new_pop)
    return new_pop
