import numpy as np

def decode_individual(individual: list, N: int, B: int, a: float, dx: float):
    """
    :param individual: List that represent sequence of numbers in binary
    :param N: The amount of decimal numbers that individual encode
    :param B: The amount of bits that one numbers should have
    :param a: The range beginning
    :param dx: Step, code precision
    :return:
    """
    binaries = np.split(np.array(individual), N)
    return np.array([a + np.sum([b[i] * 2 ** (B - i - 1) for i in range(B)]) * dx for b in binaries])

