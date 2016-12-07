

def numero_apariciones(lectura, outfile):
    lineas = ""
    for linea in lectura.readlines():#Bucle para leer el archivo
        lineas += linea
    lineas =  lineas.replace("\n", " ")#Sustituimos los saltos de linea por espacios
    lineas = lineas.split(" ")#Separamos las palabras por espacios
    
    lista = []
    for i in lineas:#Creamos una lista para añadir las palabras que contiene el archivo
        if i not in lista:
            lista.append(i)
    
    for i in lista:#Recorremos la lista
       contador = 0
       
       for j in lineas: #Recorremos el archivo buscando las palabras de la lista
            if i == j and i != " ":
                contador += 1;
       if i != " ":
           #print("La palabra '" + i + "' aparece", contador, "veces")
           outfile.write("La palabra: " +str(i) + " aparece " + str(contador) + " veces\n")#Escribimos en el archivo

       
nombref = raw_input('Introduzca el noimbre del fichero: ')
try:
    lectura = open(nombref, 'r');
    outfile = open('texto.txt', 'w') # Indicamos el valor 'w' para que cada vez que se ejecute sobre escriba lo anterior.

    numero_apariciones(lectura, outfile);
    lectura.close()#cerramos el archivo de lectura
    outfile.close()#cerramos el archivo de escritura
except IOError:
    print "Error de entrada/salida."
    exit()