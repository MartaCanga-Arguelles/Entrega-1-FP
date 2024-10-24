'''
Created on 24 oct 2024

@author: Marta
'''
import math

def P2(n:int, k:int, i:int) -> int:
 
    assert n > 0, "n debe ser mayor que 0."
    assert k > 0, "k debe ser mayor que 0."
    assert i > 0, "i debe ser mayor que 0."
    assert n >= k, "n debe ser mayor o igual que k."
    assert i < k, "i debe ser menor que k."
    resultado = 1
    for j in range(i, k+1):
        resultado *= (n - j + 1)
    return resultado

if __name__ == "__main__":
    test_cases = [
        (4, 2, 1),
        (0, 2, 3),
        (1, 0, 3), 
        (1, 2, 0), 
        (2, 2, 2),  
        (1, 2, 1),  
    ]

    for n, k, i in test_cases:
        try:
            resultado = P2(n, k, i)
            print(f"El resultado de P2({n}, {k}, {i}) es: {resultado}")
        except AssertionError as e:
            print(f"Error en P2({n}, {k}, {i}): {e}")
        except Exception as e:
            print(f"Se produjo un error inesperado en P2({n}, {k}, {i}): {e}")



def número_combinatorio(n: int, k: int) -> int:
    if k > n or k < 0:
        return 0
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))

def C2(n: int, k: int) -> int:
    assert n > 0, "n debe ser un número positivo."
    assert k >= 0, "k debe ser un número no negativo."
    assert n > k, "n debe ser mayor que k."
    return número_combinatorio(n, k + 1)

if __name__ == "__main__":
    test_cases = [
        (5, 2),      
        (2, -1), 
        (-1, 2),  
        (2, 2),  
    ]

    for n, k in test_cases:
        try:
            resultado = C2(n, k)
            print(f"El resultado de C2({n}, {k}) es: {resultado}")
        except AssertionError as e:
            print(f"Error en C2({n}, {k}): {e}")
        except Exception as e:
            print(f"Se produjo un error inesperado en C2({n}, {k}): {e}")


def S2(n: int, k: int) -> float:
    assert n > 0, "n debe ser un número positivo."
    assert k > 0, "k debe ser un número positivo."
    assert n >= k, "n debe ser mayor o igual que k."
    suma = 0
    for i in range(k + 1):
        suma += ((-1)**i)*número_combinatorio(k, i)*(k-i)**(n + 1)
    return suma * (math.factorial(k) / (n*(math.factorial(k + 2))))

if __name__ == "__main__":
    n = 4
    k = 2

    try:
        resultado = S2(n, k)
        print(f"El resultado de S2({n}, {k}) es: {resultado}")
    except AssertionError as e:
        print(f"Error: {e}")
    test_cases = [
        (0, 2),
        (4, 0),
        (2, 4)
    ]

    for n, k in test_cases:
        try:
            print(f"S2({n}, {k}) = {S2(n, k)}")
        except AssertionError as e:
            print(f"Error en S2({n}, {k}): {e}")


from collections import Counter
from typing import List, Tuple

def palabrasMasComunes(fichero: str, n: int = 5) -> List[Tuple[str, int]]:
    assert n > 1, "n debe ser mayor que 1."
    with open(fichero, 'r', encoding='utf-8') as file:
        contenido = file.read()
    palabras = contenido.lower().split()
    contador = Counter(palabras)
    palabras_comunes = contador.most_common(n)
    return palabras_comunes

if __name__ == "__main__":
    try:
        resultado = palabrasMasComunes("archivo_palabras.txt", 5)
        print(resultado)
    except Exception as e:
        print(f"Error: {e}")