i = 1

n1 = int(input("Número 1: "))
n2 = int(input("Número 2: "))

if n1 % 2 == 0 and n2 % 2 == 0 or n1 % 2 != 0 and n2 % 2 != 0:
    
    if n1 < n2:
        while i <= n1:
            
            if n1 % i == 0 and n2 % i == 0:
                mcd = i
            i = i + 1
                
    elif n1 > n2:
        while i <= n2:
            
            if n1 % i == 0 and n2 % i == 0:
                mcd = i
            i = i + 1
    
    else:
        mcd = n1
    
    print(f"El máximo común divisor de {n1} y {n2} es {mcd}.")
    
else:
    if n1 > n2:
        for i in range(n1 * n2, n1 - 1, -1):
            
            if i % n1 == 0 and i % n2 == 0:
                mcm = i
    
    elif n1 < n2:
        for i in range(n1 * n2, n2 - 1, -1):
            
            if i % n1 == 0 and i % n2 == 0:
                mcm = i
                
    else:
        mcm = n2
    
    print(f"El minimo común multiplo de {n1} y {n2} es {mcm}.")
