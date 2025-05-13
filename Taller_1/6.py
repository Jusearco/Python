n = int(input("Número entero: "))

for i in range(1,n + 1):
    if i % 2 == 0 and i % 3 == 0 and i % 5 == 0:
        print(f"El número {i} es divisible por 2, 3 y 5.")
        
    elif i % 2 == 0 and i % 3 == 0:
        print(f"El número {i} es divisible por 2 y 3.")
        
    elif i % 2 == 0 and i % 5 == 0:
        print(f"El número {i} es divisible por 2 y 5.")
        
    elif i % 3 == 0 and i % 5 == 0:
        print(f"El número {i} es divisible por 3 y 5.")
        
    elif i % 2 == 0:
        print(f"El número {i} es divisible por 2.")
        
    elif i % 3 == 0:
        print(f"El número {i} es divisible por 3.")
        
    elif i % 5 == 0:
        print(f"El número {i} es divisible por 5.")
        
    else:
        print(f"El número {i} NO es divisible por 2, 3 o 5.")