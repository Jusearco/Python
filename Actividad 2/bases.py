n = int(input("Número de base 10: "))
b = int(input("Base a escoger ( base > 0, base < 11): "))

while b > 11:
    b = int(input("Base no valida, por favor ingresar de nuevo ( base > 0, base < 11): "))
    
while b < 1:
    b = int(input("Base no valida, por favor ingresar de nuevo ( base > 0, base < 11): "))

m = 0
factor = 1

while n > 0 :
    r = n % b
    n = n // b
    m = m + r * factor
    factor = factor * 10

print(m)