import random

#lista_1 con número randoms:
n = int(input("Longitud de la lista: "))
lista_1 = []
for i in range(n):
    lista_1.append(random.randint(0, 100))
print(lista_1) #Imprimimos la lista aleatoria
max = max(lista_1) #Definimos el maximo
min = min(lista_1) #Definimos el minimo

#Promedio de los elementos pares:
suma_par = 0
cant_par = 0
for i in range(0,n,2):
    suma_par = suma_par + lista_1[i] #Calculamos el promedio de los elementos pares
    cant_par += 1
print("El promedio de las posiciones pares es: ", suma_par / cant_par)

#Suma de los elementos impares:
suma_impar = 0
for i in range(1,n,2):
    suma_impar = suma_impar + lista_1[i] #Sumamos los elementos impares

print("La suma de las posiciones impares es: ", suma_impar)

#Segunda lista:
lista_2 = [] #definimos nuestra segunda lista

for i in range(n):
    if i % 2 == 0: #Si la la posicion i es divisible entre dos, es par, sino es impar
        lista_2.append(lista_1[i]/max) #Realizamos la división con el maximo
    else:
        lista_2.append(lista_1[i]/min) #Realizamos la división con el minimo

print("Lista_2 con las divisiones del maximo y minimo:")    
print(lista_2) #Imprimimos la lista_2 modificada