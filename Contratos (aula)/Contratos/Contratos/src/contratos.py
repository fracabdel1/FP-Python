# -*- coding: utf-8 -*-
''' Examen de diciembre 2018/19 de Fundamentos de Programación (Python)

AUTOR: Mariano González
REVISORES: Carlos García, Fermín Cruz, Toñi Reina
ÚLTIMA MODIFICACIÓN: 7/ene/2020

En este ejercicio trabajaremos sobre un dataset con información
sobre contratos de trabajo. 

Los datos se encuentran almacenados en un fichero en formato CSV.
Estas son las primeras líneas del fichero de entrada (fíjese en que
la primera línea es una cabecera con los nombres de las columnas):

    numSS,fecha,codigo,dias,horas,sueldo
    41347712,01/03/2014,77232,239,6,20.8
    75402883,28/07/2014,77232,363,4,24.5
    62583432,15/07/2014,12271,214,4,29.1
    62583432,16/04/2015,50323,324,5,15.7
    ...
            
Donde:
    NumSS: número de la Seguridad Social del trabajador.
    Fecha: fecha del contrato.
    Código: código identificativo del campo de actividad del contrato.
    Día: número de días del contrato.
    Horas: número de horas de trabajo al día.
    Sueldo: sueldo bruto por hora.

En el fichero pueden existir distintos contratos para el mismo trabajador.
    
Implemente las funciones con los comentarios EJERCICIO Nº,
eliminando previamente la instrucción pass.
'''

import csv
from datetime import datetime
from matplotlib import pylab as plt
from collections import namedtuple
from collections import Counter

Contrato = namedtuple("Contrato", "numSS, fecha, codigo, dias, hora, sueldo")

# EJERCICIO 1:
def lee_contratos(fichero):
    ''' Lee el fichero de entrada y devuelve una lista de tuplas.
    
        Cada línea del fichero de entrada contiene seis datos:
            NumSS: número de la Seguridad Social del trabajador.
            Fecha: fecha del contrato.
            Código: código identificativo del campo de actividad del contrato.
            Día: número de días del contrato.
            Hora: número de horas de trabajo al día.
            Sueldo: sueldo bruto por hora.
            
        Hay que transformar ciertos elementos de la entrada en valores numéricos
        o de tipo fecha para que puedan ser procesados posteriormente.
        
        Para convertir una cadena de texto del estilo de '30/10/2007'
        en una fecha, utilice esta función: 
        fecha = datetime.strptime(fecha_en_cadena, '%d/%m/%Y').date()
        
    '''
    
    with open(fichero, encoding = 'utf-8') as f:
        lector = csv.reader(f)
        next(lector)
        
        contratos = [(Contrato(numSS, datetime.strptime(fecha, '%d/%m/%Y').date(), codigo, int(dia), int(hora), float(sueldo))) for numSS, fecha, codigo, dia, hora, sueldo in lector]
        
        return contratos
    
# EJERCICIO 2
def trabajadores_contratados_actividad(contratos, codigo):
    ''' Recibe una lista de tuplas con la información sobre los contratos y
    el código de una actividad y devuelve un conjunto con los números de la
    Seguridad Social de los trabajadores con contrato en dicha actividad.
    '''
    conjunto = set()
    
    for e in contratos:
        if e.codigo == codigo:
            conjunto.add(e.numSS)
            
    return conjunto

# EJERCICIO 3
def dias_contrato_trabajador(contratos, numeroSS):
    ''' Recibe una lista de tuplas con la información sobre los contratos y
    el número de la Seguridad Social de un trabajador y devuelve el total de
    días de trabajo acumulados por los contratos del trabajador.
    '''
    
    numero_dias = []
    
    for e in contratos:
        if e.numSS == numeroSS:
            numero_dias.append(e.dias)
            
    return sum(numero_dias)
                
# EJERCICIO 4
def trabajador_mas_dias(contratos):
    ''' Recibe una lista de tuplas con la información sobre los contratos,
    y busca el trabajador que acumula más días de contrato. Devuelve una tupla formada por
    el número de días totales y el número de la Seguridad Social del trabajador.
    En caso de empate a número de días, devuelve uno cualquiera de ellos.
    '''
    
    diccionario = dict()
    
    for e in contratos:
        if e.numSS in diccionario:
            diccionario[e.numSS] += e.dias
        else:
            diccionario[e.numSS] = e.dias
            
    tupla = sorted(diccionario.items(), reverse = True, key = lambda t:t[1])
    return tupla[:1]
    
# EJERCICIO 5
def indexa_contratos_por_actividad(contratos):
    ''' Recibe una lista de tuplas con la información sobre los contratos,
    y devuelve un diccionario en el que las claves son los códigos de actividad
    y los valores asociados son listas con las tuplas correspondientes a
    la información sobre los 3 contratos con mayor duración en días de cada actividad. 
    
    Las listas asociadas a los códigos de actividad deben estar ordenadas
    de mayor a menor duración en días.    
    '''    
    '''
    diccionario = dict()
    
    for e in contratos:
        if e.codigo in diccionario:
            diccionario[e.codigo].append(e) 
        else:
            diccionario[e.codigo] = [e]
    
    tuplas = sorted(diccionario.items(), reverse = True, key = lambda t:t[1][3])
    return tuplas
    '''
    
    diccionario = dict()
    
    codigos = [e.codigo for e in contratos]
    codigos = set(codigos)
    codigos = list(codigos)

    for codigo in codigos:
        lista = []
        for e in contratos:
            if codigo == e.codigo:
                lista.append(e)
        lista = sorted(lista, reverse = True, key = lambda t:t[3])
        lista = lista[:3]
        diccionario[codigo] = lista
        
    return diccionario

# EJERCICIO 6
def muestra_evolucion_contratos(contratos, codigo):
    ''' Recibe una lista de tuplas con la información sobre los contratos y
    el código de una actividad. Muestra una gráfica con la evolución a lo largo
    de los años del número de contratos de la actividad en cuestión.
    
    Para mostrar la gráfica use el siguiente código:
    
        plt.title("Número de contratos por año de la actividad " + codigo)
        plt.bar(range(len(numero_contratos)), numero_contratos, tick_label=anyos)
        plt.show()
    
    Debe calcular previamente las siguientes listas:
    
    - anyos: lista ordenada con los años DEL PERIODO COMPLETO para el que hay datos
    en la lista de contratos, ordenados crecientemente. Cada año debe aparecer una sola vez.
    Para obtener el año de una fecha f, utilice la expresión f.year
    - numero_contratos: lista con el número de contratos de la actividad dada
    en cada uno de los años de la lista anterior.
    '''
    
    pass
    