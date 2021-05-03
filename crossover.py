import numpy as np
import random


def cross(pop, pk):
    new_pop = []
    pop_len = len(pop)
    print(pop)
    for index in range(0, pop_len):
        # Krzyżuję osobniki
        if random.uniform(0, 1) < pk:
            print('Doszło do skrzyżowania: ')
            # Losuję miejsce krzyżowania:
            locus = random.randint(0, len(pop[index]))
            # Index kolejnego wiersza (rodzica do mutacji):
            index2 = -len(pop) + index + 1
            # Potomek po skrzyżowaniu:
            offspring = np.concatenate((pop[index][0:locus], pop[index2][locus::]))
            # Wrzucam potomka do nowej populacji:
            new_pop.append(offspring)

            # Wyświetlam obliczenia cząstkowe:
            print('Indeks rodz. 1: ', index)
            print('Indeks rodz. 2: ', index2 + len(pop))
            print('Miejsce skrzyżowania: ', locus)
            print('Potomek: ', offspring)

        else:
            print('Nie doszło do skrzyżowania: ')
            offspring = pop[index]
            print('Potomek : ', offspring)
            new_pop.append(offspring)
    return new_pop
