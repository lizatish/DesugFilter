import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

fs = 105e6
fin = 70.1e6

N = np.arange(0, 21e3, 1)

# Create a input sin signal of 70.1 MHz sampled at 105 MHz
x_in = np.sin(2 * np.pi * (fin / fs) * N)

# Define the "b" and "a" polynomials to create a CIC filter (R=8,M=2,N=6)
b = np.zeros(97)
b[[0, 16, 32, 48, 64, 80, 96]] = [1, -6, 15, -20, 15, -6, 1]
a = np.zeros(7)
a[[0, 1, 2, 3, 4, 5, 6]] = [1, -6, 15, -20, 15, -6, 1]

w, h = signal.freqz(b, a)
plt.plot(w / max(w), 20 * np.log10(abs(h) / np.nanmax(h)))
plt.title('CIC Filter Response')

output_nco_cic = signal.lfilter(b, a, x_in)

plt.figure()
plt.plot(x_in)
plt.title('Input Signal')
plt.figure()
plt.plot(output_nco_cic)
plt.title('Filtered Signal')
