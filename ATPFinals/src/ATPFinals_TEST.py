# -*- coding: utf-8 -*-

from ATPFinals_SOLUCION import *

################################################################
#  Funciones de test
################################################################
def test_calcula_ganadores(registros):
    ganadores = calcula_ganadores(registros)
    print('Número de jugadores diferentes que han ganado un torneo:',
          len(ganadores))
    
def test_ganadores_tipo(registros):
    ganadores_GS = ganadores_tipo(registros, 'Grand Slam')
    print('\nGanadores de torneos del Grand Slam:', ganadores_GS)
    
def test_torneos_por_tipo(registros):
    torneos_tipo = torneos_por_tipo(registros)
    print('\nNúmero de torneos por tipo:')
    for tipo in torneos_tipo:
        print('   ' , tipo, '-', torneos_tipo[tipo])
        
def test_ganadores_por_superficie(registros):
    ganadores_superficie = ganadores_por_superficie(registros)
    print('\nGanadores por superficie:')
    for superficie in ganadores_superficie:
        print('   ' , superficie, '-', ganadores_superficie[superficie])
    
def test_ganador_mas_torneos_superficie(registros):
    ganador_superficie = ganador_mas_torneos_superficie(registros, 'Tierra')
    print('\nJugador que ha ganado más torneos en Tierra', ganador_superficie)

       
################################################################
#  Programa principal
################################################################
if __name__ == '__main__':
    print("\nEJERCICIO 1")
    registros = lee_finales('../data/ATPfinals2019.csv')
    print("Número total de finales:", len(registros)) 
    print(registros[:5], '\n')

    print("\nEJERCICIO 2")
    test_calcula_ganadores(registros)
    print("\nEJERCICIO 3")
    test_ganadores_tipo(registros)
    print("\nEJERCICIO 4")
    test_torneos_por_tipo(registros)
    print("\nEJERCICIO 5")
    test_ganadores_por_superficie(registros)
    print("\nEJERCICIO 6")
    test_ganador_mas_torneos_superficie(registros)
