# -*- coding: utf-8 -*-

import csv
from mapas import *
from math import sin, cos, sqrt, atan2, radians


'''
Funciones de apoyo
'''

def sacar_centros(datos):
    
    centros = [(nombre, localidad, latitud, longitud) for nombre, localidad, latitud, longitud,_,_,_,_ in datos]
    return centros


'''
Ejercicio 1
'''


def lee_centros(fichero):
    
    '''
Lee el fichero de entrada y devuelve una lista de tuplas de tipo CentroSanitario
ENTRADA:
 fichero: nombre del fichero de entrada -> str
SALIDA:
 lista de tuplas CentroSanitario(nombre,localidad, latitud, longitud, estado, num_camas,
acceso_minusvalidos, tiene_uci) -> [(str, str, float, float, str, int, bool, bool)]
Cada línea del fichero se corresponde con los datos de un centro sanitario y se representa con una tupla con
los siguientes valores:
 Nombre del centro sanitario
 Localidad en la que está situado el centro sanitario
 Latitud
 Longitud
 Estado
 Número de camas
 Es accesible
 Tiene UCI
    '''
    
    
    with open(fichero, encoding='utf-8') as f:
        lector = csv.reader(f, delimiter=';') # Usamos delimiter dado que por defecto es , no ; como en este caso.
        next(lector)
        
        datos = [(nombre, localidad, float(latitud), float(longitud), estado, int(num_camas), eval(tiene_acceso_discapacitados.strip(" ").capitalize()), eval(tiene_uci.strip(" ").capitalize())) for nombre, localidad, latitud, longitud, estado, num_camas, tiene_acceso_discapacitados, tiene_uci in lector]
        return datos
    
'''
Ejercicio 2
'''

def num_total_camas_centros_accesibles(datos):
    
    '''
Calcula el número total de camas de los centros que son accesibles para discapacitados.
ENTRADA:
 centros: lista de tuplas CentroSanitario(nombre,localidad, latitud, longitud, estado, num_camas,
acceso_minusvalidos, tiene_uci) -> [(str, str, float, float, str, int, bool, bool)]
SALIDA:
 total camas-> int
Toma como entrada una lista de tuplas CentroSanitario(nombre,localidad, latitud, longitud, estado,
num_camas, acceso_minusvalidos, tiene_uci) y produce como salida un entero correspondiente al número
total de camas de los centros accesibles para discapacitados.
    '''
    
    camas = [numeroCamas for _,_,_,_,_, numeroCamas, accesoDiscapacitados,_ in datos if accesoDiscapacitados == True]
    return sum(camas)

'''
Ejercicio 3
'''

def centros_con_uci_cercanos(centros, punto, umbral):
    
    '''
Selecciona los centros que están a una distancia menor o igual que un umbral del punto dado como parámetro
ENTRADA:
 centros: lista de tuplas CentroSanitario(nombre,localidad, latitud, longitud, estado, num_camas,
acceso_minusvalidos, tiene_uci) -> [(str, str, float, float, str, int, bool, bool)]
 punto: tupla con la latitud y logitud del punto -> (float, float)
 umbral: distancia mayor en la que deben estar los centros ->float
SALIDA:
 lista de tuplas-> (str, str, float, float)
Proyecto de laboratorio: Centros Sanitarios 3
Toma como entrada una lista de tuplas CentroSanitario(nombre,localidad, latitud, longitud, estado,
num_camas, acceso_minusvalidos, tiene_uci) y produce como salida una lista con el nombre del centro, la
localidad, la latitud y la longitud de los centros situados a una distancia menor o igual que el umbral del punto
dado como parámetro.    
    '''
    
    cercano = [(nombre, localidad, latitud, longitud) for nombre, localidad, latitud, longitud,_,_,_,_ in centros if (abs(latitud-punto[0]) <= umbral) and (abs(longitud-punto[1]) <= umbral)]
    return cercano

'''
Ejercicio 4
'''

def distancia(latitud1, longitud1, latitud2, longitud2):
    
    '''
ENTRADA:
 latitud1: latitud de un punto -> float
 longitud1: longitud de un punto -> float
 latitud2: latitud de un punto -> float
 longitud2: longitud de un punto -> float
SALIDA:
 distancia -> float
Toma como entrada la latitud y longitud de dos puntos y devuelve la distancia euclídea
    '''
    radio_tierra = 6373.0
    
    inc_lat  = latitud2 - latitud1
    inc_long = longitud2 - longitud1

    a = sin(inc_lat / 2)**2 + cos(latitud1) * cos(latitud2) * sin(inc_long / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    return radio_tierra * c

'''
Ejercicio 5
'''

def media_coordenadas(centros):
    
    '''
Calcula un punto cuya latitud es la media de las latitudes de los centros que se pasan como parámetro y cuya
longitud es la media de las longitudes de los centros.
ENTRADA:
 centros: lista de tuplas (nombre, localidad, latitud, longitud) => (str, str, float, float)
SALIDA:
 tupla (latitud, longitud) -> (float, float)
Toma como entrada una lista de tuplas (nombre, localidad, latitud, longitud) y devuelve una tupla
(media_latitud, media_longitud) con la media de las latitudes de los centros y la media de las longitudes
    '''
    
    coordenadas = [(latitud, longitud) for _,_, latitud,longitud in centros]
    
    latitud = []
    longitud = []
    
    for datos in coordenadas:
        latitud.append(datos[0])
        longitud.append(datos[1])
        
    latitud_media = (sum(latitud)/len(coordenadas))
    longitud_media = (sum(longitud)/len(coordenadas))
    
    media_coordenadas = (latitud_media, longitud_media)
    
    return media_coordenadas
        

'''
Ejercicio 6
'''

def generar_mapa(centros, fichero):
    
    '''
Genera un archivo html con un mapa en el que están geolocalizados los centros que se pasan como parámetro.
ENTRADA:
 centros: lista de tuplas (nombre, localidad, latitud, longitud) => (str, str, float, float)
 fichero: nombre del archivo html generado
Toma como entrada una lista de tuplas (nombre, localidad, latitud, longitud) y genera un archivo html con un
mapa y los iconos geolocalizados.
Para implementar la función generar_mapa ayúdese de las funciones auxiliares que se implementan
en el módulo mapas.py. Además, tenga en cuenta que:
1. Primero debe crear un mapa
2. Después debe ir creando marcadores y añadiéndolos al mapa. Use
marcador.add_to(mapa) para añadir un marcador al mapa.
3. Una vez añadidos todos los marcadores, guarde el mapa en el archivo html con
mapa.save(fichero).   
    '''
    
    
    coordenadas = media_coordenadas(centros)
    etiquetas = [(nombre, latitud, longitud) for nombre,_, latitud, longitud in centros]
   
    
    mapa = crea_mapa(coordenadas[0], coordenadas[1]) # Por defecto el zoom es 9
    
    
    for e in etiquetas:
        marcador = crea_marcador (e[1], e[2], e[0])
        marcador.add_to(mapa)
    
    return mapa.save(fichero)
    
    
####################################Francisco José Caballero##############################################    