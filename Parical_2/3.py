def primera_mayus(entrada): #Definimos la función.
    
    n = len(entrada) #Vemos la cantidad de caracteres que tiene la entrada
    salida = "" + entrada[0].upper() #Cambiamos la primera letra a mayuscula
    i = 1
    while i < n:
        if entrada[i] == " " and i + 1 < n and entrada[i+1] != " ": #Si el caracter es el epacio y que este no sea mayor a la cantidad de caracteres de la entrada y ademas el siguiente no sea otro espacio
            salida = salida + entrada[i] #Entonces se le añade a la salida el espacio, se le suma uno a la i
            i += 1
            salida = salida + entrada[i].upper() #Luego se le añade la primera letra de la palabra en mayuscula 
        else: #sino hay espacio, se agrega la letra normal
            salida = salida + entrada[i]
        i += 1
        
    return salida

entrada = input("Escriba una frase: ") #Frase inicial
x = primera_mayus(entrada) 

print(x) #Se imprime la frase con las iniciales de cada palabra en mayuscula
