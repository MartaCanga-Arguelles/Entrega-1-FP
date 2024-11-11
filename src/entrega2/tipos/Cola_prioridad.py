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

class ColaPrioridad(Agregado_lineal):
    def __init__(self):
        super().__init__()
        self._priorities: List[R] = [] 
    
    def of() -> 'ColaPrioridad[E, R]':
        return ColaPrioridad()

    def __index_order(self, priority: R) -> int:
        low, high = 0, len(self._priorities)
        while low < high:
            mid = (low + high) // 2
            if self._priorities[mid] < priority:
                low = mid + 1
            else:
                high = mid
        return low

    def add(self, e: E, priority: R) -> None:
        index = self.__index_order(priority) 
        self._elements.insert(index, e) 
        self._priorities.insert(index, priority)  
    
    def add_all(self, ls: List[tuple[E, R]]) -> None:
        for e, priority in ls:
            self.add(e, priority)

    def remove(self) -> E:
        assert len(self._elements) > 0, 'El agregado está vacío'
        self._priorities.pop(0) 
        return self._elements.pop(0)

    def remove_all(self) -> List[E]:
        removed_elements = []
        while not self.is_empty():
            removed_elements.append(self.remove())
        return removed_elements

    def decrease_priority(self, e: E, new_priority: R) -> None:
        index = self._elements.index(e)
        if new_priority < self._priorities[index]:
            self._elements.pop(index)
            self._priorities.pop(index)
            self.add(e, new_priority)

    def __repr__(self) -> str:
        return f"ColaPrioridad[{', '.join(f'({str(e)}, {str(r)})' for e, r in zip(self._elements, self._priorities))}]"