import numpy as np

# Populacja:
population = np.array([
    np.array([1.2, 0.1, 3.0, 2.1]),
    np.array([1.4, 2.0, 3.2, 4.0]),
    np.array([2.0, 5.5, 6.5, 2.05]),
    np.array([0.0, 2.0, 4.0, 9.0]),
    np.array([2.2345, 23.21, 0.0, 0.2])
])
# Oceny osoboników:
oceny = np.array([-1, 0.5, 2, 10, 0])


def roulette(pop, evaluated_pop):
    # Suma ocen osobników (poddana funkcji abs aby nie mieć ujemnych elementów):
    evals_sum = np.abs(evaluated_pop).sum()
    # Wyliczone przedziały zgodnie ze wzorem:
    evals_range = [abs(eval_individual) / evals_sum for eval_individual in evaluated_pop]

    # Losuję tyle razy liczbę z przedziału [0,1] ile jest osobników populacji:
    random_array = np.random.rand(len(pop))

    # Tworzę pustą listę dla nowej populacji:
    new_pop = []

    for random_val in random_array:
        # Wybieram tylko te przedziały, które są mniejsze od random:
        cos = [i for i in evals_range if i < random_val]

        # Szukam maksimum wśród elementów:
        max_eval = np.amax(cos)

        # Szukam indeksu wybranego elementu:
        max_eval_index = evals_range.index(max_eval)
        individual = pop[max_eval_index]

        # Dodaję go do nowej populacji:
        new_pop.append(individual)

    new_pop = np.array(new_pop)
    return new_pop


print(roulette(population, oceny))
