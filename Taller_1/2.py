n = 0
divisores = 3
i = 1

while n < 2:
    n = int(input("Número entero mayor que 2: "))
    j = n
    
    if n >= 2:
        
        while divisores > 2:
            divisores = 0
            
            while i <= j:
                
                if j % i == 0:
                    divisores = divisores + 1
                i = i + 1
            i = 1
            
            if divisores > 2:
                j = j - 1

    else:
        print(f"El número {n} no es mayor a 2")

print(f"El número primo más cercano a {n} es {j}") 