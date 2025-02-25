# -*- coding: utf-8 -*-
"""SIR.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Q3-QOBGE7H5UenXOAu4VTp2SPmY0T1Tk
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Parameter model
beta = 0.2        # Laju infeksi
gamma  = 1/10     # Laju perubahan (1/gamma = 10 hari )
N = 1000          # tota; populasi

# Kondisi awal
S0 = N-1      # semua individu rentan kecuali 1 yang terinfeksi
I0 = 1        # individu terinfeksi pada awalnya
R0 = 0        # tidak ada yang sembuh pada awalnya

# waktu simulasi (dalam hari)
t = np.linspace(0, 160, 160)    # simulasi selama 160 hari

#Model SIR
def sir_model(y, t, N, beta, gamma):
  S, I, R = y
  dSdt = -beta * S * I / N
  dIdt = beta * S * I / N - gamma * I
  dRdt = gamma * I
  return [dSdt, dIdt, dRdt]

#Menyelesaikan sistem persamaan diferensial
y0 = [S0, I0, R0]
solution = odeint(sir_model, y0, t, args=(N, beta, gamma))
S, I, R = solution.T

# Plot hasil simulasi
plt.figure(figsize=(10, 6))
plt.plot(t, S, label= 'Susceptible' , color='blue' )
plt.plot(t, I, label= 'Infected' , color='red' )
plt.plot(t, R, label= 'Recovered' , color='green' )
plt.xlabel('Hari')
plt.ylabel('Jumlah Individu')
plt.title('Simulasi Model SIR')
plt.legend()
plt.grid()
plt.show()

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import ipywidgets as widgets
from IPython.display import display

#Model SIR
def sir_model(y, t, N, beta, gamma):
  S, I, R = y
  dSdt = -beta * S * I / N
  dIdt = beta * S * I / N - gamma * I
  dRdt = gamma * I
  return [dSdt, dIdt, dRdt]

#Fungsi untuk memprebaharui grafik
def update_SIR(beta, gamma, S0, I0, Tmax):
  N = S0 + I0     #Total populasi
  R0 = 0          #Tidak ada yang sembuah pada awalnya
  t = np.linspace(0, Tmax, Tmax)   #waktu simulasi

  #menyelesaikan sistem persamaan diferensial
  y0 = [S0, I0, R0]
  solution = odeint(sir_model, y0, t, args=(N, beta, gamma))
  S, I, R = solution.T

  #Plot hasil simulasi
  plt.figure(figsize=(10, 6))
  plt.plot(t, S, label= 'Susceptible' , color='blue' )
  plt.plot(t, I, label= 'Infected' , color='red' )
  plt.plot(t, R, label= 'Recovered' , color='green' )
  plt.xlabel('Hari')
  plt.ylabel('Jumlah Individu')
  plt.title('Simulasi Model SIR')
  plt.legend()
  plt.grid()
  plt.show()

#Membuat slider interaktif
widgets.interactive(update_SIR,
                    beta=widgets.FloatSlider(min=0.0001, max=1, step=0.0001, value=0.2, description='beta'),
                    gamma=widgets.FloatSlider(min=0.01, max=1, step=0.01, value=0.1, description='gamma'),
                    S0=widgets.IntSlider(min=1, max=1000, step=1, value=997, description='S0'),
                    I0=widgets.IntSlider(min=1, max=1000, step=1, value=3, description='I0'),
                    Tmax=widgets.IntSlider(min=10, max=200, step=10, value=100, description='Tmax'))