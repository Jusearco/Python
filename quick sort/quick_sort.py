import random as rnd
def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivote = lista[0]
        menores = []
        for x in lista[1:]:
            if x <= pivote:
                menores.append(x)
        mayores = []
        for x in lista[1:]:
            if x > pivote:
                mayores.append(x)
        return quick_sort(menores) + [pivote] + quick_sort(mayores)

n = int(input("Cantidad de números en la lista: "))
L = []
F = int(input("Número hasta el que llega: "))
for i in range(n):
    L.append(int(F*rnd.random()))

print(f"Lista sin ordenar: {L}")

ordenada = quick_sort(L)
print(f"Lista ordenada: {ordenada}")