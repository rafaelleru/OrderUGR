import sys
import os

home = os.path.expanduser("~")
Descargas = os.path.join(home, "Descargas")
UGR = os.path.join(home, "UGR")

def compruebaArchivo(cadena, archivo):
    archivo_nuevo = ""

    if "_"+cadena in archivo:
        archivo_nuevo = archivo.replace("_"+cadena, '')
    elif "-"+cadena in archivo:
        archivo_nuevo = archivo.replace("-"+cadena, '')
    else:
        archivo_nuevo = archivo

    print(archivo_nuevo)
    return archivo_nuevo

def mueveArchivos():
    tipoDeArchivos = [
        'TSI', 'FBD', 'IC',
        'IA', 'AC', 'ALG'
        ]
    for path, dirs, files in os.walk(Descargas):
        for arch in files:
            for tipo in tipoDeArchivos:
                if tipo in arch:
                    arch_nuevo=compruebaArchivo(tipo, arch)
                    os.rename(os.path.join(Descargas,arch), os.path.join(UGR, tipo + "/" + arch_nuevo))   


mueveArchivos()
