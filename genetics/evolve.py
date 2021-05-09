from genetics.population import generate_population, evaluate_population, best_individual
from selection.crossover import cross
from selection.mutation import mutate
from selection.roulette import roulette
import numpy as np


def evolve(object_function, population_size, cross_probability, mutation_probability, generations, code_precision, N=2):
    """
    This function implements classic genetic algorithm
    :param N: Carefully if you change this param function can required modification too
    :param object_function: Object function that will be used in algorithm
    :param population_size: The number of individuals
    :param cross_probability: The number between 0 and 1
    :param mutation_probability: The number between 0 and 1
    :param generations: Number of generation will be created in during execution
    :param code_precision: For binary coding (look at genetics.individual)
    :return:
    """
    list_best = []
    list_best_generations = []
    list_mean = []

    # Started population:
    population = generate_population(population_size, 10)
    evaluated_population = evaluate_population(object_function, population, N, 5, 1, code_precision)

    # Statistics:
    best_sol = best_individual(population, evaluated_population)
    best_generation = 0
    list_best.append(best_sol['value'])
    list_best_generations.append(best_sol['value'])
    list_mean.append(np.sum(evaluated_population) / len(evaluated_population))

    for i in range(0, generations):

        population = roulette(population, evaluated_population)
        population = cross(population, cross_probability)
        population = mutate(population, mutation_probability)
        evaluated_population = evaluate_population(object_function, population, N, 5, 1, code_precision)

        # Statistics:
        next_best_sol = best_individual(population, evaluated_population)
        list_best_generations.append(next_best_sol['value'])
        list_mean.append(np.sum(evaluated_population) / len(evaluated_population))

        if next_best_sol['value'] > best_sol['value']:
            best_sol = next_best_sol
            best_generation = i

        list_best.append(best_sol['value'])

    return {'The best solution': best_sol, 'The best generation': best_generation,
            'List of the best': np.array(list_best),
            'List of the best in all populations': np.array(list_best_generations),
            'Average eval in generation': np.array(list_mean)}

