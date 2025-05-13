import numpy as np
import random as rnd
import matplotlib.pyplot as plt
from time import perf_counter_ns

def bubble_sort(L):

    operaciones = 0
    n = len(L)
    for i in range(n - 1):
        operaciones += 1
        for j in range(n - i - 1):
            operaciones += 1
            if L[j] > L[j + 1]:
                operaciones += 1
                L[j], L[j + 1] = L[j + 1], L[j]
                operaciones += 1
                
    return L, operaciones  

def selection_sort(L):
    
    operaciones = 0

    for i in range(len(L) - 1):
        operaciones += 1
        min = i
        for j in range(i + 1, len(L)):
            operaciones += 1
            if (L[min] > L[j]):
                operaciones += 1
                min = j
        if min != i:
            L[min], L[i] = L[i], L[min]
            operaciones += 1
    
    return L, operaciones

def insertion_sort(L):
    operaciones = 0

    i = 1
    while i < len(L):
        operaciones += 1

        j = i
        while j > 0 and L[j - 1] > L[j]:
            operaciones += 1

            L[j], L[j - 1] = L[j - 1], L[j]
            operaciones += 1
            j -= 1
        i += 1

    return L, operaciones


num_elements = np.arange(10, 1001, 10)
print(num_elements)
size = num_elements.size
print(size)
#print(num_elements)
t_bubble = np.zeros(size)
ops_bubble = np.zeros(size)
t_selection = np.zeros(size)
ops_selection = np.zeros(size)
t_insertion = np.zeros(size)
ops_insertion = np.zeros(size)
t_quick_sort = np.zeros(size)

for i, n in enumerate(num_elements) :
    vector = np.random.randint(0, 100, n, dtype=np.int16)

    #bubble
    vector_ord = vector.copy()
    t_inicio = perf_counter_ns()
    B, ops = bubble_sort(vector_ord)
    t_final = perf_counter_ns()
    ops_bubble[i] = ops 
    t_bubble[i] = t_final - t_inicio
    print(f"vector ordenado: \n{B}")

    #selection
    vector_ord = vector.copy()
    t_inicio = perf_counter_ns()
    B, ops = selection_sort(vector_ord)
    t_final = perf_counter_ns()
    ops_selection[i] = ops
    t_selection[i] = t_final - t_inicio
    print(B)

    #insertion
    vector_ord = vector.copy()
    print(f"vector ordenado: \n{vector_ord}")
    t_inicio = perf_counter_ns()
    B, ops = insertion_sort(vector_ord)
    t_final = perf_counter_ns()
    ops_insertion[i] = ops
    t_insertion[i] = t_final - t_inicio
    print(B)

menu = """"
OPCIONES

1. Cantidad de veces de ordenamiento.
2. Tiempo de ordenamiento.
"""
print(menu)
opc = int(input("Escoge una opción: "))

if opc == 1:
    plt.plot(num_elements, ops_bubble, "g*", num_elements, ops_selection, "b*", num_elements, ops_insertion, "r*")
    plt.show()
    
elif opc == 2:
    plt.plot(num_elements, t_bubble, "g-", num_elements, t_selection, "b-", num_elements, t_insertion, "r-")
    plt.show()