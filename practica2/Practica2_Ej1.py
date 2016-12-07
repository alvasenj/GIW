import csv, os, operator

def contaminacion():
	error = False;
	try:
		csvFile = open("agua_eprtr_2008_030412.csv");
	except IOError:
		error = True;
		print ("Error al intentar abrir el archivo \"agua_eprtr_2008_030412.csv\".");
	if(error == False):
		csvFileOutput = open("AguaAgrupada.csv","w");
		lector = csv.reader(csvFile, delimiter=';');
		escritor = csv.writer(csvFileOutput, delimiter=',');
		datos=list(lector);
		act = "";
		escritor.writerow(["contaminacion","empresa"]);
		for elem in datos:
			if(elem[2] != act and elem[9] != "(null)" and elem[3] != "NIMA"):
				escritor.writerow([elem[9],elem[2]]);
				act = elem[2];
		csvFile.close();


def frecuencias():
	error = False;
	try:
		csvFile = open("residuos_peligrosos_eprtr_2008_040412.csv");
	except IOError:
		error = True;
		print ("Error al intentar abrir el archivo \"residuos_peligrosos_eprtr_2008_040412.csv\".");

	if(error == False):
		csvFileOutput = open("FrecuenciaResiduos.csv","w");
		lector = csv.reader(csvFile, delimiter=';');
		escritor = csv.writer(csvFileOutput, delimiter=',');
		datos=list(lector);
		act = datos[0][2];
		frec = 1;
		escritor.writerow(["jugador","frecuencia"]);
		for elem in datos:
			if(elem[2] == act):
				frec = frec + 1;
			else:
				if(elem[3] != "NIMA" and elem[2] != "(null)"):
					escritor.writerow([act,frec]);
					act = elem[2];
					frec = 1;
		csvFile.close();

def top10():
	error = False;
	try:
		csvFile = open("aire_eprtr_2008_030412.csv");
	except IOError:
		error = True;
		print ("Error al intentar abrir el archivo \"aire_eprtr_2008_030412.csv\".");

	if(error == False):
		lector = csv.reader(csvFile, delimiter=';');
		datos=list(lector);
		dato = [];
		lista = [];

		act = datos[1][2];
		suma = 0.0;
		i = 0;

		for elem in datos:
			if(elem[2] == act and elem[3] != "NIMA" and elem[10] != "(null)"):
				elem[10] = elem[10].replace(',','.');
				suma = suma + float(elem[10]);
			else:
				if(elem[3] != "NIMA" and elem[2] != "(null)"):
					lista.insert(i,[act,suma]);
					i = i + 1;
					act = elem[2];
					suma = 0.0;
		csvFile.close();

		csvFileOutput = open("Contaminantes.csv","w");
		escritor = csv.writer(csvFileOutput, delimiter=',');
		sortedlist = sorted(lista, key=operator.itemgetter(1), reverse=1);
		o = 0;
		for elem in sortedlist:
			if o >= 10:
				break;
			escritor.writerow([elem[0],elem[1]]);
			o = o + 1;

		csvFileOutput.close();

contaminacion();
frecuencias();
top10();
