import matplotlib.pyplot as plt


def plot_wavelet_decomposition(a, b):

    # determine decomposition level
    l = len(b)

    # init the figure
    f, axis = plt.subplots(l+1, 1, figsize=(10, 10))

    # plot the approximation coefficients
    axis[0].plot(range(a.shape[0]), a, 'r')
    axis[0].set_title("Approximation coefficients at level " + str(l))

    detail_sum = 0
    for level in range(1, l+1):
        axis[level].plot(range(len(b[level-1])), b[level-1])
        axis[level].set_title("Detail coefficients at level " + str(level))

    plt.show()