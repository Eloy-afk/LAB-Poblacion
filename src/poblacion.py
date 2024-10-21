from collections import namedtuple
import csv
from datetime import datetime
import matplotlib.pyplot as plt

RegistroPoblacion = namedtuple('RegistroPoblacion', 'pais, codigo, año, censo')

def lee_poblaciones(ruta_fichero):
    poblacion=[]
    with open(ruta_fichero, encoding='utf-8') as f:
        lector=csv.reader(f)
        for pais, codigo, año, censo in lector:
            año=int(año)
            censo=int(censo)

            poblacion.append(RegistroPoblacion(pais, codigo, año, censo))
    return poblacion

def calcula_paises(poblaciones):
    paises={registro.pais for registro in poblaciones}
    return sorted(paises)

def filtra_por_pais(poblaciones, nombre_o_codigo):
    resultado=[
        (registro.año,registro.censo)
        for registro in poblaciones
        if registro.pais == nombre_o_codigo or registro.censo==nombre_o_codigo

    ]
    return resultado


def filtra_por_paises_y_anyo(poblaciones, anyo, paises):
    resultado=[
        (registro.pais,registro.censo)
        for registro in poblaciones
        if registro.año==anyo and registro.pais in paises

    ]

    return resultado


def muestra_evolucion_poblacion(poblaciones, nombre_o_codigo):
    registros_pais=filtra_por_pais(poblaciones, nombre_o_codigo)

    registros_pais.sort(key=lambda x: x[0])
    
    lista_años = [registro[0] for registro in registros_pais]
    lista_habitantes = [registro[1] for registro in registros_pais]
    
    titulo = f"Evolución de la población en {nombre_o_codigo}"
    
    plt.title(titulo)
    plt.plot(lista_años, lista_habitantes)
    plt.show()
    
    return registros_pais


def muestra_comparativa_paises_anyo(poblaciones, anyo, paises):
    registro_pais=filtra_por_paises_y_anyo(poblaciones, anyo, paises)
    registro_pais.sort(key=lambda x: x[0])

    lista_paises=[registro[0] for registro in registro_pais]
    lista_habitantes=[registro[1] for registro in registro_pais]
    
    titulo=f"Comparación de países en el año {anyo}"
    plt.title(titulo)
    plt.bar(lista_paises, lista_habitantes)
    plt.show()
    return registro_pais




