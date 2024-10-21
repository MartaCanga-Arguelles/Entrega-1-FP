'''
Created on 10 oct 2024

@author: Marta
'''
from collections import Counter
from pickle import NONE

def palabra_repetida(archivo, cad, separador):
    try:
        with open(archivo, "r", encoding="utf-8") as fichero:
            contenido = fichero.read()
            contenido = contenido.lower()
            palabras = contenido.split()
            contador = palabras.count(cad)
            
        return contador
    except FileNotFoundError:
        print("El archivo no ha sido encontrado")
        return 0



def lineas_cadenas_texto(nombre_fichero, cad):
    lineas_encontradas = []
    with open(nombre_fichero, "r", encoding="utf-8") as fichero:
        cad_lower = cad.lower()
        for linea in fichero:
            if cad_lower in linea.lower():
                lineas_encontradas.append(linea.strip())
                
    return lineas_encontradas



def palabras_unicas(nombre_fichero):
    palabras = set()
    try:
        with open(nombre_fichero, "r", encoding="utf-8") as fichero:
            for linea in fichero:
                for palabra in linea.split():
                    palabras.add(palabra.strip())
    except FileNotFoundError:
        print(f"error fichero")
    except Exception as e:
        print(f"error e")
        
    return list(palabras)


from typing import Optional
def longitud_promedio_lineas(file_path: str) -> Optional[float]:
    try:
        with open(file_path, "r", encoding="utf-8") as fichero:
            lineas = fichero.readlines()
            if not lineas:
                return None 
            l_total = 0
            t_terminos = 0
            for linea in lineas:
                linea = linea.strip()
                linea = linea.split(",")
                l_linea = len(linea)
                l_total += l_linea
                t_terminos += 1
            return l_total / t_terminos
        
    except IOError as e:
        print(f"error e")
        return 0
    

