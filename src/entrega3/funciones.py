'''
Created on 9 dic 2024

@author: carme
'''
import os
import networkx as nx
import matplotlib.pyplot as plt
from typing import Optional, Dict, List, Tuple, TypeVar, Generic
from datetime import datetime

V = TypeVar('V')  # Tipo de los vértices
E = TypeVar('E')  # Tipo de las aristas

# Clase E_Grafo
class E_Grafo(Generic[V, E]):
    def __init__(self, dirigido=False):
        self.vertices = {}  # Diccionario de vértices
        self.aristas = {}  # Diccionario de aristas
        self.dirigido = dirigido

    def add_vertex(self, v):
        if v not in self.vertices:
            self.vertices[v] = {'vecinos': set(), 'predecesores': set(), 'sucesores': set()}
            return True
        return False

    def add_edge(self, origen, destino):
        if origen == destino:  # No se permiten bucles
            return False
        if origen not in self.vertices or destino not in self.vertices:
            return False
        # Añadir la arista
        self.vertices[origen]['vecinos'].add(destino)
        self.vertices[destino]['vecinos'].add(origen)
        if self.dirigido:
            self.vertices[origen]['sucesores'].add(destino)
            self.vertices[destino]['predecesores'].add(origen)
        return True

    def to_networkx_graph(self):
        """Convierte el grafo en un grafo de networkx para su visualización"""
        G = nx.DiGraph() if self.dirigido else nx.Graph()
        for v in self.vertices:
            G.add_node(v)
        for origen in self.vertices:
            for destino in self.vertices[origen]['vecinos']:
                G.add_edge(origen, destino)
        return G


# Clase Recorrido (BFS y DFS)
class Recorrido(Generic[V, E]):
    def __init__(self, grafo: E_Grafo[V, E], origen: V):
        self._grafo = grafo
        self._origen = origen
        self._tree = {}  # Estructura para almacenar el árbol de recorrido
        self._path = []  # Lista para almacenar el camino
        self._init_recorrido()

    def _init_recorrido(self):
        """Método para inicializar el recorrido, comenzando desde el origen"""
        # Iniciar el árbol con el origen
        self._tree[self._origen] = (None, 0.0)  # El origen no tiene predecesor y su distancia es 0
        self._path.append(self._origen)

    def bfs(self):
        """Método de recorrido en amplitud (BFS)"""
        visited = set()
        queue = [self._origen]
        while queue:
            node = queue.pop(0)
            if node not in visited:
                visited.add(node)
                for neighbor in self._grafo.vertices[node]['vecinos']:
                    if neighbor not in visited:
                        self._tree[neighbor] = (node, self._tree[node][1] + 1)
                        queue.append(neighbor)
        return self._tree

    def dfs(self):
        """Método de recorrido en profundidad (DFS)"""
        visited = set()
        stack = [self._origen]
        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                for neighbor in self._grafo.vertices[node]['vecinos']:
                    if neighbor not in visited:
                        self._tree[neighbor] = (node, self._tree[node][1] + 1)
                        stack.append(neighbor)
        return self._tree


# Definición de clases Usuario y Relacion
class Usuario:
    def __init__(self, dni: str, nombre: str, apellidos: str, fecha_nacimiento: str):
        self.dni = dni
        self.nombre = nombre
        self.apellidos = apellidos
        self.fecha_nacimiento = datetime.strptime(fecha_nacimiento, "%Y-%m-%d").date()

    @classmethod
    def parse(cls, cadena: str) -> 'Usuario':
        dni, nombre, apellidos, fecha_nacimiento = cadena.split(',')
        return cls(dni, nombre, apellidos, fecha_nacimiento)

    def __str__(self):
        return f"{self.dni} - {self.nombre} {self.apellidos}"


class Relacion:
    _xx_num = 0  # Contador estático para generar IDs únicos

    def __init__(self, interacciones: int, dias_activa: int):
        Relacion._xx_num += 1
        self.id = Relacion._xx_num
        self.interacciones = interacciones
        self.dias_activa = dias_activa

    @classmethod
    def of(cls, interacciones: int, dias_activa: int) -> 'Relacion':
        return cls(interacciones, dias_activa)

    def __str__(self):
        return f"({self.id} - días activa: {self.dias_activa} - num interacciones: {self.interacciones})"


# Clase Red_social
class Red_social(E_Grafo[Usuario, Relacion]):
    def __init__(self, tipo_grafo='no dirigido'):
        super().__init__(dirigido=(tipo_grafo == 'dirigido'))
        self.usuarios_dni = {}

    @classmethod
    def parse(cls, archivo_usuarios: str, archivo_relaciones: str) -> 'Red_social':
        red_social = cls()
        
        # Leer usuarios
        with open(archivo_usuarios, 'r') as f_usuarios:
            for linea in f_usuarios:
                usuario = Usuario.parse(linea.strip())
                red_social.add_vertex(usuario.dni)
                red_social.usuarios_dni[usuario.dni] = usuario

        # Leer relaciones
        with open(archivo_relaciones, 'r') as f_relaciones:
            for linea in f_relaciones:
                id_usuario1, id_usuario2, interacciones, dias_activa = linea.strip().split(',')
                interacciones, dias_activa = int(interacciones), int(dias_activa)
                usuario1 = red_social.usuarios_dni.get(id_usuario1)
                usuario2 = red_social.usuarios_dni.get(id_usuario2)
                
                if usuario1 and usuario2:
                    # Crear la relación entre los dos usuarios
                    relacion = Relacion.of(interacciones, dias_activa)
                    red_social.add_edge(usuario1.dni, usuario2.dni)
                    
        return red_social

    def __str__(self):
        return f"Red social con {len(self.usuarios_dni)} usuarios"

import os

if __name__ == "__main__":
    
    f1 = os.path.join(os.path.dirname(__file__), "usuarios.txt")
    f2 = os.path.join(os.path.dirname(__file__), "relaciones.txt")

    rrss = Red_social.parse(f1, f2)

    origen_dni = '251439091'
    destino_dni = '87345530M'

    origen = rrss.usuarios_dni.get(origen_dni)
    destino = rrss.usuarios_dni.get(destino_dni)

    G = rrss.to_networkx_graph()

    import matplotlib.pyplot as plt
    plt.figure(figsize=(10, 8))
    nx.draw(G, with_labels=True, node_color="lightblue", node_size=2000, font_size=10, font_weight="bold")
    plt.title("Red Social de Usuarios")
    plt.show()

