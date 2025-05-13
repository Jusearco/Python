import math
from time import perf_counter_ns

def comb(n, k):
    return (math.factorial(n)) / ((math.factorial(k)) * (math.factorial(n - k)))

n = int(input("n: "))
antes = perf_counter_ns()
for m in range(0, n + 1):
    for i in range(0, m + 1):
        print(int(comb(m, i)), end=",")
    print("")
despues = perf_counter_ns()
print (despues - antes)