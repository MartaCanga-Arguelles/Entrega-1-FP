'''
Created on 10 nov 2024

@author: carme
'''
from entrega2.tipos.Cola import Cola

cola = Cola.of()

cola.add_all([23, 47, 1, 2, -3, 4, 5])
print("Resultado de la cola:", cola) 

elementos_eliminados = cola.remove_all()
print("Elementos eliminados utilizando remove_all:", elementos_eliminados)