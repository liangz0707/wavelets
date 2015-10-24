from scipy import concatenate, dot, zeros_like, array, newaxis


def dwt(s, poly, l=1):

    detail = []
    approximation = array(s)
    for level in range(l):

        # downsample the signal by two
        s = approximation.reshape(approximation.shape[0]/2, 2).transpose()

        # decompose the signal by one level
        decomposition = zeros_like(s, dtype=float)
        for z in range(poly.shape[1]/2):
            decomposition += dot(poly[:, 2*z:2*z+2], concatenate((s[:, z:], s[:, :z]), axis=1))

        # store the detail coefficients obtained by the decomposition
        approximation = decomposition[0, :]
        detail.append(decomposition[1, :])

    return approximation, detail


def idwt(a, d, poly, l=1):

    if len(a.shape) == 1:
        a = a[newaxis, :]

    for level in reversed(range(l)):

        # extract the detail part for this iteration
        decomposition = concatenate((a, d[level][newaxis, :]), axis=0)

        reconstruction = zeros_like(decomposition, dtype=float)
        for z in range(poly.shape[1]/2):
            reconstruction += dot(poly[:, 2*z:2*z+2].transpose(), concatenate((decomposition[:, decomposition.shape[1]-z:], decomposition[:,:decomposition.shape[1]-z]), axis=1))

        # upsample the approximation by two
        a = reconstruction.transpose().reshape(1, 2*a.shape[1])

    return a


def dwt_2d(image, poly, l=1):

    for level in range(l):

        # select the relevant part in the image
        sub_image = image[:(image.shape[0]/(2**level)), :(image.shape[1]/(2**level))]

        # row wise
        for row in range(sub_image.shape[0]):

            # extract row for processing
            s = sub_image[row, :]

            # decompose the row
            a, d = dwt(s, poly)

            # place row back in matrix
            sub_image[row, :] = concatenate((a[newaxis, :], d[0][newaxis, :]), axis=1)

        # column wise
        for col in range(sub_image.shape[1]):

            # extract row for processing
            s = sub_image[:, col]

            # decompose the row
            a, d = dwt(s, poly)

            # place row back in matrix
            sub_image[:, col] = concatenate((a, d[0]), axis=0)

    return image


def idwt_2d(image, poly, l=1):

    for level in reversed(range(l)):

        # select the relevant part in the image
        sub_image = image[:(image.shape[0]/(2**level)), :(image.shape[1]/(2**level))]

        # col wise
        for col in range(sub_image.shape[1]):

            # extract rows for processing
            a = sub_image[:sub_image.shape[0]/2, col]
            d = sub_image[sub_image.shape[0]/2:, col]

            # place in reconstructed matrix
            sub_image[:, col] = idwt(a, [d], poly)

        # row wise
        for row in range(sub_image.shape[0]):

            # extract rows for processing
            a = sub_image[row, :sub_image.shape[1]/2]
            d = sub_image[row, sub_image.shape[1]/2:]

            # place in reconstructed matrix
            sub_image[row, :] = idwt(a, [d], poly)


    return image