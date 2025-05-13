n = int(input("Ingresa un número entero positivo: "))
copia = n
factor = 1
r = 0

while copia != 0:
    m = (copia + 1) % 10
    r = m * factor + r
    factor = factor * 10
    copia = (copia - copia % 10) / 10
    
print(r)