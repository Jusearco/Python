contpos = 0
contneg = 0

n = int(input("Ingresa un número: "))

if n > 0:
    print(f"El número {n} es positivo.")
    j = n
    k = 0
    contpos = 1

elif n < 0:
    print(f"El número {n} es negativo.")
    k = n
    j = 0
    contneg = 1

else:
    print(f"El número {n} es neutro.")
    k = 0
    j = 0
    
n = 1
    
while n != 0:
    n = int(input("Ingresa un número: "))
    
    if n > 0:
        print(f"El número {n} es positivo.")
        j = j + n
        contpos = contpos + 1

    elif n < 0:
        print(f"El número {n} es negativo.")
        k = k - n
        contneg = contneg + 1
    
    else:
        print(f"El numero {n} es neutro")
        
if contpos == 0 and contneg == 0:
    print("NO hay promedio en los número positivos")
    print("NO hay promedio en los número negativos")
    
elif contneg == 0:
    print(f"El promedio de los número positivos es {j/contpos}")
    print("NO hay promedio en los número negativos")

elif contpos == 0:
    print(f"El promedio de los número negativos es {k/contneg}")
    print("NO hay promedio en los número positivos")
    
else:
    print(f"El promedio de los número positivos es {j/contpos}")
    print(f"El promedio de los número negativos es {k/contneg}")
    


    
    
    
    
    
    
    
    
    