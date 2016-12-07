# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal
"""
def desplazamiento(cadena, desplazamiento):
    cadena = cadena.upper();
    cadena2 = "";
    for i in range(0,len(cadena)):
        if ord(cadena[i]) > 64 and ord(cadena[i]) < 91:
            cadena2 += chr((((ord(cadena[i])-65) + desplazamiento)%26)+65);
        else:
            cadena2 += cadena[i];
    cadena2 = cadena2.lower();
    return cadena2;
    
def permutacion(cadena, cambio):
    division = cadena.split(" ");
    salida = "";
    division2 = [];
    for i in range(0,len(division)):
        division2.insert((i+cambio)%len(division),division[i]);
    for i in range(0,len(division2)):
        salida += division2[i] + " ";
    return salida;

cadena = raw_input('Introduce la cadena\n');
despla= raw_input('Introduce el desplazamiento\n');
cambio = raw_input('Introduce la rotacion\n');
if despla.isdigit() and cambio.isdigit() and not cadena.isdigit():
    print permutacion(desplazamiento(cadena,int(despla)),int(cambio));
else:
    print "error en alguno de los datos introducidos";
