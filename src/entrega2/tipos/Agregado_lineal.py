'''
Created on 10 nov 2024

@author: carme
'''
from abc import ABC, abstractmethod
from typing import List, Callable, TypeVar, Generic

E = TypeVar('E') 
R = TypeVar('R') 

class Agregado_lineal(ABC):
    def __init__(self):
        self._elements: List[E] = []
    
    def size(self) -> int:
        return len(self._elements)
    
    def is_empty(self) -> bool:
        return len(self._elements) == 0
    
    def elements(self) -> List[E]:
        return self._elements
    
    def add(self, e: E) -> None:
        pass
    
    def add_all(self, ls: List[E]) -> None:
        for e in ls:
            self.add(e)
    
    def remove(self, elemento: E) -> E:
        if elemento in self._elements:
            self._elements.remove(elemento)
            return elemento
        else:
            raise ValueError(f"El elemento {elemento} no se encuentra en la lista.")

    def remove_all(self) -> List[E]:
        elementos_eliminados = self._elements[:]
        self._elements.clear()
        return elementos_eliminados

