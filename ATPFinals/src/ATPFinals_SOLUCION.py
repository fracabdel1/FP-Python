# -*- coding: utf-8 -*-
''' Finales ATP 2018 

AUTOR: Mariano González
ÚLTIMA MODIFICACIÓN: 16/1/2020
'''

import csv
from collections import Counter
from collections import namedtuple

Final = namedtuple('Final', 'lugar, torneo, tipo, superficie, ganador, finalista') 
    
# EJERCICIO 1:
def lee_finales(fichero):
    registros = []
    with open(fichero, encoding='utf-8') as f:
        lector = csv.reader(f)
        next(lector)
        for lugar, torneo, tipo, superficie, ganador, finalista in lector:
            registros.append(Final(lugar, torneo, tipo,
                superficie, ganador, finalista))
    return registros

# EJERCICIO 2:
def calcula_ganadores(registros):
    ''' Calcula el conjunto de jugadores que han ganado algún torneo
    '''
    ganadores = {f.ganador for f in registros}
    return ganadores

# EJERCICIO 3:
def ganadores_tipo(registros, tipo):
    ''' Calcula los ganadores de todos los torneos de un tipo
    '''
    ganadores = [f.ganador for f in registros if f.tipo == tipo]
    return ganadores

# EJERCICIO 4:
def torneos_por_tipo(registros):
    ''' Crea un diccionario con el número de torneos de cada tipo
    '''
    # Con dict
    torneos = dict()
    for f in registros:
        if f.tipo in torneos:
            torneos[f.tipo] += 1
        else:
            torneos[f.tipo] = 1
    
    # Con Counter
    torneos = Counter([f.tipo for f in registros])
            
    return torneos

# EJERCICIO 5:
def ganadores_por_superficie(registros):
    ''' Crea un diccionario con los ganadores en cada superficie
    '''
    # Con dict
    ganadores = dict()
    for f in registros:
        if f.superficie in ganadores:
            ganadores[f.superficie].append(f.ganador)
        else:
            ganadores[f.superficie] = [f.ganador]
            
    return ganadores

# EJERCICIO 6:
def ganador_mas_torneos_superficie(registros, superficie):
    ''' Calcula el jugador que ha ganado más torneos de una superficie 
    '''
    # Con Counter
    ganadores = Counter(f.ganador for f in registros if f.superficie == superficie)
    ganador = max(ganadores.items(), key = lambda t:t[1])
    
    # También
    ganador = max(ganadores, key = ganadores.get)
    
    # También
    ganador = ganadores.most_common(1) # Solo aplicable al tipo Counter
        
    # Con el método anterior
    ganadores = ganadores_por_superficie(registros)[superficie]
    ganador = Counter(ganadores).most_common(1) 
    
    return ganador

'''
OTRAS FUNCIONES PROPUESTAS:
- Jugadores que han ganado torneos en todas las superficies
- Torneos de un tipo ganados por cada jugador
- Número de torneos ganados por cada jugador
- Jugador que ha ganado un torneo dado
- Jugador con mayor porcentaje de finales ganadas
'''
