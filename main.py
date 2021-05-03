import numpy as np
from crossover import cross
from mutation import mutate

population = np.array([
    np.random.randint(2, size=10),
    np.random.randint(2, size=10),
    np.random.randint(2, size=10),
    np.random.randint(2, size=10)
])

print(population)
print('')
cross(population, 0.5)
print(mutate(population, 0.5))
