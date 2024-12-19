'''
Created on 19 dic 2024

@author: carme
'''
from typing import TypeVar, Generic, Dict, List, Set
class Gen:
    def __init__(self, nombre: str, tipo: str, num_mutaciones: int, loc_cromosoma: str):
        if num_mutaciones < 0:
            raise ValueError("El número de mutaciones debe ser mayor o igual a 0")
        self._nombre = nombre
        self._tipo = tipo
        self._num_mutaciones = num_mutaciones
        self._loc_cromosoma = loc_cromosoma

    @property
    def nombre(self):
        return self._nombre

    @property
    def tipo(self):
        return self._tipo

    @property
    def num_mutaciones(self):
        return self._num_mutaciones

    @property
    def loc_cromosoma(self):
        return self._loc_cromosoma

    @classmethod
    def of(cls, nombre: str, tipo: str, num_mutaciones: int, loc_cromosoma: str) -> 'Gen':
        return cls(nombre, tipo, num_mutaciones, loc_cromosoma)

    @classmethod
    def parse(cls, cadena: str) -> 'Gen':
        partes = cadena.split(',')
        if len(partes) != 4:
            raise ValueError("La cadena no tiene el formato correcto")
        nombre, tipo, num_mutaciones, loc_cromosoma = partes
        return cls(nombre, tipo, int(num_mutaciones), loc_cromosoma)

    def __str__(self):
        return f"Gen(nombre={self.nombre}, tipo={self.tipo}, num_mutaciones={self.num_mutaciones}, loc_cromosoma={self.loc_cromosoma})"

    def __eq__(self, other):
        if isinstance(other, Gen):
            return self.nombre == other.nombre
        return False

    def __hash__(self):
        return hash(self.nombre)


# Clase RelacionGenAGen
class RelacionGenAGen:
    def __init__(self, nombre_gen1: str, nombre_gen2: str, conexion: float):
        if not isinstance(nombre_gen1, str):
            raise TypeError("nombre_gen1 debe ser un string")
        if not isinstance(nombre_gen2, str):
            raise TypeError("nombre_gen2 debe ser un string")
        if not isinstance(conexion, float):
            raise TypeError("conexion debe ser un float")
        if not -1 <= conexion <= 1:
            raise ValueError("conexion debe estar entre -1 y 1")
        
        self.nombre_gen1 = nombre_gen1
        self.nombre_gen2 = nombre_gen2
        self.conexion = conexion

    @staticmethod
    def of(nombre_gen1: str, nombre_gen2: str, conexion: float) -> 'RelacionGenAGen':
        return RelacionGenAGen(nombre_gen1, nombre_gen2, conexion)

    @staticmethod
    def parse(cadena: str) -> 'RelacionGenAGen':
        partes = cadena.split(',')
        if len(partes) != 3:
            raise ValueError("La cadena no tiene el formato correcto")
        nombre_gen1, nombre_gen2, conexion = partes
        return RelacionGenAGen(nombre_gen1, nombre_gen2, float(conexion))

    def __str__(self):
        return f"RelacionGenAGen(nombre_gen1={self.nombre_gen1}, nombre_gen2={self.nombre_gen2}, conexion={self.conexion})"


# Definir los tipos genéricos
TGen = TypeVar('TGen')
TRelacionGenAGen = TypeVar('TRelacionGenAGen')


# Clase Grafo genérica
class Grafo(Generic[TGen, TRelacionGenAGen]):
    def __init__(self, es_dirigido: bool = False) -> None:
        self.es_dirigido = es_dirigido
        self.vertices: Dict[TGen, List[TRelacionGenAGen]] = {}
    
    def agregar_vertice(self, vertice: TGen) -> None:
        if vertice not in self.vertices:
            self.vertices[vertice] = []

    def agregar_arista(self, vertice1: TGen, vertice2: TGen, relacion: TRelacionGenAGen) -> None:
        self.vertices[vertice1].append(relacion)
        if not self.es_dirigido:
            self.vertices[vertice2].append(relacion)


# Clase RedGenica que hereda de Grafo
class RedGenica(Grafo[Gen, RelacionGenAGen]):
    def __init__(self, es_dirigido: bool = False) -> None:
        super().__init__(es_dirigido)
        self.genes_por_nombre: Dict[str, Gen] = {}

    @staticmethod
    def of(es_dirigido: bool = False) -> 'RedGenica':
        return RedGenica(es_dirigido)

    @staticmethod
    def parse(f1: str, f2: str, es_dirigido: bool = False) -> 'RedGenica':
        red = RedGenica.of(es_dirigido)
        
        # Leer y agregar genes desde f1
        with open(f1, 'r') as archivo_genes:
            for linea in archivo_genes:
                gen = Gen.parse(linea.strip())
                red.agregar_vertice(gen)
                red.genes_por_nombre[gen.nombre] = gen
        
        # Leer y agregar relaciones desde f2
        with open(f2, 'r') as archivo_relaciones:
            for linea in archivo_relaciones:
                relacion = RelacionGenAGen.parse(linea.strip())
                gen1 = red.genes_por_nombre[relacion.nombre_gen1]
                gen2 = red.genes_por_nombre[relacion.nombre_gen2]
                red.agregar_arista(gen1, gen2, relacion)
        
        return red

    def dfs(self, inicio: str, destino: str, visitados: Set[str] = None) -> List[Gen]:
        if visitados is None:
            visitados = set()
        if inicio == destino:
            return [self.genes_por_nombre[inicio]]
        
        visitados.add(inicio)
        for relacion in self.vertices[self.genes_por_nombre[inicio]]:
            vecino = relacion.nombre_gen2 if relacion.nombre_gen1 == inicio else relacion.nombre_gen1
            if vecino not in visitados:
                camino = self.dfs(vecino, destino, visitados)
                if camino:
                    return [self.genes_por_nombre[inicio]] + camino
        
        return []

    def subgrafo(self, genes: List[Gen]) -> 'RedGenica':
        subgrafo = RedGenica(self.es_dirigido)
        for gen in genes:
            if gen.nombre in self.genes_por_nombre:
                gen_original = self.genes_por_nombre[gen.nombre]
                subgrafo.agregar_vertice(gen_original)
                subgrafo.genes_por_nombre[gen_original.nombre] = gen_original
            else:
                    raise KeyError(f"El gen {gen.nombre} no está presente en el grafo original.")
    
        for gen in genes:
            gen_original = self.genes_por_nombre[gen.nombre]
            for relacion in self.vertices[gen_original]:
                gen1 = self.genes_por_nombre[relacion.nombre_gen1]
                gen2 = self.genes_por_nombre[relacion.nombre_gen2]
                if gen1 in subgrafo.vertices and gen2 in subgrafo.vertices:
                    subgrafo.agregar_arista(gen1, gen2, relacion)
                    return subgrafo


# Código de prueba
if __name__ == "__main__":
    # Crear la red génica desde archivos
    red_genica = RedGenica.parse("genes.txt", "red_genes.txt", es_dirigido=False)
    
    # Paso 2: Recorrido en profundidad desde KRAS hasta PIK3CA
    camino = red_genica.dfs("KRAS", "PIK3CA")
    print("Camino DFS:", [gen.nombre for gen in camino])
    
    # Paso 3: Crear subgrafo y mostrarlo
    subgrafo = red_genica.subgrafo(camino)
    print("Subgrafo generado:")
    for gen, relaciones in subgrafo.vertices.items():
        print(f"{gen.nombre}: {[str(relacion) for relacion in relaciones]}")
