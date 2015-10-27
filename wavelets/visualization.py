import matplotlib.pyplot as plt
from scipy import zeros


def plot_wavelet_decomposition(a, b):
    """
    plot the approximation and detail coefficients at every level
    :param a: approximation coefficients
    :param b: list of detail coefficients
    :return: None
    """
    l = len(b)

    f, axis = plt.subplots(l+1, 1, figsize=(10, 10))

    axis[0].plot(range(a.shape[0]), a, 'r')
    axis[0].set_title("Approximation coefficients at level " + str(l))

    for level in reversed(range(1, l+1)):
        axis[l - level + 1].plot(range(len(b[level-1])), b[level-1])
        axis[l - level + 1].set_title("Detail coefficients at level " + str(level))

    plt.show()


def plot_wavelet_decomposition_map(s, b):
    """
    plot the approximation and detail coefficients at every level in a heatmap
    :param s: original signal
    :param b: list of detail coefficients
    :return: None
    """
    f, axis = plt.subplots(2, 1, sharex=True)

    l = len(b)
    heat_map = zeros((l, 2*len(b[0])))
    ylabels = list()

    for level in list(reversed(range(len(b)))):
        for i in range(0, heat_map.shape[1], 2**(level+1)):
            heat_map[heat_map.shape[0]-level-1, i:i + 2**(level+1)] = b[level][i / 2**(level+1)]

        ylabels.append('b {}'.format(level + 1))

    axis[0].plot(s)
    axis[0].set_title('original signal')

    axis[1].set_yticks(range(heat_map.shape[0]))
    axis[1].set_yticklabels(ylabels)
    axis[1].set_title("Heatmap of the wavelet decomposition " + str(l))
    axis[1].imshow(-heat_map, cmap='hot', interpolation='nearest', aspect='auto')

    plt.show()