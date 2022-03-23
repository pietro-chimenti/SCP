from scipy import *
from matplotlib.pyplot import *
import numpy as np

print ("Calculando Pi usando o método Monte Carlo")
N = int (input("Escolha o número de pontos: "))
n = 0
i = 1

while i < N:
    rng = np.random.default_rng()
    x_axis = rng.random()
    y_axis = rng.random()
    if x_axis**2 + y_axis**2 < 1:
        n += 1
    # print(4*n/i)
    i += 1
resultado = 4*n/N
print(f"O valor de pi é: {resultado}")
