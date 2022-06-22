# -*- coding: utf-8 -*-

from centros import *
from math import radians


# Función de lectura de datos del archivo .csv
datos=lee_centros('..\data\centrosSanitarios.csv')

# Funciones de salida

def test_lee_centros():
    print("Los 10 primeros datos del fichero son los siguientes:")
    print(datos[:10], "\n")
    
def test_num_total_camas_centros_accesibles():
    print("Hay {} camas disponibles en centros con acceso a gente discapacitada".format(num_total_camas_centros_accesibles(datos)))

def test_centros_con_uci_cercanos():
    punto = (36.657635572267445, -5.656869439190807)
    umbral = 0.2
    print("Hay {} centros con UCI, los más cercanos son: {} \n".format(len(centros_con_uci_cercanos(datos, punto, umbral)) ,centros_con_uci_cercanos(datos, punto, umbral)))

def test_distancia():
    sevilla = (37.3828300, -5.9731700)
    cadiz = (36.5008762, -6.2684345)
    print("La distancia entre Sevilla y Cádiz es: {} km".format(distancia(radians(sevilla[0]), radians(sevilla[1]), radians(cadiz[0]), radians(cadiz[1]))))

def test_media_coordenadas():
    centro = sacar_centros(datos)
    print("Las coordenadas medias de todos los centros de cadiz son: {}".format(media_coordenadas(centro)))
    
def test_generar_mapa():
    punto = (36.657635572267445, -5.656869439190807)
    umbral = 0.2
    #centros = centros_con_uci_cercanos(datos, punto, umbral) #sacar_centros(datos)
    centros = sacar_centros(datos)
    fichero = "..\out\mapa1.html"
    generar_mapa(centros, fichero)

# Test
    
#test_lee_centros()
#test_num_total_camas_centros_accesibles()
#test_centros_con_uci_cercanos()
#test_distancia()
#test_media_coordenadas()
test_generar_mapa() 