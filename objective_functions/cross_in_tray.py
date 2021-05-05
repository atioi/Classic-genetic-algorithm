import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm


def cross_in_tray(XY):
    """
    CROSS-IN-TRAY FUNCTION
    :param X: X domain
    :param Y: Y domain
    :return: Set of values
    """
    X, Y = XY

    return -0.0001 * (np.abs(np.sin(X) * np.sin(Y) * np.exp(100 - np.sqrt(X ** 2 + Y ** 2) / np.pi)) + 1) ** 0.1


def plot(X: np.array, Y: np.array):
    """
    Cross-in-Tray plot drafter
    :param X: X domain
    :param Y: Y domain
    :return: None
    """
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    X, Y = np.meshgrid(X, Y)
    Z = cross_in_tray([X, Y])
    ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, linewidth=0, antialiased=False)
    plt.show()
