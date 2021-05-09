import numpy as np
from genetics.evolve import evolve
from objective_functions.cross_in_tray import cross_in_tray
import matplotlib.pyplot as plt

pop_size = 60
pk = 0.7
pm = 0.01
generations = 200
dx = 1e-10

result = evolve(cross_in_tray, pop_size, pk, pm, generations, dx)

# Statystki:

list_mean = result['Average eval in generation']
list_best_generations = result['List of the best in all populations']
list_best = result['List of the best']

fig, axs = plt.subplots(3)

fig.set_figheight(10)
fig.set_figwidth(10)

x = np.arange(0, generations + 1)
axs[0].plot(x, list_mean, 'o')
axs[0].set_title('Average eval in generation')

axs[1].set_title('List of the best in all populations')
axs[1].plot(x, list_best_generations, 'o')

axs[2].set_title('List of the best')
axs[2].plot(x, list_best, 'o')

plt.show()
