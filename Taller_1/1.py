
n = int(input("¿Cúantos números enteros vas a ingresar? "))

i = 0
j = 0
k = 0
m = 1

while i < n:
    N = int(input(f"Número {m}: "))
    m = m + 1
    
    if N % 2 == 0:
        k = N + k
        j = j + 1
    i = i + 1
    
r = k/j
print("El promedio de los número pares es:", r)