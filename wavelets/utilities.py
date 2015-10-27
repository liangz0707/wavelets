from scipy import array, newaxis, concatenate


def classic2polyphase(c, d):
    """
    Transforms the coefficients of the low- and high-pass filter to a polyphase form
    :param c: low-pass coefficients
    :param d: high-pass coefficients
    :return: polyphase format containing c and d
    """
    poly = concatenate((array(c)[newaxis, :], array(d)[newaxis, :]), axis=0)

    return poly