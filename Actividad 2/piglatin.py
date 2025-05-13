entrada = str(input("Ingresa una palabra: "))
n = len(entrada)
vocales = "aeiou"

if entrada[0] in vocales:
    print(entrada+"way")
    i = n
else:
    for i in range(n):
        if entrada[i] in vocales:
            print(entrada[i:] + entrada[:i] + "ay")
            i = n
    print(entrada + "ay")