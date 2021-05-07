from selection.roulette import roulette
import numpy as np


def roulette_test():
    population = np.random.uniform(-100, 100, 4)
    evals = np.random.uniform(-100, 100, 4)
    el = [2,3,5,1][0]
    print(el)
    try:
        # for i in range(0, 10000):
        roulette(population, evals)
    except Exception as exception:
        print(exception)
