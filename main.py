import matplotlib.pyplot as plt
import numpy as np

fileObject = open("coeffs.txt", "r")
coeffs = [float(elem) for elem in fileObject.read().split('\n')]

# Низкочастотный сигнал
Fs = 1000
fc1 = 10
sample = 1000
x = np.arange(sample)
y1 = np.sin(2 * np.pi * fc1 * x / Fs)

# Высокочастотный сигнал
fc2 = 190
y2 = np.sin(2 * np.pi * fc2 * x / Fs)

y3 = y1 + y2

fig, axs = plt.subplots(4)
fig.suptitle('Лаба2')
axs[0].plot(x, y1)
axs[0].set_title('Низкочастотный сигнал')
axs[1].plot(x, y2)
axs[1].set_title('Высокочастотный сигнал')
axs[2].plot(x, y3)
axs[2].set_title('Суммарный сигнал')

y4 = []
for n in range(len(x)):
    sum = 0
    for k, coeff in enumerate(coeffs):
        if n - k <= 0:
            x_val = 0
        else:
            x_val = y3[n - k]
        sum += coeff * x_val
    y4.append(sum)

axs[3].plot(x, y4)
axs[3].set_title('Выход фильтра')

fig.tight_layout()
plt.show()
