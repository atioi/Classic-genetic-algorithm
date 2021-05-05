from genetics.population import generate_population, evaluate_population, best_individual
from objective_functions.cross_in_tray import cross_in_tray
from selection.crossover import cross
from selection.mutation import mutate
from selection.roulette import roulette

N = 2


def evolve(object_function, population_size, cross_probability, mutation_probability, generations, code_precision):
    """
    This function implements classic genetic algorithm
    :param object_function: Object function that will be used in algorithm
    :param population_size: The number of individuals
    :param cross_probability: The number between 0 and 1
    :param mutation_probability: The number between 0 and 1
    :param generations: Number of generation will be created in during execution
    :param code_precision: For binary coding (look at genetics.individual)
    :return:
    """
    list_best = []
    list_mean = []

    # Started population:
    population = generate_population(population_size, 10)
    evaluated_population = evaluate_population(object_function, population, N, 5, 1, code_precision)

    for i in range(0, generations):
        # Roulette selection:
        population = roulette(population, evaluated_population)
        # New population after crossing
        population = cross(population, cross_probability)
        # New population after muting
        population = mutate(population, mutation_probability)

        evaluated_population = evaluate_population(object_function, population, N, 5, 1, code_precision)
        best = best_individual(population, evaluated_population)

        list_best.append(best['value'])
        list_mean.append(sum(evaluated_population) / len(evaluated_population))


evolve(cross_in_tray, 5, 0.4, 0.6, [], 0.06451612903225806)
