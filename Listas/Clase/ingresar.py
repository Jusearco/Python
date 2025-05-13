A = []
print(A)
n = int(input("Número de elementos: "))
for i in range(1,n+1):
    A.append(float(input(f"Elemento {i}: ")))
    
print(A)

suma = 0
for i in range(len(A)):
    print(A[i])
    suma = suma + A[i]

print(suma)
if len(A) > 0:
    print(f"promedio es {suma/len(A)}")
    
suma = 0
for x in A:
    print(x)
    suma = suma + x