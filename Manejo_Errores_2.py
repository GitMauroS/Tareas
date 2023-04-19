try:
    y = 1 / 0
except ZeroDivisionError:
    print("Zero Division!")
except ArithmeticError:
    print("Arithmetic problem!")

print("THE END.")

def badFun(n):
    raise ZeroDivisionError
try:
    badFun(0)
except ArithmeticError:
    print("What happened? An error?")
    
print("THE END.")

import math
x = float(input("Enter a number: "))
assert x >= 0.0
x = math.sqrt(x)
print(x)
