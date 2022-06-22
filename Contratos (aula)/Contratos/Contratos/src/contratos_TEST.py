# -*- coding: utf-8 -*-
'''
Created on 2 ene. 2020

@author: mariano
'''

from contratos import *

def test_trabajadores_contratados_actividad(fichero, codigo):
    trabajadores = trabajadores_contratados_actividad(fichero, codigo)
    return trabajadores

def test_dias_contrato_trabajador(contratos, numeroSS):
    dias_trabajados = dias_contrato_trabajador(contratos, numeroSS)
    return dias_trabajados

################################################################
#  Programa principal
################################################################
if __name__ == '__main__':
    
    print('EJERCICIO 1:')
    
    fichero = lee_contratos('../data/contratos.csv')
    print('Hay {} trabajadores siendo los 10 primeros: {}.'.format(len(fichero),fichero[:10]))
    
    print('EJERCICIO 2:')
    
    codigo = '77232'
    trabajadores = test_trabajadores_contratados_actividad(fichero, codigo)
    print('Los trabajadores para la actividad {} son: {}' .format(codigo, trabajadores))
    
    print('EJERCICIO 3:')
    
    numeroSS = '27634587'
    dias_trabajados = test_dias_contrato_trabajador(fichero, numeroSS)
    print('El número total de dias trabajados de {} es de {} días.' .format(numeroSS, dias_trabajados))
    
    print('EJERCICIO 4:')
    
    tupla = trabajador_mas_dias(fichero)
    numSS = tupla [0][0]
    dias = tupla [0][1]
    print('El trabajador con más días de contrato es {} con un total de {} días' .format(numSS, dias))
    
    print('EJERCICIO 5:')
    
    codigo = '77232'
    resultado = indexa_contratos_por_actividad(fichero)
    contratos = resultado[codigo]
    print('Los contratos de la actividad {} con mayor duración son: {}' .format(codigo, contratos))
    
    print('EJERCICIO 6:')

