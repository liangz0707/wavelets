import matplotlib.pyplot as plt
import wavelets as wav
from scipy import misc, sum, zeros_like

# obtain a grey-scale image of Lena
image = misc.lena().astype(dtype=float)

# specific decomposition depth
l = 2

# obtain the low-pass and high-pass coefficients in polyphase form
poly = wav.wavelet_function.daubechies(order=3)

# apply an l-level wavelet decomposition
decomposition = wav.dwt_2d(image, poly, l)

# erase the detail
compression = zeros_like(decomposition)
compression[:(compression.shape[0]/(2**l)), :(compression.shape[1]/(2**l))] = decomposition[:(compression.shape[0]/(2**l)), :(compression.shape[1]/(2**l))].copy()

# reconstruct the image without detail
image_hat = wav.idwt_2d(compression, poly, l)

# plotting
fig, ax = plt.subplots(2, 2, figsize=(10, 10))
fig.suptitle('mean squared reconstruction difference = {}'.format(sum(sum((image_hat - image)**2))/(image.shape[0] * image.shape[1])))

ax[0, 0].imshow(image, cmap=plt.cm.gray)
ax[0, 0].set_title('original image')

ax[0, 1].imshow(decomposition, cmap=plt.cm.gray)
ax[0, 1].set_title('result after {}-level wavelet decomposition'.format(l))

ax[1, 0].imshow(decomposition[:(compression.shape[0]/(2**l)), :(compression.shape[1]/(2**l))], cmap=plt.cm.gray)
ax[1, 0].set_title('compressed image (approximation coeff)'.format(l))

ax[1, 1].imshow(image_hat, cmap=plt.cm.gray)
ax[1, 1].set_title('image reconstructed from compression'.format(l))

plt.show()


