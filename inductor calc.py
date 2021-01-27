import numpy as np
import matplotlib.pyplot as plt
from sympy import Symbol, solve

# B = mu * N * I / (2 * pi * r)
# L = mu * N**2 * A / (2 * pi * r)
# L = 0.42 muH = 420 mH

pi = np.pi
mu = 4 * pi * (10 ** -7)
L  = 420e-3

N = Symbol('N')
A = Symbol('A')
r = Symbol('r')

def equation(*args) :
    return (mu * (N**2) * A / (2 * pi * r)) - L
def get_result(equation) :
    return np.abs(solve(equation)[0])

print("Choose the case for the known values :\n")
print("1 : N, A")
print("2 : N, r")
print("3 : A, r\n")

case = int(input("case : "))

if case == 1 :
    print("type N and A\n")
    N = float(input("N : "))
    A = float(input("A : "))
    
    eq = equation(N, A)
    r = get_result(eq)
    print(f"r is {r}")

elif case == 2:
    print("type N and r\n")
    N = float(input("N : "))
    r = float(input("r : "))
    
    eq = equation(N, r)
    A = get_result(eq)
    print(f"A is {A}") 

elif case == 3:
    print("type A and r\n")
    A = float(input("A : "))
    r = float(input("r : "))  
    
    eq = equation(A, r)
    N = get_result(eq)
    print(f"N is {N}")

  