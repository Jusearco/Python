n = int(input("Numero para pasar a base 2, 4, 8, 16: "))

n2 = n
n4 = n
n8 = n
n16 = n

m = 0
factor = 1

while n2 > 0 :
    r = n2 % 2
    n2 = n2 // 2
    m = m + r * factor
    factor = factor * 10
    
print(f"El numero {n} en base 2 es: {m}")
m = 0
factor = 1

while n4 > 0 :
    r = n4 % 4
    n4 = n4 // 4
    m = m + r * factor
    factor = factor * 10
    
print(f"El numero {n} en base 4 es: {m}")
m = 0
factor = 1

while n8 > 0 :
    r = n8 % 8
    n8 = n8 // 8
    m = m + r * factor
    factor = factor * 10
    
print(f"El numero {n} en base 8 es: {m}")
m = ""

while n16 > 0 :
    r = n16 % 16
    n16 = n16 // 16
    
    if r == 10 :
        m = "A" + m
    elif r == 11 :
        m = "B" + m
    elif r == 12 :
        m = "C" + m
    elif r == 13 :
        m = "D" + m
    elif r == 14 :
        m = "E" + m
    elif r == 15 :
        m = "F" + m
    else:
        m = str(r) + m
        
if m == "":
    m = "0"
        
print(f"El numero {n} en base 16 es: {m}")