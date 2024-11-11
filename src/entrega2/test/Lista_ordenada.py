'''
Created on 10 nov 2024

@author: carme
'''
from entrega2.tipos.Lista_ordenada import ListaOrdenada
lista = ListaOrdenada(lambda x: x)
lista.add(3)
lista.add(1)
lista.add(2)
print(lista)

elemento_eliminado = lista.remove(1)
print("El elemento eliminado al utilizar remove():", elemento_eliminado)

lista.add(1)
elementos_eliminados = lista.remove_all()
print("Elementos eliminados al utilizar remove_all():", elementos_eliminados)

lista.add(1)
lista.add(3)
lista.add(2)
  
lista.add(0)
print("Lista después de añadirle el 0:", lista) 

lista.add(10)
print("Lista después de añadirle el 10:", lista)
 
lista.add(7)
print("Lista después de añadirle el 7:", lista)