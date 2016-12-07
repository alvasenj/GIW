# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 22:01:22 2016

@author: Alberto Marquez Gómez
@author: Álvaro Asenjo Torrico	
@author: Juan José Montiel Cano

"""

import urllib, os
from BeautifulSoup import *

html = urllib.urlopen('http://trenesytiempos.blogspot.com.es/').read() #Abrimos la página web para encontrar las entradas del blog
sopa = BeautifulSoup(html)
etiquetas=sopa.findAll('a',attrs={"class":"post-count-link"}, limit=46)#Identificamos las entradas del blog mediante la etiqueta <a> y el atributo post-count-link
                                                                        #limit 46 porque sólo queremos las del 2016
d=1
for i in etiquetas:
    if(d>1):
        print i
        etiqueta = i.get('href')#Extraemos la url de cada entrada
        html2=urllib.urlopen(etiqueta).read() #Leemos la página
        soup = BeautifulSoup(html2) 
        etiquetasImagen=soup('a',{"imageanchor":"1"}) #Identificamos las imágenes con etiqueta <a> y atributo imageanchor=1
        j=0 
        os.mkdir(str(d))#Creamos el directorio para cada entrada
        #Leemos las imágenes de dicha entrada y las guardamos en un .jpg
        for k in etiquetasImagen:
            archivo=open(str(d)+"/foto"+str(j)+".jpg","wb")
            imagen=urllib.urlopen(k.get('href',None))
            while True:
                info = imagen.read(100000)
                if len(info) < 1 : break
                archivo.write(info)
            archivo.close()
            j=j+1
    d=d+1
        
       





