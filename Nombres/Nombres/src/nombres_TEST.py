# -*- coding: utf-8 -*-

from nombres import *

################################################################
#  Funciones de test
################################################################
def test_filtrar_por_genero(registros):
    print("TEST de 'filtrar_por_genero'")
    print("   - Número de registros para '{}': {}".format('Hombre', len(filtrar_por_genero(registros, 'Hombre'))))
    print("   - Número de registros para '{}': {}\n".format('Mujer', len(filtrar_por_genero(registros, 'Mujer'))))


def test_calcular_nombres(registros):
    print("TEST de 'calcular_nombres'")
    print("   - Ambos géneros: {}".format(sorted(list(calcular_nombres(registros)))[:10]))
    print("   - Hombres: {}".format(sorted(list(calcular_nombres(registros, 'Hombre')))[:10]))
    print("   - Mujeres: {}\n".format(sorted(list(calcular_nombres(registros, 'Mujer')))[:10]))


def test_calcular_top_nombres_de_año(registros):
    año = 2008
    print("TEST de 'calcular_top_nombres_de_año' para {}".format(año))
    print("   - Ambos géneros: {}".format(calcular_top_nombres_de_año(registros, año)))
    print("   - Hombres: {}".format(calcular_top_nombres_de_año(registros, año, filtro='Hombre')))
    print("   - Mujeres: {}\n".format(calcular_top_nombres_de_año(registros, año, filtro='Mujer')))
    

def test_calcular_nombres_ambos_generos(registros):
    print("TEST de 'calcular_nombres_ambos_generos'")
    print("   - Nombres: {}\n".format(calcular_nombres_ambos_generos(registros)))


def test_calcular_nombres_compuestos(registros):
    print("TEST de 'calcular_nombres_compuestos'")
    print("   - Ambos géneros: {}".format(sorted(list(calcular_nombres_compuestos(registros)))))
    print("   - Hombres: {}".format(sorted(list(calcular_nombres_compuestos(registros, filtro='Hombre')))))
    print("   - Mujeres: {}\n".format(sorted(list(calcular_nombres_compuestos(registros, filtro='Mujer')))))
    

def test_calcular_nombre_mas_frecuente_por_año(registros):
    print("TEST de 'calcular_nombre_mas_frecuente_por_año'")
    print("   - Ambos géneros: {}".format(calcular_nombre_mas_frecuente_por_año(registros)))
    print("   - Hombres: {}".format(calcular_nombre_mas_frecuente_por_año(registros, filtro='Hombre')))
    print("   - Mujeres: {}\n".format(calcular_nombre_mas_frecuente_por_año(registros, filtro='Mujer')))


def test_calcular_frecuencia_por_año(registros):
    print("TEST de 'calcular_frecuencia_por_año'")
    nombre = 'ABRIL'
    print("   - {}: {}\n".format(nombre, calcular_frecuencia_por_año(registros, nombre)))


def test_mostrar_evolucion_por_año(registros):
    print("TEST de 'mostrar_evolucion_por_año'")
    nombre = 'IKER'
    mostrar_evolucion_por_año(registros, nombre)
    print()

def test_calcular_frecuencia_acumulada(registros):
    print("TEST de 'calcular_frecuencia_acumulada'")
    nombre = 'IKER'
    print("   - {}: {}\n".format(nombre, calcular_frecuencia_acumulada(registros, nombre)))


def test_calcular_frecuencias_por_nombre(registros):
    print("TEST de 'calcular_frecuencias_por_nombre'")
    print("   - Frecuencias: {}\n".format(calcular_frecuencias_por_nombre(registros)))


def test_mostrar_frecuencias_nombres(registros):
    print("TEST de 'mostrar_frecuencias_nombres'")
    mostrar_frecuencias_nombres(registros, 20)
    print()
    
    
################################################################
#  Programa principal
################################################################

registros = leer_frecuencias_nombres('../data/frecuencias_nombres.csv')
#print(registros[:10], "\n")

#test_filtrar_por_genero(registros)
#test_calcular_nombres(registros)
#test_calcular_top_nombres_de_año(registros)
#test_calcular_nombres_ambos_generos(registros)
#test_calcular_nombres_compuestos(registros)
#test_calcular_nombre_mas_frecuente_por_año(registros)
#test_calcular_frecuencia_por_año(registros)
#test_mostrar_evolucion_por_año(registros)
#test_calcular_frecuencia_acumulada(registros)
test_calcular_frecuencias_por_nombre(registros)
#test_mostrar_frecuencias_nombres(registros)
