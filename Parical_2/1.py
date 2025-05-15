import numpy as np

n = int(input("Matriz (n*n): "))
matriz = np.random.randint(0, 99, size = (n, n))
print(matriz)

dig_1 = np.diag(matriz)
sum_1 = sum(dig_1)
matriz_inv = np.fliplr(matriz)
dig_2 = np.diag(matriz_inv)
sum_2 = sum(dig_2)
promedio = (sum_1+sum_2)/(n*2)

print(promedio)
