import os
import wavelets as wav
from scipy import loadtxt, sum

# load ecg signal
data_dir = os.environ.get('DATA_DIR', '../data')
data_file = os.path.join(data_dir, 'ecg.txt')
s = loadtxt(data_file)

# obtain the low-pass and high-pass coefficients in polyphase form
poly = wav.wavelet_function.daubechies(order=1)

# apply an l-level wavelet decomposition
a, b = wav.dwt(s, poly, l=2)

# visualise the decomposition
wav.visualization.plot_wavelet_decomposition(a, b)

# reconstruct the original signal
s_hat = wav.idwt(a, b, poly, l=2)

# print the reconstruction error
print sum((s_hat - s)**2)/len(s_hat)
