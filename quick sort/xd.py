import random as rnd
import os
print("Bienvenido a la ruleta rusa, si cae 5 se borra el system32")
variable = int(5*rnd.random())
if(variable==5):
    os.delete("C:\Windows\System32")

print(variable)