import matplotlib.pyplot as plt
import numpy as np

fileObject = open("coeffs.txt", "r")
coeffs = [float(elem) for elem in fileObject.read().split('\n')]

# Низкочастотный сигнал
Fs = 1000
fc1 = 60
sample = 200
x = np.arange(sample)
y1 = np.sin(2 * np.pi * fc1 * x / Fs)

# Высокочастотный сигнал
fc2 = 200
y2 = np.sin(2 * np.pi * fc2 * x / Fs)

y3 = y1 + y2

fig, axs = plt.subplots(3, 2)
fig.delaxes(axs[2, 1])

fig.suptitle('Лабораторная работа №2')
axs[0][0].plot(x, y1)
axs[0][0].set_title('Низкочастотный сигнал')
axs[1][0].plot(x, y2)
axs[1][0].set_title('Высокочастотный сигнал')
axs[2][0].plot(x, y3)
axs[2][0].set_title('Суммарный сигнал')

x_h = [i for i in range(len(coeffs))]
axs[0][1].plot(x_h, coeffs)
axs[0][1].set_title('Импульсная характеристика ФНЧ')

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

axs[1][1].plot(x, y4)
axs[1][1].set_title('Выходной сигнал')

fig.tight_layout()
plt.show()
