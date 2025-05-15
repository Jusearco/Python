import random 
n = int(input("Cantidad de elementos de la lista_1: ")) #Cantidad de elementos en la primera lista.

lista_1 = []
for i in range(n):
    lista_1.append(random.randint(0, 100)) #Se agregan numeros aleatorios de 0 hasta 100 a la lista_1.

print("Lista_1: ")
print(lista_1) #Imprimimos la lista 1

lista_2 = lista_1[::3] #Se crea la lista_2 con los valores de 3 en 3 de la lista_1

print("Lista_2 con posiciones de 3 en 3 de lista_1: ") 
print(lista_2) #Se imprime la lista_2