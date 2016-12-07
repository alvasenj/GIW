#!/usr/bin/env python
# -*- coding: utf-8 -*-

from xml.dom.minidom import parse
import xml.dom.minidom
import urllib

'''
cortamos los datos recibidos por la url, primero por el tag <h3>Descripción</h3>
y luego por el tag <h3>Enlaces</h3>
esto nos dejará solo la descripcion
'''
def cortaDescripcion(texto):
    #print str(texto.decode('utf-8'));
    source = "<h3>Descripci";
    #source2 = source.decode('utf-8');
    corte1 = texto.split(source);
    corte2 = corte1[1].split("<h3>Enlaces</h3>");
    return corte2[0][7:];

'''
buscara el monumento en google maps y sacará su latitud y longitud
'''
def muestraPosicion(monumento):
    print "Nombre del Monumento: ", monumento;
    serviceurl = 'http://maps.googleapis.com/maps/api/geocode/xml?'
    url = serviceurl + urllib.urlencode({'address': monumento,'components':'country:ES'})
    uh= urllib.urlopen(url)
    data = uh.read()
    location = data.split("<location>") #Nos quedamos solo con la etiqueta Location
    lat = location[1].split("</lat>") 
    lat2 = lat[0].split("<lat>") #Sacamos la latitud correspondida entre las etiquetas <lat> y </lat>
    print "latitud: ",lat2[1], " longitud: ",lat[1].split("</lng>")[0].split("<lng>")[1];
    
def muestraMonumentos(Features):
    '''Recorremos todos los elementos y sacamos sus elementos PropertyValue
        cada uno de los datos del array datos es un elemento distinto
            - datos[0] => nombre
            - datos[1] => url
            - ...
        mostramos todos los nombres.
    '''
    for feature in Features:
        datos = feature.getElementsByTagName("PropertyValue");
        print datos[0].childNodes[0].data;

def solicitaMonumento(Features):
    nombre = raw_input("Introduce el nombre del monumento: ");
    nombre2 = nombre.decode('utf-8');
    for feature in Features:
        datos = feature.getElementsByTagName("PropertyValue");
        if(datos[0].childNodes[0].data == nombre2):
            Contenido = urllib.urlopen(datos[1].childNodes[0].data); #descargamos los datos de la URL.
            output = Contenido.read();
            muestraPosicion(nombre);
            print "Página web asociada: ", datos[1].childNodes[0].data;
            print "Descripcion: "
            print cortaDescripcion(output);
            break;


ArbolDOM = xml.dom.minidom.parse("MonumentosZaragoza.xml");
catalogo = ArbolDOM.documentElement;
#Cogemos todos los elementos Features, para tenerlos agrupados por monumento
Features = catalogo.getElementsByTagName("Feature");
muestraMonumentos(Features);
solicitaMonumento(Features);