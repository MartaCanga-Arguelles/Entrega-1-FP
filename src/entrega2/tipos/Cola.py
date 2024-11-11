'''
Created on 10 nov 2024

@author: carme
'''
from abc import ABC, abstractmethod
from typing import List, TypeVar, Generic

E = TypeVar('E')  

class Agregado_lineal(ABC, Generic[E]):
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
    
    def remove(self) -> E:
        assert not self.is_empty(), 'El agregado está vacío'
        return self._elements.pop(0)

    def remove_all(self) -> List[E]:
        elementos_eliminados = self._elements[:]
        self._elements.clear()
        return elementos_eliminados

class Cola(Agregado_lineal[E]):
    def __init__(self):
        super().__init__()

    def of() -> 'Cola[E]':
        return Cola()

    def add(self, e: E) -> None:
        self._elements.append(e)

    def __repr__(self) -> str:
        return f"Cola({', '.join(map(str, self._elements))})"


