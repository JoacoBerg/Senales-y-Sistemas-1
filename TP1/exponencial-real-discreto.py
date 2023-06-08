import numpy as np
import matplotlib.pyplot as plt

# --- INGRESO ---

n0 = -1 # tiempo inicial
m = 7 # cantidad de muestras

# --- PROCEDIMIENTO ---

# vector n discreto [n0,n0+m]
n = np.arange(n0,n0 + m,1)

# señal
senal = np.exp(n) # e^(n)

# Imprimo
np.set_printoptions(precision=4)
print('n: ')
print(n)
print('señal x[n]: ')
print(senal)

# Gráficas
plt.stem(n, senal)
plt.xlabel('n')
plt.ylabel('señal x[n]')
plt.show()