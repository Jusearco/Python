import random as rnd
#from time import perf_counter_ns

n = 10
L = []
for i in range(n):
    L.append(int(30*rnd.random()))
print(L)

#t1_inicio = perf_counter_ns()

'''
operaciones = 0
intercambios = 0
'''

for i in range(len(L) - 1):
    min = i
    for j in range(i + 1, len(L)):
        if (L[min] > L[j]):
            min = j
    if min != i:
        L[min], L[i] = L[i], L[min]
