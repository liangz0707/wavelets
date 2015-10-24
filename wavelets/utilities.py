from scipy import array, newaxis, concatenate


def classic2polyphase(c, d):
    poly = concatenate((array(c)[newaxis, :], array(d)[newaxis, :]), axis=0)

    return poly