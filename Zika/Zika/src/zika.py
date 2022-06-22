# -*- coding: utf-8 -*-
'''
Created on 17 oct. 2018

@author: mateosg, reinaqu

En este ejercicio trabajaremos sobre un fichero en formato CSV que tiene
información sobre el virus del zika.
A continuación se muestran las primeras cinco líneas de dicho fichero.
Fíjese que la primera línea es la cabecera con los datos de las columnas:

    report_date,location,location_type,data_field,data_field_code,value,unit
    02/07/2016,Brazil-Pernambuco,state,microcephaly_not,BR0003,1173,cases
    02/07/2016,Brazil-Bahia,state,microcephaly_under_investigation,BR0001,659,cases
    02/07/2016,Brazil-Pernambuco,state,microcephaly_under_investigation,BR0001,489,cases
    02/07/2016,Brazil-Paraiba,state,microcephaly_not,BR0003,479,cases

Cada línea describe la acción del virus zika sobre una zona, de forma que los
datos de izquierda a derecha se corresponden con la fecha de detección,
la localización, el tipo de división territorial (estado, país...),
la sintomatología detectada, el código asignado al reporte, el número de
casos o de municipios afectados, y el dominio del valor anterior o unidades 
(casos o municipios).

Para la conversión de texto a fecha, puede ayudarse de la siguiente expresión:
    datetime.strptime(fecha_string, '%d/%m/%Y').date()

Siga las instrucciones e implemente las funciones que aparecen a continuación.

'''
import csv
from datetime import datetime, date
from matplotlib import pylab as plt
from collections import namedtuple

ZikaReport = namedtuple('ZikaReport',
        'fecha,location,location_type,data_field,data_field_code,value,unit')

# EJERCICIO 1
def lee_fichero(fichero):
    '''
    Lee el fichero de entrada y lo almacena en una lista de namedtuple de
    tipo ZikaReport(report_date,location,location_type,data_field,
    data_field_code,value,unit)
    Entrada:
      -fichero: nombre con ruta del fichero con los datos -> str
    Salida:
      -Lista de tuplas de tipo ZikaReport con los datos del fichero
       -> [ZikaReport(...)]
    '''
 
    with open (fichero, encoding = 'utf-8') as f:
        lector = csv.reader(f)
        next(lector)
        
        zika = [(ZikaReport((datetime.strptime(fecha, '%d/%m/%Y').date()), location, location_type, data_field, data_field_code, int(value), unit)) for fecha,location,location_type,data_field,data_field_code,value,unit in lector]
        return zika

    
#EJERCICIO 2
def num_casos_entre(reports, fecha_inicial, fecha_final):
    '''
    Devuelve el total de casos detectados entre las fechas especificadas
    por el intervalo (fecha_inicial, fecha_final) ambas incluídas,
    y que tengan el valor 'cases' en el campo unit. 
    Nótese que el campo 'unit' hace referencia al dominio y puede tomar
    como valores 'cases' y 'municipalities' (casos y municipios respectivamente).
    
    Entrada:
     - reports: lista de tuplas con los informes del virus del Zika
       -> [ZikaReport(...)]
     - fecha_inicial: Fecha inicial del intervalo de fechas buscadas -> date
     - fecha_final: Fecha final del intervalo de fechas buscasdas -> date
    Salida:
     - Número total de casos de Zika detectado en el intervalo de fechas
       dado por (fecha_inicial, fecha_final), ambos inclusive,
       y cuya unidad es de tipo 'cases'. -> int
    '''
    '''
    contador = 0
    
    for e in reports:
        if e.unit == 'cases' and fecha_inicial <= e.fecha and fecha_final >= e.fecha:
            contador += e.value
    return contador       
    
    '''
    casos = [e.value for e in reports if fecha_inicial <= e.fecha and fecha_final >= e.fecha and e.unit == 'cases']
    return sum(casos)

# EJERCICIO 3  
def casos_zika_territorio_USA(reports):
    '''
    Devuelve una lista con las localizaciones y el número de casos del virus
    Zika en el territorio de Estados Unidos. Note que el tipo de localización
    debe ser 'territory', las unidades 'cases' y la localización debe contener
    'United_States'
    Entrada:
     - reports: lista de tuplas con los informes del virus del Zika
       -> [ZikaReport(...)]
    Salida:
    - Lista de tuplas (location, valor) con el número de casos de virus zika
      en los territorios de Estados Unidos -> [(str, int)]
    ''' 
    '''
    lista = list()
    
    for e in reports:
        if e.location_type == 'territory' and 'United_States' in e.location and e.unit == 'cases':
            tupla = (e.location, e.value)
            lista.append(tupla)
    return lista
    '''       
    
    tupla = [(e.location, e.value) for e in reports if 'United_States' in e.location and e.location_type == 'territory' and e.unit == 'cases']
    return tupla
    
# EJERCICIO 4  
def filtra_por_estado(reports, anyo):
    '''
    Devuelve una lista ordenada por fecha, con tuplas distintas de la forma
    (fecha,localización) de aquellos informes cuyo tipo de localización
    sea 'state', y cuyos casos tuvieron lugar en el año que se pasa como
    parámetro de entrada. Note que en la lista resultado no 
    puede haber tuplas duplicadas.
    Entrada:
     - reports: lista de tuplas con los informes del virus del Zika
       -> [ZikaReport(...)]
     - anyo: Año de los informes buscados -> int
    Salida:
     - lista de tuplas (fecha, localización) ordenada por fecha y con
       la fecha y la localización de los informes del año dado como
       parámetro y cuyo tipo de localización es 'state' -> [(date,str)]
    '''
    '''
    lista = list()
    conjunto = set()
    
    for e in reports:
        if e.location_type == 'state' and anyo == e.fecha.year:
            tupla = (e.fecha, e.location)
            conjunto.add(tupla)
    lista = list(conjunto)
    return sorted(lista)
    '''
    casos = [(e.fecha, e.location) for e in reports if anyo == e.fecha.year and e.location_type == 'state']
    casos = set(casos)
    casos = list(casos)
    return sorted(casos)
    
# EJERCICIO 5 
def anyo_mas_casos(reports):
    '''
    Devuelve el año en el que se han producido más casos de Zika en forma
    de tupla (total_casos,año)
    Entrada:
     - reports: lista de tuplas con los informes del virus del Zika
       -> [ZikaReport(...)]
    Salida:
     - Una tupla de la forma (total_casos, año) con el número total de casos
       del año y el año con más casos -> (int, int)
    '''
    '''
    dicc = dict()
    lista = list()
    
    for e in reports:
        if e.fecha.year in dicc:
            dicc[e.fecha.year] += e.value
        else:
            dicc[e.fecha.year] = e.value
            
    lista = dicc.items()
    valor_tupla = sorted(lista, reverse = True, key=lambda t:t[1])
    return valor_tupla
    '''
    dicc = dict()
    
    for e in reports:
        if e.unit == 'cases':
            if e.fecha.year in dicc:
                dicc[e.fecha.year] += e.value
            else:
                dicc[e.fecha.year] = e.value
    
    tupla = [(int(casos), int(fecha)) for fecha, casos in dicc.items()]
    return max(tupla)
    
# EJERCICIO 6   
def porcentaje_por_descrip(reports):
    '''
    Devuelve un diccionario en el que las claves son la descripción del
    informe ('data_field'), y los valores, el porcentaje de informes con
    esa descripción respecto al número total de informes.
    Entrada:
     - reports: lista de tuplas con los informes del virus del Zika
       -> [ZikaReport(...)]
    Salida:
     - Un diccionario {descripcion:porcentaje} en el que las claves son
       la descripción de la sintomatología y los valores son el porcentaje
       de informes con respecto al número total de informes que tienen
       esa descripción {str:float}
    '''
    
    dicc = dict()
    
    dolencias = [e.data_field for e in reports]
    numero_dolencias = len(dolencias)
    dolencias = set(dolencias)
    
    for dol in dolencias:
        contador = 0
        for a in reports:
            if a.data_field == dol:
                contador += 1
        porcent = (contador / numero_dolencias) * 100
        dicc[dol] = porcent
    
    return dicc

# EJERCICIO 7 
def dibuja_casos_zika_por_pais(reports):
    '''
    Muestra una gráfica de barras con el número de casos acumulados por país.
    El total de casos de un país se calcula acumulando el valor del campo 'value'
    de los reportes del país con unidad 'cases' y tipo de localización 'country'.
    Tenga en cuenta que los Estados Unidos son una excepción a esta regla,
    ya que el número de casos de este país se debe calcular como la suma
    de los casos del territorio USA (al no haber informes que acumulen la
    totalidad del país, sino que la información está desglosada por territorio).
    
    Se usarán las siguientes instrucciones para generar el diagrama de barras:
    
    fig = plt.figure(titulo)
    ax = fig.add_subplot(111) 
    n_x = range(len(paises))
    ax.bar(n_x, num_casos, width=0.8, align='center')
    ax.set_xticks(n_x)
    ax.set_xticklabels(paises,rotation='vertical')
    
    en las que titulo es una cadena con el título que aparecerá en la barra
    superior de la ventana en la que se muestra el gráfico, paises es una
    lista ordenada con el nombre de los países, y num_casos es una lista
    con el número de casos asociados a cada país.   
    Entrada:
     - reports: lista de tuplas con los informes del virus del Zika
       -> [ZikaReport(...)]    
    '''
    pass