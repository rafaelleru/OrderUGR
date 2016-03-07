#!/bin/usr/python3
import sys
import os

home = os.path.expanduser("~")
Descargas = os.path.join(home, "Descargas")
UGR = os.path.join(home, "UGR")

primero = os.path.join(UGR, "primero")
segundo = os.path.join(UGR, "segundo")
tercero = os.path.join(UGR, "tercero")
cuarto = os.path.join(UGR, "cuarto")

curso1 = [
    'CA', 'ALEM', 'FS', 'FP', 'FFT'
    'LMD', 'TOC', 'MP', 'ES', 'IES']

curso2 = [
    'SO', 'SCD', 'EC', 'ED', 'PDOO',
    'IA', 'FIS', 'AC', 'ALG', 'FBD']

curso3 = [
    'MC', 'IG', 'DDSI', 'FR', 'ISE',
    ] #Mas cosas

cursos = [ curso1, curso2, curso3 ]
path_cursos = [primero, segundo, tercero, cuarto]

def eliminaCadena(cadena, archivo):
    archivo_nuevo = ""

    if "_"+cadena in archivo:
        archivo_nuevo = archivo.replace("_"+cadena, '')
    elif "-"+cadena in archivo:
        archivo_nuevo = archivo.replace("-"+cadena, '')
    else:
        archivo_nuevo = archivo

    return archivo_nuevo


def renombraPath(archivo):
    nuevo_path = None
    for curso in cursos:
        for asignatura in curso:
            if asignatura in archivo:
                ncurso = cursos.index(curso)
                archivo_nuevo = eliminaCadena(asignatura, archivo)
                nuevo_path = os.path.join(path_cursos[ncurso], os.path.join(asignatura, archivo_nuevo))
    return nuevo_path

def mueveArchivos():

    for path, dirs, files in os.walk(Descargas):
        for arch in files:
            nuevo_archivo = renombraPath(arch)
            if not (nuevo_archivo is None):
                os.rename(os.path.join(Descargas, arch), nuevo_archivo)
                print(nuevo_archivo)


mueveArchivos()
