from collections import namedtuple
import csv
import matplotlib.pyplot as plt

RegistroPoblacion = namedtuple('RegistroPoblacion', 'pais, codigo, año, censo')
def lee_poblaciones(ruta):
    poblacion=[]
    with open (ruta, encoding='utf-8') as f:
        lector=csv.reader(f)
        for pais, codigo, año, censo in lector:
            año=int(año)
            censo=int(censo)

            poblacion.append(RegistroPoblacion(pais, codigo, año, censo))
    return poblacion

def calcula_paises(poblaciones):
    paises={registro.pais for registro in poblaciones}
    return paises


def filtra_por_pais(poblaciones, nombre_o_codigo):
    resultado=[(registro.pais, registro.censo) for registro in poblaciones if registro.año == nombre_o_codigo or registro.censo==nombre_o_codigo]
    return sorted(resultado)


def filtra_por_paises_y_anyo(poblaciones, anyo, paises):
    resultado=[(registro.pais, registro.censo) for registro in poblaciones if registro.año == anyo and registro.pais in paises]
    return resultado



