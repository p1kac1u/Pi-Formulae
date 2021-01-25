from math import sqrt
from decimal import Decimal, getcontext

print("How many times do you wanna iterate the entire zeta function?")
iteration = int(input())

print("How many digits do you wanna get?")
deciprecision = int(input())

getcontext().prec = deciprecision + 1

def riemannzeta(n):
    zeta = Decimal(0)
    for i in range(1, iteration + 1):
        zeta += Decimal(1/(i**n))
    return zeta

print(Decimal(sqrt(6*riemannzeta(2))))
