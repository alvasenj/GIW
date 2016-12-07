# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este archivo temporal se encuentra aquí:
C:\Users\usuario_local\.spyder2\.temp.py
"""

import json


def loadJSON(input_file):

    js = json.loads(input_file.read().decode("utf-8-sig"))  
    print(js)
    #    for i in js:#Recorremos la lista
    #        print(js['Ubicación'])       
       
    
    
    
try:
    input_file  = file('semaforos.txt', "r")
    outfile = open('texto.txt', 'w') # Indicamos el valor 'w' para que cada vez que se ejecute sobre escriba lo anterior.

    loadJSON(input_file);
    outfile.close()#cerramos el archivo de escritura
except IOError:
    print "Error de entrada/salida."
    exit()    
    
