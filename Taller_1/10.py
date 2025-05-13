n = int(input("Ingrese un número: "))
penultimo = 0
ultimo = 1
i = 2

while ultimo < n:
    suma = penultimo + ultimo
    penultimo = ultimo
    ultimo = suma
    i = i + 1
    
if ultimo == n:
    suma = penultimo + ultimo
    penultimo = ultimo
    ultimo = suma
    i = i + 1    
    print(ultimo)

else:
    print(ultimo)