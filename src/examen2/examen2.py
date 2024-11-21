'''
Created on 21 nov 2024

@author: carme
'''
from abc import ABC
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
    
    def remove(self, elemento: E) -> E:
        print(f"Intentando eliminar el elemento: {elemento}")
        print(f"Estado de la cola antes de eliminar: {self._elements}")
        if elemento in self._elements:
            self._elements.remove(elemento)  # Eliminar el primer elemento encontrado
            print(f"Elemento {elemento} eliminado. Estado actual de la cola: {self._elements}")
            return elemento
        else:
            raise ValueError(f"El elemento {elemento} no se encuentra en la lista.")

    def remove_all(self) -> List[E]:
        elementos_eliminados = self._elements[:]
        self._elements.clear()
        return elementos_eliminados


class ColaConLimite(Agregado_lineal[E]):
    def __init__(self, capacidad: int):
        super().__init__()
        self.capacidad = capacidad

    def add(self, e: E) -> None:
        if self.size() >= self.capacidad:
            raise OverflowError("La cola está llena.")
        self._elements.append(e)

    def is_full(self) -> bool:
        return self.size() >= self.capacidad

    @classmethod
    def of(cls, capacidad: int):
        return cls(capacidad)

from typing import Callable, Optional


class Agregado_lineal_modificado(ABC, Generic[E]):
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
        print(f"Intentando eliminar el elemento: {elemento}")
        print(f"Estado de la cola antes de eliminar: {self._elements}")
        if elemento in self._elements:
            self._elements.remove(elemento)  # Eliminar el primer elemento encontrado
            print(f"Elemento {elemento} eliminado. Estado actual de la cola: {self._elements}")
            return elemento
        else:
            raise ValueError(f"El elemento {elemento} no se encuentra en la lista.")

    def remove_all(self) -> List[E]:
        elementos_eliminados = self._elements[:]
        self._elements.clear()
        return elementos_eliminados

    def contains(self, e: E) -> bool:
        return e in self._elements
    
    def find(self, func: Callable[[E], bool]) -> Optional[E]:
        for e in self._elements:
            if func(e):
                return e
        return None

    def filter(self, func: Callable[[E], bool]) -> List[E]:
        return [e for e in self._elements if func(e)]


def test_cola_con_limite():
    print("=== INICIO DE PRUEBAS PARA ColaConLimite ===")

    # Prueba: Inicialización vacía
    print("\nPrueba: Inicialización vacía")
    cola = ColaConLimite.of(5)
    assert cola.is_empty(), "Error: La cola debería estar vacía al inicializarse."
    assert not cola.is_full(), "Error: La cola no debería estar llena al inicializarse."
    assert cola.size() == 0, "Error: El tamaño inicial debería ser 0."
    assert cola.elements() == [], "Error: La lista de elementos inicial debería estar vacía."
    print("Inicialización vacía: OK")

    # Prueba: Agregar elementos dentro de la capacidad
    print("\nPrueba: Agregar elementos dentro de la capacidad")
    cola.add("Tarea 1")
    cola.add("Tarea 2")
    cola.add("Tarea 3")
    assert cola.size() == 3, "Error: El tamaño debería ser 3."
    assert cola.elements() == ["Tarea 1", "Tarea 2", "Tarea 3"], "Error: Los elementos no coinciden."
    print("Agregar elementos dentro de la capacidad: OK")

    # Prueba: Exceder la capacidad
    print("\nPrueba: Exceder la capacidad")
    try:
        cola.add("Tarea 4")
        cola.add("Tarea 5")
        print("Error: Se esperaba OverflowError al agregar más elementos de la capacidad.")
    except OverflowError:
        print("Exceder la capacidad: OK")

    # Prueba: Eliminar un elemento específico
    print("\nPrueba: Eliminar un elemento específico")
    print(f"Estado de la cola antes de eliminar: {cola.elements()}")
    
    if "Tarea 2" in cola.elements():
        cola.remove("Tarea 2")
        print(f"Estado de la cola después de eliminar: {cola.elements()}")
    else:
        print("Error: No se encuentra 'Tarea 2' en la cola antes de la eliminación.")
    
    assert cola.size() == 2, "Error: El tamaño debería ser 2 después de eliminar un elemento."
    assert cola.elements() == ["Tarea 1", "Tarea 3"], "Error: Los elementos restantes no coinciden."
    print("Eliminar un elemento específico: OK")

    # Prueba: Eliminar un elemento inexistente
    print("\nPrueba: Eliminar un elemento inexistente")
    try:
        cola.remove("Tarea 4")
        print("Error: Se esperaba ValueError al eliminar un elemento inexistente.")
    except ValueError:
        print("Eliminar un elemento inexistente: OK")

    # Prueba: Verificar si la cola está llena
    print("\nPrueba: Verificar si la cola está llena")
    cola.add("Tarea 4")
    cola.add("Tarea 5")
    assert cola.is_full(), "Error: La cola debería estar llena."
    print("Verificar si la cola está llena: OK")

    # Prueba: Verificar si la cola está vacía
    print("\nPrueba: Verificar si la cola está vacía")
    cola.remove_all()
    assert cola.is_empty(), "Error: La cola debería estar vacía después de eliminar todos los elementos."
    print("Verificar si la cola está vacía: OK")

    # Prueba: Agregar una lista de elementos dentro de la capacidad
    print("\nPrueba: Agregar una lista de elementos dentro de la capacidad")
    cola = ColaConLimite.of(4)
    cola.add_all(["Tarea 1", "Tarea 2", "Tarea 3"])
    assert cola.size() == 3, "Error: El tamaño debería ser 3 después de agregar elementos de una lista."
    assert cola.elements() == ["Tarea 1", "Tarea 2", "Tarea 3"], "Error: Los elementos no coinciden."
    print("Agregar una lista de elementos dentro de la capacidad: OK")

    # Prueba: Agregar una lista que excede la capacidad
    print("\nPrueba: Agregar una lista que excede la capacidad")
    try:
        cola.add_all(["Tarea 4", "Tarea 5"])
        print("Error: Se esperaba OverflowError al agregar una lista que excede la capacidad.")
    except OverflowError:
        print("Agregar una lista que excede la capacidad: OK")

    print("\n=== TODAS LAS PRUEBAS SE COMPLETARON CORRECTAMENTE ===")

test_cola_con_limite()

def test_agregado_lineal_modificado():
    print("=== INICIO DE PRUEBAS PARA Agregado_lineal_modificado ===")
    
    # Crear una instancia de Agregado_lineal_modificado de tipo str
    agregado = Agregado_lineal_modificado[str]()
    
    # Prueba: Inicialización vacía
    print("\nPrueba: Inicialización vacía")
    assert agregado.is_empty(), "Error: El agregado debería estar vacío al inicializarse."
    assert agregado.size() == 0, f"Error: El tamaño inicial debería ser 0. Tamaño actual: {agregado.size()}"
    print("Inicialización vacía: OK")
    
    # Prueba: Agregar un solo elemento
    print("\nPrueba: Agregar un solo elemento")
    agregado.add("Elemento 1")
    assert agregado.size() == 1, f"Error: El tamaño debería ser 1. Tamaño actual: {agregado.size()}"
    assert agregado.elements() == ["Elemento 1"], f"Error: El elemento agregado no coincide. Elementos actuales: {agregado.elements()}"
    print("Agregar un solo elemento: OK")
    
    # Prueba: Agregar múltiples elementos
    print("\nPrueba: Agregar múltiples elementos")
    agregado.add_all(["Elemento 2", "Elemento 3", "Elemento 4"])
    assert agregado.size() == 4, f"Error: El tamaño debería ser 4. Tamaño actual: {agregado.size()}"
    assert agregado.elements() == ["Elemento 1", "Elemento 2", "Elemento 3", "Elemento 4"], f"Error: Los elementos no coinciden. Elementos actuales: {agregado.elements()}"
    print("Agregar múltiples elementos: OK")
    
    # Prueba: Verificar si contiene un elemento
    print("\nPrueba: contains()")
    assert agregado.contains("Elemento 2"), "Error: Debería contener 'Elemento 2'."
    assert not agregado.contains("Elemento 5"), "Error: No debería contener 'Elemento 5'."
    print("contains() - Verificación: OK")
    
    # Prueba: Buscar un elemento usando find()
    print("\nPrueba: find()")
    found = agregado.find(lambda x: "Elemento 3" in x)
    assert found == "Elemento 3", f"Error: Debería encontrar 'Elemento 3'. Encontrado: {found}"
    
    found = agregado.find(lambda x: "Elemento 5" in x)
    assert found is None, "Error: No debería encontrar 'Elemento 5'."
    print("find() - Búsqueda: OK")
    
    # Prueba: Filtrar elementos usando filter()
    print("\nPrueba: filter()")
    filtered = agregado.filter(lambda x: "Elemento" in x)
    assert filtered == ["Elemento 1", "Elemento 2", "Elemento 3", "Elemento 4"], f"Error: Los elementos filtrados no coinciden. Filtrados: {filtered}"

    filtered = agregado.filter(lambda x: "3" in x)
    assert filtered == ["Elemento 3"], f"Error: El filtro debería devolver solo 'Elemento 3'. Filtrados: {filtered}"
    print("filter() - Filtrado: OK")
    
    # Prueba: Eliminar un elemento existente
    print("\nPrueba: Eliminar un elemento específico")
    removed = agregado.remove("Elemento 2")
    assert removed == "Elemento 2", f"Error: Debería eliminar 'Elemento 2'. Eliminado: {removed}"
    assert agregado.size() == 3, f"Error: El tamaño debería ser 3 después de eliminar un elemento. Tamaño actual: {agregado.size()}"
    assert "Elemento 2" not in agregado.elements(), "Error: 'Elemento 2' no debería estar en los elementos después de eliminarlo."
    print("Eliminar un elemento específico: OK")
    
    # Prueba: Eliminar un elemento inexistente
    print("\nPrueba: Eliminar un elemento inexistente")
    try:
        agregado.remove("Elemento 5")
        print("Error: Se esperaba ValueError al eliminar un elemento inexistente.")
    except ValueError:
        print("Eliminar un elemento inexistente: OK")
    
    # Prueba: Eliminar todos los elementos
    print("\nPrueba: Vaciar todos los elementos")
    removed_all = agregado.remove_all()
    assert removed_all == ["Elemento 1", "Elemento 3", "Elemento 4"], f"Error: Los elementos eliminados no coinciden. Eliminados: {removed_all}"
    assert agregado.is_empty(), "Error: El agregado debería estar vacío después de eliminar todos los elementos."
    print("Vaciar todos los elementos: OK")

    # Prueba: Verificar si el agregado está vacío
    print("\nVerificar si el agregado está vacío después de vaciarlo")
    assert agregado.is_empty(), "Error: El agregado debería estar vacío."
    print("Verificación si está vacío: OK")

    # Prueba: Agregar elementos después de vaciar
    print("\nPrueba: Agregar elementos después de vaciar")
    agregado.add("Elemento 5")
    agregado.add("Elemento 6")
    assert agregado.size() == 2, f"Error: El tamaño debería ser 2. Tamaño actual: {agregado.size()}"
    assert agregado.elements() == ["Elemento 5", "Elemento 6"], f"Error: Los elementos no coinciden. Elementos actuales: {agregado.elements()}"
    print("Agregar elementos después de vaciar: OK")
    
    print("\n=== TODAS LAS PRUEBAS SE COMPLETARON CORRECTAMENTE ===")

test_agregado_lineal_modificado()
