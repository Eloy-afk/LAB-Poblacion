import poblacion

poblaciones= poblacion.lee_poblaciones('data/population.csv')



paises_totales=poblacion.calcula_paises(poblaciones)
paises_random =['Argentina','Arab World', 'Spain', 'Zimbabwe', 'Chile', 'Puerto Rico']


resultados = poblacion.filtra_por_paises_y_anyo(poblaciones, 2006, paises_totales)
print(resultados)

print(poblacion.muestra_evolucion_poblacion(poblaciones, 'Argentina'))
print(poblacion.muestra_comparativa_paises_anyo(poblaciones, 2006, paises_random))