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
    'CA', 'ALEM', 'FS', 'FP', 'FFT',
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
path_cursos = ['primero', 'segundo', 'tercero', 'cuarto']

def renombraArchivos(paraMover):
    nuevos = []
    for tupla in paraMover:
        tupla[1] = tupla[1].replace('-'+tupla[0], '')
        nuevos.append(tupla)
        #print(tupla)

        
def busca_archivos():
    asig_arch = None
    paraMover = []
    for root, dirs, files in os.walk(Descargas):
        for curso in cursos:
            for asig in curso:
                for archivo in files:
                    if archivo.endswith(asig):
                        asig_arch = [asig, archivo, cursos.index(curso)]
                        print(asig_arch)
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
    
tomove = busca_archivos()
mueveArchivos(tomove)
