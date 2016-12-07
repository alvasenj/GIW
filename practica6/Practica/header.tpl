<!DOCTYPE html>
<html xml:lang="en">

<head>
  <title>{{title}}</title>
  <meta http-equiv="content-type" content="text/html; charset=iso-8859-1" />
  <link rel="stylesheet" type="text/css" href="style.css" />
</head>

<body>
  <div id="main">
    <div id="header">
      <div id="logo">
        <h1>Libreria</h1>
      </div>
      <div id="menubar">
        <ul id="menu">
          <li class="tab_selected"><a href="/">Principal</a></li>
          <li><a href="/addBook">Añadir libro</a></li>
          <li><a href="/libreria">Libros</a></li>
          <li><a href="/libreriaUpdate">Modificar Libros</a></li>
          <li><form action="/buscar" method="post">
            Nombre del libro: <input name="titulo" type="text" />
            <input value="Buscar" type="submit" />
        </form>
        </li>
        <li><form action="/logout" method="post">
            <input value="Cerrar Sesión" type="submit" />
        </form>
        </li>
        </ul>
      </div>
    </div>
    <div id="site_content">
      <div id="content">