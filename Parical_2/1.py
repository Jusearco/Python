import numpy as np

n = int(input("Matriz (n*n): ")) #Pedimos la longitud de la matriz n*n
matriz = np.random.randint(0, 99, size = (n, n)) #Le añadimos valores aleatorias a la matriz
print(matriz)

dig_1 = np.diag(matriz) #Encontramos la diagonal principal de la matriz
matriz_inv = np.fliplr(matriz) #Encontramos la matriz inversa para la segunda diagonal
dig_2 = np.diag(matriz_inv)
promedio = (sum(dig_1)+sum(dig_2))/(n*2) #Sumamos todos los valores de la diagonal 1 y 2 y lo divimos por la cantidad de elementos dados por 2 para la cantidad de elementos que se usaron

print("El promedio de la matriz principal y secundaria es: ", promedio) #Imprimimos el promedio
