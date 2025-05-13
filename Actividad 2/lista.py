n = int(input("Ingresa un número: "))

i = 1

while i <= n:
    n2 = i % 2
    n3 = i % 3
    n5 = i % 5
    if n2 ==0 :
        print(i)
    elif n3 == 0:
        print(i)
    elif n5 == 0:
        print(i)
    i = i + 1