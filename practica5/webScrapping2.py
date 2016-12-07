# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 23:13:40 2016

@author: Alberto Marquez Gómez
@author: Álvaro Asenjo Torrico	
@author: Juan José Montiel Cano

"""

import urllib, re
from BeautifulSoup import *

d=0
cont=0

cadena = raw_input("Buscar: ")#Solicitamos al usuario la cadena para la búsqueda
html = urllib.urlopen('http://trenesytiempos.blogspot.com.es/').read()#Abrimos la página web para encontrar las entradas del blog
sopa = BeautifulSoup(html)
etiquetas=sopa.findAll('a',attrs={"class":"post-count-link"})#Identificamos las entradas del blog mediante la etiqueta <a> y el atributo post-count-link

print "Resultados para su búsqueda: "
for i in etiquetas:
    if d>1:
        etiqueta = i.get('href') #Extraemos la url de cada entrada
        html2=urllib.urlopen(etiqueta).read() #Leemos la página
        texto = re.findall(cadena, html2) #Buscamos la cadena solicitada por el usuario
        for j in texto:
            if j != "":
                cont+=1
                print etiqueta
                break
    d+=1
if cont == 0:
    print "No se han encontrado resultados para la búsqueda ",cadena


    