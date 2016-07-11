#!/usr/bin/python3
import os

"""paths de las carpetas, si se tiene otra organizacion distinta cambiar los
que hagan falta"""
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
    #'MC', 'IG', 'DDSI', 'FR', 'ISE',
    #'SWAP', 'TDRC', 'SMM', 'TW', 'CUIA',  # TI
    #'DHD', 'SMP', 'AS', 'ACAP', 'DSE',  # IC
    #'DS', 'SG', 'DSD', 'DIU', 'SIBW',  # IS
    'MCA', 'MH', 'TSI', 'IC', 'AA',  # CSI
    #'SIE', 'PW', 'SMD', 'ISI', 'ABD'  # SI
]  # Mas cosas
"""curso4 = [
    'SE', 'TR', 'CPD', 'IAH', 'TE',
    'II', 'CLP', 'CII', 'MEI', 'EISI',
    'CEGE', 'DI', 'DIU', 'MDA', 'DBA',
    'DGP', 'PGV', 'SSO', 'LP', 'AO',
    'PPR', 'NTP', 'VC', 'NPI', 'PL',
    'TIC', 'SS', 'PTC', 'PLD', 'CRIP',
    'RI', 'IN', 'BDD', 'RI', 'SIG',
    'GRD', 'RSC', 'SCGC', 'PDIH', 'DAI',
    'IV', 'SPSI', 'TID', 'CRIM', 'PDM',
    'PDS', 'PCS', 'RMS', 'RPC', 'FADI',
    'MNI']"""

cursos = [curso1, curso2, curso3]
path_cursos = [primero, segundo, tercero, cuarto]

"""funcion que elimina la cadena que identifica la asignatura de un archivo'
para almacenarlo"""


def eliminaCadena(cadena, archivo):
    archivo_nuevo = None

    if "_" + cadena in archivo:
        archivo_nuevo = archivo.replace("_" + cadena, '')
    elif "-" + cadena in archivo:
        archivo_nuevo = archivo.replace("-" + cadena, '')
    elif cadena + "-" in archivo:
        archivo_nuevo = archivo.replace(cadena + "-", '')
    elif cadena + "_" in archivo:
         archivo_nuevo = archivo.replace(cadena + "_", '')
    elif cadena in archivo:
        archivo_nuevo = archivo.replace(cadena, '')
    else:
        archivo_nuevo = archivo

    return archivo_nuevo

# funcion que devuelve la nueva ruta del archivo


def renombraPath(archivo):
    nuevo_path = None
    for curso in cursos:
        for asignatura in curso:
            if asignatura in archivo:
                ncurso = cursos.index(curso)
                archivo_nuevo = eliminaCadena(asignatura, archivo)
                # si la carpeta para esa asignatura no existe la crea
                if not os.path.isdir(os.path.join(UGR, asignatura)):
                    os.makedirs(os.path.join(path_cursos[ncurso],
                                             asignatura))
                nuevo_path = os.path.join(
                    path_cursos[ncurso], os.path.join(asignatura,
                                                      archivo_nuevo))
    return nuevo_path


def mueveArchivos():

    for path, names, files in os.walk(Descargas):
        for arch in files:
            nuevo_archivo = renombraPath(arch)
            if not (nuevo_archivo is None):
                os.rename(os.path.join(Descargas, arch), nuevo_archivo)
                print(nuevo_archivo)



mueveArchivos()
