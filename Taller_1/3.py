n = 0
i = 1

while n < 1:
    n = int(input("Número entero positivo: "))
    
    while i <= n:
        
        if i*i == n:
            print(f"El número {n} tiene raíz cuadrada exacta y es {i}.")
            i = n + 2
            
        else:    
            i = i + 1

if i - 1 == n:
    print(f"El número {n} no tiene raíz cuadrada exacta.")
    
