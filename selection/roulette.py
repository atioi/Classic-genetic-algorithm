import numpy as np


def roulette(population: np.array, evaluated_population: np.array):
    const = np.max(np.abs(evaluated_population))
    evaluated_population = evaluated_population + const
    eval_sum = np.sum(evaluated_population)
    eval_range = np.cumsum([eval_individual / eval_sum for eval_individual in evaluated_population])

    random_values = np.random.rand(len(population))

    new_population = np.array([])

    for random_value in random_values:
        indexes, *b = np.where(eval_range < random_value)
        survivor = population[len(indexes)]
        new_population = np.append(new_population, survivor)
