from poblacion2 import *

poblaciones=lee_poblaciones('data/population.csv')
paises=calcula_paises(poblaciones)
resultado1=filtra_por_paises_y_anyo(poblaciones, 2006, paises)
print(resultado1)