from wavelets import utilities


def daubechies(order, polyphase=True):
    """
    returns the lowpass and highpass filter coefficients for a Daubechies wavelet
    :param order: the order of the wavelet function
    :param polyphase: whether the output should be return in polyphase form
    :return: the daubieches-<order> coefficients
    """
    if order is 1:
        c = [0.7071067812, 0.7071067812]
        d = [-0.7071067812, 0.7071067812]
    elif order is 2:
        c = [-0.1294095226, 0.2241438680, 0.8365163037, 0.4829629131]
        d = [-0.4829629131, 0.8365163037, -0.2241438680, -0.1294095226]
    elif order is 3:
        c = [0.035226291882100656, -0.08544127388224149, -0.13501102001039084, 0.4598775021193313, 0.8068915093133388, 0.3326705529509569]
        d = [-0.3326705529509569, 0.8068915093133388, -0.4598775021193313, -0.13501102001039084, 0.08544127388224149, 0.035226291882100656]
    else:
        raise ValueError('order is not supported')

    if polyphase:
        return utilities.classic2polyphase(c, d)

    return c, d
