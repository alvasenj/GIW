<!DOCTYPE html>
<html>
<head>
	<title>Login</title>
	<link rel="stylesheet" type="text/css" href="style.css" />
</head>
<body>
	<div id="site_content">
      <div id="login">
      	<form action="/" method="post">
            Username: <input name="usuario" type="text" />
            Password: <input name="password" type="password" />
            <input value="Login" type="submit" />
        </form>
        <form action="/signIn">
            <input value="Registro" type="submit" />
        </form>

      </div>
     </div>
</body>
</html>