# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este archivo temporal se encuentra aquí:
C:\Users\usuario_local\.spyder2\.temp.py
"""
import json, operator

def loadJSON(input_file, out_file):
    
    v = "<b>Ubicación:</b>";
    v2 = v.decode('utf-8')
    
    v3=" <b>Semáforos:</b>"
    v4 = v3.decode('utf-8')
    
    v5="<b>Descripción:</b>"
    v6 = v5.decode('utf-8')
    
    total = 0
    listaUbicaciones = []
    listaSemaforos = [] 
    listaFinal = []
    listaOrdenada = []
#    
#    maxFrec = 0
    
    k = 0

    data = input_file.read();
    file_input = json.loads(str(data));

    
    for i in file_input['features']:
        desc = i['properties']['Description'];
        if v2 in desc:
            buscado = desc.index(v2)
            buscado2 = desc.index(v4)
            buscado3 = desc.index(v6)
            
            ubicacion = desc[buscado+len(v2):buscado2]
            ub = ubicacion.split(',')   #ubicacion
            
            

            semaforos = desc[buscado2+len(v4):buscado3]
            sem = semaforos.split('<')
            numSem = sem[0].strip()     #semaforos para ubicacion dada
            
            if numSem != '':
                listaSemaforos.append(int(str(numSem)))
                listaUbicaciones.append(ub[0])
                total += int(str(numSem))
        
    for j in listaUbicaciones:   
        frecuencia = listaSemaforos[k]/float(total) 
        #print frecuencia;
        listaFinal.append([listaUbicaciones[k],listaSemaforos[k],frecuencia]);       
        k += 1

    listaOrdenada = sorted(listaFinal, key=operator.itemgetter(2), reverse=1);
    i = 0;
    #print listaOrdenada;
    for l in listaOrdenada:
        #print l[2];
        out_file.write("Ubicación:" + str(l[0].encode('utf-8')) + ", Semáforos:" + str(l[1]) + ", Frecuencia: " + str(l[2])+ '\n');
        if i >= 10:
            break;
        i += 1;
    
    #out_file.close()#cerramos el archivo de escritura
    
    #out_file = file('Frecuencia_Semaforos.txt', 'r')
    
    
    #ordenamos JSON
    '''while True:
        line = out_file.readline()
        if not line: break
        line = line.strip()
#        json_obj = json.dumps(str(line))
        listaOrdenada.append(line)
        
    
    listaOrdenada = sorted(listaOrdenada, key = operator.itemgetter())
    print listaOrdenada

#    lines = sorted(lines, key=lambda k: k['page']['update_time'], reverse=True)
'''

    
    
   
   
try:
    input_file  = file('semaforos.txt', "r")
    outfile = open('Frecuencia_Semaforos.txt', 'w') # Indicamos el valor 'w' para que cada vez que se ejecute sobre escriba lo anterior.
    
    loadJSON(input_file, outfile);
    outfile.close()
    input_file.close()
except IOError:
    print "Error de entrada/salida."
    exit()    
    
