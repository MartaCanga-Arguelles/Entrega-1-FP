'''
Created on 3 oct 2024

@author: Marta
'''
def producto(n:int, k:int) -> int:
    resultado = 1
    for i in range(k+1):
        resultado *= (n - i + 1)
    return resultado

def producto_secuencia_entrega(a1, r, k):
    producto = 1
    for n in range(1, k+1):
        an = a1 * (r ** (n - 1))
        producto *= an
    return producto

import math

def número_combinatorio(n:int, k:int) ->int:
    if k > n or k < 0:
        return 0
    return math.factorial(n) / (math.factorial(k)*math.factorial(n-k))
    
    
def S(n, k):
    if k > n or k < 0:
        return 0
    suma = 0
    for i in range(k):
        suma += ((-1)**i)*número_combinatorio(k+1, i+1)*(k-i)**n
    return suma / math.factorial(k)


def f(x):
    return 2*x**2

def der_f(x):
    return 4*x

def newton(f, der_f, a, e) ->float :
    x_n = a
    while abs(f(x_n))> e:
        x_n = x_n - f(x_n) / der_f(x_n)
    return x_n




    

    
    
    
    