'''
Created on 10 nov 2024

@author: carme
'''
from entrega2.tipos.Lista_ordenada_sin_repeticion import Lista_ordenada_sin_repeticion

lista = Lista_ordenada_sin_repeticion(lambda x: -x)

elementos_a_añadir = [23, 47, 47, 1, 2, -3, 4, 5]
for elemento in elementos_a_añadir:
    lista.add(elemento)

print("Resultado de la lista ordenada sin repetición:", lista)

elemento_eliminado = lista.remove(47)
print("El elemento eliminado al utilizar remove():", elemento_eliminado)

lista.add(47)
elementos_eliminados = lista.remove_all()
print("Elementos eliminados al utilizar remove_all():", elementos_eliminados)

lista.add(23)
lista.add(5)
lista.add(4)
lista.add(47)
lista.add(2)
lista.add(1)
lista.add(-3)
  
lista.add(0)
print("Lista después de añadirle el 0:", lista) 

lista.add(0)
print("Lista después de añadirle el 0:", lista)
 
lista.add(7)
print("Lista después de añadirle el 7:", lista)