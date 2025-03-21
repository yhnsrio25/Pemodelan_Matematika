# -*- coding: utf-8 -*-
"""SIR Tugas 3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1_gxvJFFqQQQ1i7y2VQwhZJ8Q1MtgP5Xd
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

beta =  0.2
gamma = 1/10
alpha = 0.01
sigma = 0.005
N = 1000

S0 = N -1
I0 = 1
R0 = 0

t = np.linspace(0, 300, 300)

def sir_model(y, t, N, beta, gamma, sigma, alpha):
    S, I, R = y
    dSdt = alpha * N - beta * S * I / N - sigma * S
    dIdt = beta * S * I / N - gamma * I - sigma * I
    dRdt = gamma * I - sigma * R
    return [dSdt, dIdt, dRdt]
y0 = [S0, I0, R0]
solution = odeint(sir_model, y0, t, args=(N, beta, gamma, sigma, alpha))
S, I, R = solution.T

plt.figure(figsize=(10, 6))
plt.plot(t, S, label='Susceptible', color='blue')
plt.plot(t, I, label='Infected', color='red')
plt.plot(t, R, label='Recovered', color='green')
plt.xlabel('Hari')
plt.ylabel('Jumlah Individu')
plt.title('Simulasi Model SIR')
plt.legend()
plt.grid()
plt.show()