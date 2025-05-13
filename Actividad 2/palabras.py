entrada = str(input("Palabra: "))
n = len(entrada)

salida = ""

for i in range(n):
    if  entrada[i] != " ":
        salida = salida + entrada[i]
    else:
        print(salida)
        salida = ""

print(salida)