#!/usr/bin/python3
import os
import sys

"""paths de las carpetas, si se tiene otra organizacion distinta cambiar los
que hagan falta"""
home = os.path.expanduser("~")

#Cambio de variables de ruta
#Comprobacion si .conf existe
if os.path.isfile(os.path.join(home,".orderUGR.conf"):
    f = open(os.path.join(home,".orderUGR.conf"), 'r')
    rutaDescargas = f.readline()
    rutaCursos = f.readline()
    f.close()
else:
    rutaDescargas = "Descargas"
    rutaCursos = "UGR"
                  
Descargas = os.path.join(home, rutaDescargas)
UGR = os.path.join(home, rutaCursos)

primero = os.path.join(UGR, "primero")
segundo = os.path.join(UGR, "segundo")
tercero = os.path.join(UGR, "tercero")
cuarto = os.path.join(UGR, "cuarto")

curso1 = [
    'CA', 'ALEM', 'FS', 'FP', 'FFT',
    'LMD', 'TOC', 'MP', 'ES', 'IES']

curso2 = [
    'SO', 'SCD', 'EC', 'ED', 'PDOO',
    'IA', 'FIS', 'AC', 'ALG', 'FBD']

curso3 = [
    'MC', 'IG', 'DDSI', 'FR', 'ISE', 'SWAP'
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
path_cursos = ['primero', 'segundo', 'tercero', 'cuarto']

def renombraArchivos(paraMover):
    nuevos = []
    for tupla in paraMover:
        tupla[1] = tupla[1].replace('-'+tupla[0], '')
        nuevos.append(tupla)
        #print(tupla)   debuggin
        
def busca_archivos():
    asig_arch = None
    paraMover = []
    for root, dirs, files in os.walk(Descargas):
        for curso in cursos:
            for asig in curso:
                for archivo in files:
                    if archivo.endswith(asig):
                        asig_arch = [asig, archivo, cursos.index(curso)]
                        #print(asig_arch)
                        paraMover.append(asig_arch)
    renombraArchivos(paraMover)
    return paraMover

def mueveArchivos(paraMover):
    for tupla in paraMover:
        curso = os.path.join(UGR, path_cursos[tupla[2]])
        directorio = os.path.join(curso, tupla[0])
        archivo_antiguo = os.path.join(Descargas, tupla[1]+'-'+tupla[0])
        nuevo = os.path.join(directorio, tupla[1])
        os.rename(archivo_antiguo, nuevo)
        print(nuevo)
       #Voy a escribir el log por si se pierde algo

tomove = busca_archivos()

#Crea archivo de configuracion con las rutas propias
if len(sys.argv) == 2: 
    if sys.argv[1] == '--configure':
        rutaCursos = input ("Ruta (sin /home/<user>/) donde quiere guardar los archivos ordenados: ")
        rutaDescargas = input ("Ruta (sin /home/<user>/) donde se descargan por defecto los archivos: ")
        f = open(os.path.join(home,".orderUGR.conf"), "w")
        f.write( rutaDescargas + "\n" )
        f.write( rutaCursos + "\n" )
        f.close()
    else:
        print ("El argumento introducido es erroneo. Pruebe con  --configure ")
        

if tomove is not []:
    print("No hay archivos que mover.")
else:
    mueveArchivos(tomove)
    print("Todo en su sito.")


