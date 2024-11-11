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

class ListaOrdenada(Agregado_lineal):
    def __init__(self, order: Callable[[E], R]):
        super().__init__()
        self._order = order 
        
    def of(order: Callable[[E], R]) -> 'ListaOrdenada[E]':
        return ListaOrdenada(order)
    
    def __index_order(self, e: E) -> int:
        low, high = 0, len(self._elements)
        while low < high:
            mid = (low + high) // 2
            if self._order(self._elements[mid]) < self._order(e):
                low = mid + 1
            else:
                high = mid
        return low

    def add(self, e: E) -> None:
        index = self.__index_order(e)  
        self._elements.insert(index, e) 

    def __repr__(self) -> str:
        return f"ListaOrdenada([{', '.join(map(str, self._elements))}])"
