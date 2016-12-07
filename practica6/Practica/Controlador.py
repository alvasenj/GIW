# -*- coding: utf-8 -*-
"""

@author: Alberto Marquez Gómez
@author: Álvaro Asenjo Torrico	
@author: Juan José Montiel Cano

"""
import sqlite3
from bottle import route, request, response, run, template, error

access = False

@route('/')
def login():
    username = request.get_cookie('account', secret='some-secret-key')
    if(username is None):       
        return template('login')
    else:
        return mostrar_libros()

@route('/',method='POST') 
def do_login():
    username = request.forms.get('usuario')
    password = request.forms.get('password')
    db = sqlite3.connect('libreria.sqlite3')
    cur = db.cursor()
    cur.execute("SELECT nombre FROM compradores where nombre= '%s' and password = '%s'" % (username, password))
    if cur.fetchone() is not None:
        global access
        access = True
        response.set_cookie('account', username, secret='some-secret-key')
        return mostrar_libros()
    else: 
        return "Debe registrarse antes de iniciar sesion \n", signIn()
    cur.close()
       
@route('/signIn') 
def signIn():
    return '''
        <form action="/signIn" method="post">
            Username: <input name="usuario" type="text" />
            Password: <input name="password" type="password" />
            <input value="signIn" type="submit" />
        </form>'''

@route('/signIn',method='POST') 
def do_signIn():
    username = request.forms.get('usuario')
    password = request.forms.get('password')
    db = sqlite3.connect('libreria.sqlite3')
    cur = db.cursor()
    cur.execute("SELECT nombre FROM compradores where nombre= '%s'" % (username))
    if cur.fetchone() is None:
        cur.execute('INSERT INTO compradores(nombre, password) VALUES(?,?)',(username,password))
        db.commit()
    else:
        return "Ya existe un usuario con dicho nombre \n .Introduzca un usuario válido", signIn()
    cur.close()
    return login()
    
@route('/libreria')
def mostrar_libros():
    username = request.get_cookie('account', secret='some-secret-key')
    if(username is None and access== False):
        return login()
    else:
        db = sqlite3.connect('libreria.sqlite3')
        c = db.cursor()
        c.execute("SELECT id,item,cantidad FROM libros")
        data = c.fetchall()
        c.close()
        output = template('mostrar_libros', rows=data)
        return output
        
@route('/libreria',method='POST')
def do_mostrar_libros():
    db = sqlite3.connect('libreria.sqlite3')
    c = db.cursor()
    c.execute("SELECT id,item,cantidad FROM libros")
    data = c.fetchall()
    c.close()
    output = template('mostrar_libros', rows=data)
    return output

@route('/remove',method='POST')
def do_remove():
    id = request.forms.get('id')
    id = id.split('/')
    id = int(id[0])
    db = sqlite3.connect('libreria.sqlite3')
    cur = db.cursor()
    cur.execute('DELETE FROM libros where id="%i"' % id)
    db.commit()
    cur.close()
    return do_mostrar_libros()

@route('/libreriaUpdate')
def mostrar_libros_update():
    username = request.get_cookie('account', secret='some-secret-key')
    if(username is None):
        return login()
    else:     
        db = sqlite3.connect('libreria.sqlite3')
        c = db.cursor()
        c.execute("SELECT id,item,cantidad FROM libros")
        data = c.fetchall()
        c.close()
        output = template('mostrar_libros_modificar', rows=data)
        return output
        
@route('/libreriaUpdate',method='POST')
def do_update_libros():
    id = request.forms.get('id')
    id = id.split('/')
    id = int(id[0])
    titulo = request.forms.get('titulo')
    cantidad = request.forms.get('cantidad')
    db = sqlite3.connect('libreria.sqlite3')
    c = db.cursor()
    c.execute("UPDATE libros SET item = ?, cantidad = ? WHERE id = ?", (titulo,cantidad,id))
    db.commit()
    c.close()
    return mostrar_libros_update();

        
@route('/buscar',method='POST')
def do_buscar_libros():
    titulo = request.forms.get('titulo')
    db = sqlite3.connect('libreria.sqlite3')
    c = db.cursor()
    c.execute("SELECT id,item,cantidad FROM libros where item = '%s'" % titulo)
    data = c.fetchall()
    c.close()
    output = template('mostrar_libros', rows=data)
    return output

@route('/addBook') 
def addBook():
    username = request.get_cookie('account', secret='some-secret-key')
    if(username is None):
        return login()
    else:
        return '''
            <form action="/addBook" method="post">
                Titulo: <input name="titulo" type="text" />
                Cantidad: <input name="cantidad" type="int" />
                <input value="addBook" type="submit" />
            </form>
            <form action="/libreria">
                <input value="Principal" type="submit" />
            </form>'''

@route('/addBook',method='POST')
def do_addBook():
    titulo = request.forms.get('titulo')
    cantidad = request.forms.get('cantidad')
    db = sqlite3.connect('libreria.sqlite3')
    cur = db.cursor()
    cur.execute('INSERT INTO libros(item, cantidad) VALUES(?,?)',(titulo,cantidad))
    db.commit()
    cur.close()
    return login()

@route('/logout',method='POST')
def do_logout():
    response.set_cookie('account', None, secret='some-secret-key')
    global access
    access = False
    return "Se ha cerrado su sesion\n"

'''---------------GESTION DE ERRORES-------------------- '''
@error(404)
def error404(error):
    return 'Error en la página solicitada'

    
run(host='localhost', port=8080, debug=True)
