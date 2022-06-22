# -*- coding: utf-8 -*-
''' Análisis de frecuencias de nombres

AUTOR: José A. Troyano
REVISOR:  
ÚLTIMA MODIFICACIÓN: 26/05/2019

En este proyecto trabajaremos con datos correspondientes a los nombres de las
personas nacidas en España desde 2002 a 2017. Los datos están tomados del Instituto
Nacional de Estadística (https://www.ine.es/), donde se pueden encontrar muchos datos interesantes
principalmente sobre la demografía, economía, y sociedad españolas. Representaremos 
la información de entrada mediante listas de tuplas, y a partir de esta estructura implementaremos
una serie de funciones que nos permitirán realizar varios tipos de consultas y generar visualizaciones.

FORMATO DE ENTRADA:
-------------------
Trabajaremos con ficheros en formato CSV. Cada registro del fichero de entrada ocupa
una línea y contiene cuatro informaciones sobre los nombres (año, nombre, frecuencia, genero). 
Estas son las primeras líneas de un fichero de entrada:

    Año,Nombre,Frecuencia,Género
    2002,ALEJANDRO,8020,Hombre
    2002,PABLO,5799,Hombre
    2002,DANIEL,5603,Hombre
    2002,DAVID,5414,Hombre
    2002,ADRIAN,4949,Hombre
    2002,JAVIER,4909,Hombre
    2002,ALVARO,4595,Hombre
    2002,SERGIO,3744,Hombre

FUNCIONES A IMPLEMENTAR:
------------------------
- lee_registros(fichero):
    lee el fichero de registros y devuelve una lista de tuplas con nombre
- filtrar_por_genero(registros, genero):
    recibe una lista de tuplas y devuelve solo los registros del género recibido como parámetro
- calcular_nombres(registros, filtro=None):
    calcula el conjunto de nombres aplicando el filtro de género recibido como parámetro
- calcular_top_nombres_de_año(registros, año, limite=10, filtro=None):
    calcula los nombres más frecuentes de un año
- calcular_nombres_ambos_generos(registros):
    calcula el conjunto de nombres que han sido usados en ambos géneros
- calcular_nombres_compuestos(registros, filtro=None):
    calcula el conjunto de nombres con más de una palabra
- calcular_nombre_mas_frecuente_por_año(registros, filtro=None):
    calcula una lista de tuplas (año, nombre) con el nombre más frecuentes cada año
- calcular_frecuencia_por_año(registros, nombre):
    calcula una lista de tuplas (año, frecuencia) con las frecuencias de un nonmbre cada año
- mostrar_evolucion_por_año(registros, nombre):
    genera un gráfico con la evolución de la frecuencia de un nombre
- calcular_frecuencia_acumulada(registros, nombre):
    calcula la frecuencia acumulada de un nombre en todos los años
- calcular_frecuencias_por_nombre(registros):
    calcula un diccionario {nombre:frecuencia} con la frecuencia acumulada de cada nombre
- mostrar_frecuencias_nombres(registros, limite=10):
    genera un diagrama de barras con las frecuencias de los nombres más populares
'''

import csv
from collections import namedtuple
from matplotlib import pyplot as plt

# EJERCICIO 1:
Registro = namedtuple('Registro', 'año, nombre, frecuencia, genero')
def leer_frecuencias_nombres(fichero):
    ''' Lee el fichero de registros y devuelve una lista de tuplas con nombre
    
    ENTRADA: 
       - fichero: nombre del fichero de entrada -> str
    SALIDA: 
       - lista de registros (año, nombre, frecuencia, género) -> [Registro(int, str, int, str)]
    '''
    with open (fichero, encoding='utf-8') as f: #Abrimos el fichero como f
        lector=csv.reader(f)#leemos el fichero f y lo guardamos en lector
        next(lector) #Saltamos la cabecera
        registros=[(int(anyo), str(nombre), int(frecuencia), str(genero)) for anyo, nombre, frecuencia, genero in lector] #Creamos una lista de tuplas
        return registros #Retornamos los datos seleccionados
    


# EJERCICIO 2:
def filtrar_por_genero(registros, genero):
    ''' Recibe una lista de tuplas y devuelve solo los registros del género recibido como parámetro
    
    ENTRADA: 
       - registros: lista de registros (año, nombre, frecuencia, género) -> [Registro(int, str, int, str)]
       - genero: del que se seleccionarán los registros -> str
    SALIDA: 
       - lista de registros seleccionados -> [Registro(int, str, int, str)]
    '''
    
    filtradoGenero=[(int(anyo), str(nombre), int(frecuencia), str(genero1)) for anyo, nombre, frecuencia, genero1 in registros if genero1==genero]
    return filtradoGenero


# EJERCICIO 3:
def calcular_nombres(registros, filtro=None):
    ''' Calcula el conjunto de nombres aplicando el filtro de género recibido como parámetro 
    
    ENTRADA: 
       - registros: lista de registros (año, nombre, frecuencia, género) -> [Registro(int, str, int, str)]
       - filtro: 'Hombre', 'Mujer', o None si no se aplica filtro  -> str
    SALIDA: 
       - conjunto de nombres encontrados -> {str}
    '''
    
    nombres={nombres for anyo, nombres, frecuencias, genero in registros if genero==filtro or filtro==None}
    return nombres


# EJERCICIO 4:
def calcular_top_nombres_de_año(registros, año, limite=10, filtro=None):
    ''' Calcula los nombres más frecuentes de un año
    
    ENTRADA: 
       - registros: lista de registros (año, nombre, frecuencia, género) -> [Registro(int, str, int, str)]
       - año: del que se hace la consulta -> int
       - limite: número de nombres a recuperar -> int
       - filtro: 'Hombre', 'Mujer', o None si no se aplica filtro  -> str
    SALIDA: 
       - lista de tuplas (nombre, frecuencia) ordenanda de mayor a menor frecuencia  -> [(str, int)]
    '''
    
    nombresDelAño=[(nombre, frecuencia) for anyo, nombre, frecuencia, genero in registros if (genero==filtro or filtro==None) and (anyo==año)]
    
    #Ordenamos usando listas
    #nombresDelAño=sorted(nombresDelAño, reverse=True)
    #=[(nombre, frecuencia) for  frecuencia, nombre in nombresDelAño]
    #return nombresDelAñoOrdenados[:limite]
    
    #Ordenamos usando parametros de Sorted
    nombresDelAño=sorted(nombresDelAño, key=lambda t:t[1], reverse=True)
    return nombresDelAño[:10]
    
        
        
        

# EJERCICIO 5:
def calcular_nombres_ambos_generos(registros):
    ''' Calcula el conjunto de nombres que han sido usados en ambos géneros
    
    ENTRADA: 
       - registros: lista de registros (año, nombre, frecuencia, género) -> [Registro(int, str, int, str)]
    SALIDA: 
       - conjunto de nombres comunes a ambos géneros  -> {str}
    '''
    Hombres=[nombre for _, nombre, _, genero in registros if genero=="Hombre"]
    Mujeres=[nombre for _, nombre, _, genero in registros if genero=="Mujer"]
    
    Repetido=[nombre for _, nombre, _, _ in registros if (nombre in Hombres and nombre in Mujeres)]
    Repetido=set(Repetido)
    Repetido=list(Repetido)
    return Repetido

# EJERCICIO 6:
def calcular_nombres_compuestos(registros, filtro=None):
    ''' Calcula el conjunto de nombres con más de una palabra
    
    ENTRADA: 
       - registros: lista de registros (año, nombre, frecuencia, género) -> [Registro(int, str, int, str)]
       - filtro: 'Hombre', 'Mujer', o None si no se aplica filtro  -> str
    SALIDA: 
       - conjunto de nombres con más de una palabra  -> {str}
    '''
    
    nombresCompuestos=[nombre for _, nombre, _, _ in registros if " " in nombre]
    nombresCompuestos=set(nombresCompuestos)
    return nombresCompuestos


# EJERCICIO 7:
def calcular_nombre_mas_frecuente_por_año(registros, filtro=None):
    ''' Calcula una lista de tuplas (año, nombre) con el nombre más frecuentes cada año
    
    ENTRADA: 
       - registros: lista de registros (año, nombre, frecuencia, género) -> [Registro(int, str, int, str)]
       - filtro: 'Hombre', 'Mujer', o None si no se aplica filtro  -> str
    SALIDA: 
       - lista de tuplas (año, nombre, frecuencia) ordenanda por año  -> [(int, str, int)]
       
    Se calculará en primer lugar la lista de años y, posteriormente, se buscará el nombre
    más frecuente para cada año.
    '''
    #Creamos una lista con todos los años disponibles
    
    años=[anyo for anyo,_,_,_ in registros]
    años=set(años)
    años=list(años)
    
    #Creamos otra lista con los datos de salida que vamos a filtrar
    
    nombre = [(anyo, nombre, frecuencia) for anyo, nombre, frecuencia, genero in registros if genero==filtro or filtro==None]
    
    #filtramos los datos obtenidos para ver 
    
    nombreMasFrecuentePorAño = []
    
    for ano in años:
        frecuenciaMax = 0
        for datos in nombre:
            if datos[0]==ano and datos[2] > frecuenciaMax:
                frecuenciaMax = datos[2]
                almacen = datos
        nombreMasFrecuentePorAño.append(almacen)
    
    return sorted(nombreMasFrecuentePorAño)



# EJERCICIO 8:
def calcular_frecuencia_por_año(registros, nombre):
    ''' Calcula una lista de tuplas (año, frecuencia) con las frecuencias de un nonmbre cada año
    
    ENTRADA: 
       - registros: lista de registros (año, nombre, frecuencia, género) -> [Registro(int, str, int, str)]
       - nombre: del que se hace la consulta  -> str
    SALIDA: 
       - lista de tuplas (año, frecuencia) ordenanda por año  -> [(int, int)]
       
    En el caso de que un nombre se use para hombres y mujeres, se sumarán ambas frecuencias
    '''
    Hombres=[(anyo,nombre,frecuencia) for anyo, nombre, frecuencia, genero in registros if genero=="Hombre"]
    Mujeres=[(anyo, nombre,frecuencia) for anyo, nombre, frecuencia, genero in registros if genero=="Mujer"]
    
    for datos in registros:
        if datos[1]==nombre and nombre in Hombres and nombre in Mujeres:
            frecuenciaHombres=[frecuencia for anyo, nombreReg, frecuencia in Hombres if anyo==datos[0] and nombreReg==nombre]
            frecuenciaMujeres=[frecuencia for anyo, nombreReg, frecuencia in Mujeres if anyo==datos[0] and nombreReg==nombre]
            frecuencias=[(datos[0], frecuenciaHombres[0]+frecuenciaMujeres[0])]
        else:
            frecuencias = [(anyo, frecuencia) for anyo, nombreReg, frecuencia, _ in registros if nombreReg==nombre]
        
    return frecuencias
    

# EJERCICIO 9:
def mostrar_evolucion_por_año(registros, nombre):
    ''' Genera un gráfico con la evolución de la frecuencia de un nombre
    
    ENTRADA: 
       - registros: lista de registros (año, nombre, frecuencia, género) -> [Registro(int, str, int, str)]
       - nombre: del que se hace la consulta  -> str
    SALIDA EN PANTALLA: 
       - curva con la evolución de la frecuencia del nombre
    
    Se usarán las siguientes instrucciones para generar la gráfica:
        plt.plot(años, frecuencias)
        plt.title("Evolución del nombre '{}'".format(nombre))
        plt.show()
    Donde 'años' y 'frecuencias' se extraen del resultado de la función
    'calcular_frecuencia_por_año'
    '''
    años=[]
    frecuencias=[]
    
    datos=calcular_frecuencia_por_año(registros, nombre)
    for datos in datos:
        años.append(datos[0])
        frecuencias.append(datos[1])
    '''
    plt.title("Comparativa de paises")
    indice = range(len(años))
    plt.bar(indice, frecuencias)
    plt.xticks(indice, años, fontsize=8)
    plt.show()
    '''
    
    plt.title("Evolución del nombre '{}'".format(nombre))
    plt.plot(años, frecuencias)
    plt.show()
# EJERCICIO 10:
def calcular_frecuencia_acumulada(registros, nombre):
    ''' Calcula la frecuencia acumulada de un nombre en todos los años
    
    ENTRADA: 
       - registros: lista de registros (año, nombre, frecuencia, género) -> [Registro(int, str, int, str)]
       - nombre: del que se hace la consulta  -> str
    SALIDA: 
       - suma de las frecuencias del nombre en todos los años  -> int
    '''
    suma=0
    frecuencias=[frecuencia for _, nombreReg, frecuencia, _ in registros if nombreReg == nombre]
    for frecuencia in frecuencias:
        suma+=frecuencia
    return suma


# EJERCICIO 11:
def calcular_frecuencias_por_nombre(registros):
    ''' Calcula un diccionario {nombre:frecuencia} con la frecuencia acumulada de cada nombre
    
    ENTRADA: 
       - registros: lista de registros (año, nombre, frecuencia, género) -> [Registro(int, str, int, str)]
    SALIDA: 
       - diccionario con la frecuencia acumulada de cada nombre -> {str:int}
    '''
    diccionario = {}
    
    for datos in registros:
        frecuenciaAcumulada=calcular_frecuencia_acumulada(registros, datos[1])
        nombre=datos[1]
        diccionario[nombre]=frecuenciaAcumulada
    return diccionario


# EJERCICIO 12:
def mostrar_frecuencias_nombres(registros, limite=10):
    ''' Genera un diagrama de barras con las frecuencias de los nombres más populares
    
    ENTRADA: 
       - registros: lista de registros (año, nombre, frecuencia, género) -> [Registro(int, str, int, str)]
       - limite: número de nombres a mostrar -> int
    SALIDA EN PANTALLA: 
       - diagrama de barras con las frecuencias de los nombres más populares
    
    Se usarán las siguientes instrucciones para generar la gráfica:
        plt.bar(nombres, frecuencias)
        plt.xticks(rotation=80)
        plt.title("Frecuencia de los {} nombres más comunes".format(limite))
        plt.show()
        
    Donde 'años' y 'frecuencias' se extaren del resultado de la función
    'calcular_frecuencias_por_nombre'
    '''
    nombres=[nombres for _,nombres,_,_ in registros]
    nombres=nombres[:limite]
    frecuencias=[]
    diccionario=calcular_frecuencias_por_nombre(registros)

    for nombre in nombres:
        frecuencias.append(diccionario[nombre])

    
    plt.bar(nombres, frecuencias)
    plt.xticks(rotation=80)
    plt.title("Frecuencia de los {} nombres más comunes".format(limite))
    plt.show()
    
 
###############################################################################################

########################### Francisco José Caballero del Campo ################################