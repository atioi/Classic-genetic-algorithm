import numpy as np
from genetics.individual import decode_individual


def generate_population(individuals_number: int, length: int):
    """
    Function that generate population:
    :param individuals_number:
    :param length: int
    :return: np.array
    """
    return np.random.randint(2, size=(individuals_number, length))


def evaluate_population(objective_function, population, N, B, a, dx):
    return np.array([objective_function(decode_individual(individual, N, B, a, dx)) for individual in population])


def best_individual(population, evaluated_population):
    index = np.argmax(evaluated_population)
    return {'individual': population[index], 'value': evaluated_population[index]}
