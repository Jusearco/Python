print("CALCULADORA")
print("1.Ingresar números")
print("2.Salir")

inicio = str(input("Escoga una opcción(en números): "))

if inicio != "1":
    print("Hasta la proxima :D")
    
else:
    i = 1
    rta = 0
    
    n1 = float(input(f"Número {i}: "))
    sig = str(input("+, -, *, /: "))
    i = i + 1
    n2 = float(input(f"Número {i}: "))
            
    if sig == "+":
        rta = n1 + n2
    elif sig == "-":
         rta = n1 - n2
    elif sig == "*":
        rta = n1 * n2
    else:
        rta = n1 / n2
    i = i + 1
    print("el resultado es,",rta)
    
    print("1.Salir")
    inicio = str(input("+, -, *, /: "))
    
    while i != 0:
        if inicio == "1" :
            print("Hasta la proxima :D")
            i = 0
        
        else:
            n3 = float(input(f"Número {i}: "))
            if sig == "+":
                rta = rta + n3
            elif sig == "-":
                rta = rta - n3
            elif sig == "*":
                rta = rta * n3
            else:
                rta = rta / n3
            print("el resultado es,",rta)
            i = i + 1

            print("1.Salir")
            inicio = str(input("+, -, *, /: "))

        
        
            
        
    