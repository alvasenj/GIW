# -*- coding: utf-8 -*-
"""
Editor de Spyder

Ejercicio 2 PRÁCTICA 1

Enviamos un correo electrónico usando python
"""

from smtplib import SMTP
from smtplib import SMTPException

def serverConnect(username, password, receivers, message):
    server = SMTP('smtp.live.com:587') #Nos conectamos al servidor de correo outlook desde el puerto 587
    server.ehlo()    
    server.starttls() 
    server.ehlo()
    server.login(username,password) #Nos logueamos con los datos del emisor
    server.sendmail(username, receivers, message) #Enviamos el mensaje
    server.quit()     #Cerramos la conexion con el servidor

send = 'NO'
    
print('CORREO USANDO PYTHON\n')

# Datos de la cuenta de correo del emisor
username = raw_input('Introduzca su usuario: ')
password = raw_input('Introduzca su password: ')

while send.upper() == 'NO': #Hasta que el usuario no confirme los datos seguiremos pidiendo receptor y mensaje
    receivers = raw_input('To: \n') #Receptor
    message = raw_input('Introduzca el mensaje: \n') #Mensaje
    send = raw_input('¿Desea enviar el mensaje? SI/NO \n')
try:
    serverConnect(username, password, receivers, message)
    print("Successfully sent email")
    exit()
except SMTPException:
    print("Error: unable to send email")
    


   

   
