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
    for path, dirs, files in os.walk(Descargas):
        for arch in files:
            #Asignatura TSI
            if "TSI" in arch:
                arch_nuevo=compruebaArchivo("TSI", arch)
                os.rename(os.path.join(Descargas,arch), os.path.join(UGR, "TSI/" + arch_nuevo))
            #Asignatura FBD
            elif "FBD" in arch:
                arch_nuevo=compruebaArchivo("FBD", arch)
                os.rename(os.path.join(Descargas,arch), os.path.join(UGR, "FBD/" + arch_nuevo))
            #Asignatura IC
            elif "IC" in arch:
                arch_nuevo=compruebaArchivo("IC", arch)
                os.rename(os.path.join(Descargas,arch), os.path.join(UGR, "IC/" + arch_nuevo))
            #Asignatura IA
            elif "IA" in arch:
                arch_nuevo=compruebaArchivo("IA", arch)
                os.rename(os.path.join(Descargas,arch), os.path.join(UGR, "IA/" + arch_nuevo))
            #Asignatura AC
            elif "AC" in arch:
                arch_nuevo=compruebaArchivo("AC", arch)
                os.rename(os.path.join(Descargas,arch), os.path.join(UGR, "AC/" + arch_nuevo))
            #Asignatura ALG
            elif "ALG" in arch:
                arch_nuevo=compruebaArchivo("ALG", arch)
                os.rename(os.path.join(Descargas,arch), os.path.join(UGR, "ALG/" + arch_nuevo))

mueveArchivos()
