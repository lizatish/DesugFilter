from math import cos, sin

import numpy as np
from matplotlib import pyplot as plt

fileObject = open("coeffs.txt", "r")
coeffs = [float(elem) for elem in fileObject.read().split('\n')]

# Низкочастотный сигнал
Fs = 1000
fc1 = 10
sample = 600
x = np.arange(sample)
y1 = np.sin(2 * np.pi * fc1 * x / Fs)

# Высокочастотный сигнал
fc2 = 200
y2 = np.sin(2 * np.pi * fc2 * x / Fs)

y3 = y1 + y2

Xk = []
for n in range(len(y3)):
    sum = 0
    for k in range(len(coeffs)):
        x_val = y3[n]
        sum += complex(cos(-k * n / len(coeffs)), sin(-k * n / len(coeffs))) * x_val
    Xk.append(sum)

xn = []
for n in range(len(Xk)):

    sum = 0
    for k in range(2 * len(coeffs)):

        x_val = Xk[n]
        sum += complex(cos(k * n / len(coeffs)), sin(k * n / len(coeffs))) * x_val
    xn.append(1 / len(coeffs) * sum)

Xkstar = []
for k in range(0, len(coeffs), 2):
    sum = 0
    for n in range(0, len(xn)):
        x_val = xn[n]
        sum += complex(cos(-k * n / (2 * len(coeffs))), sin(-k * n / (2 * len(coeffs)))) * x_val
    Xkstar.append(sum)

Hkstar = []
for k in range(0, len(coeffs), 2):
    sum = 0
    for n in range(0, 2 * len(coeffs)):
        if n >= len(coeffs):
            x_val = 0
        else:
            x_val = coeffs[n]
        sum += complex(cos(-k * n / (2 * len(coeffs))), sin(-k * n / (2 * len(coeffs)))) * x_val
    Hkstar.append(sum)

Ykstar = []
for x_, h_ in zip(Xkstar, Hkstar):
    Ykstar.append(x_ * h_)

ystar = []
for n in range(len(x)):
    sum = 0
    for k in range(0, len(Ykstar)):
        x_val = Ykstar[k]
        sum += complex(cos(k * n / (2 * len(coeffs))), sin(k * n / (2 * len(coeffs)))) * x_val
    ystar.append((1 / (2 * len(coeffs))) * sum)
print(ystar)

fig, axs = plt.subplots(1)

fig.suptitle('Лаба2')
axs.plot(x, ystar)
axs.set_title('Свертка Фурье')

fig.tight_layout()
plt.show()
