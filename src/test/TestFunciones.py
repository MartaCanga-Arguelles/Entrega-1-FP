'''
Created on 3 oct 2024

@author: Marta
'''
from funciones.funciones import producto
from funciones.funciones import producto_secuencia_entrega 
from funciones.funciones import número_combinatorio
from funciones.funciones import S
from funciones.funciones import newton 
from funciones.funciones import f
from funciones.funciones import der_f
  
n = 4
k = 2

print(f"El producto de {n} y {k} es: {producto(n, k)}")

a1 = 3
r = 5
k = 2

print(f"El producto de la secuencia geométrica con a1 = {a1}, r = {r} y k = {k} es: {producto_secuencia_entrega(a1, r, k)}")

n = 4
k = 2

print(f"El número combinatorio de {n} y {k} es: {número_combinatorio(n, k)}")

n = 4
k = 2

print(f"El número S(n,k) siendo n = {n} y k = {k} es: {S(n, k)}")

a = 3
e = 0.001
print(f"Resultado de la función 5 con a = {a} y e = {e}: {newton(f, der_f, a, e)}")
    
