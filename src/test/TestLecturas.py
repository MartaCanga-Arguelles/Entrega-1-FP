'''
Created on 10 oct 2024

@author: carme
'''
from lecturas.lecturas import palabra_repetida
from lecturas.lecturas import lineas_cadenas_texto
from lecturas.lecturas import palabras_unicas
from lecturas.lecturas import longitud_promedio_lineas
from lecturas.lecturas import longitud_promedio_lineas

cad = "quijote"
separador = " "
archivo = "lin_quijote.txt"

print(f"El número de veces que aparece la palabra {cad} en el fichero {archivo} es: {palabra_repetida(archivo, cad, separador)}")

nombre_fichero = "lin_quijote.txt"
cad = "quijote"

print(f"Las líneas en las que aparece la palabra {cad} son: {lineas_cadenas_texto(nombre_fichero, cad)}")

nombre_fichero = "archivo_palabras.txt"
print(f"Las palabras únicas en el fichero {nombre_fichero} son: {palabras_unicas(nombre_fichero)}")

file_path = "palabras_random.csv"
print(f"La longitud promedio de las líneas del fichero {file_path} es: {longitud_promedio_lineas(file_path)}")

file_path = "vacio.csv"
print(f"La longitud promedio de las líneas del fichero {file_path} es: {longitud_promedio_lineas(file_path)}")