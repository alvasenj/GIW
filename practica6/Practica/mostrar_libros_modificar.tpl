% include('header.tpl', title='libreria')
            <h1>Libros que se encuentran en la librería</h1>
            <table>
            <tr><th>Item</th><th>Cantidad</th></tr>
            %for row in rows:
                <tr>
                    <form action="/libreriaUpdate" method="post">
                        <td><input type="text" name="titulo" value="{{row[1]}}"/></td> 
                        <td><input type="text" name="cantidad" value="{{row[2]}}"/></td> 
                        <td>
                            <input name="id" type="hidden" value={{row[0]}}/>
                            <input type="submit" value="Modificar"/>
                        </td>
                    </form>
                </tr>
            %end
            </table>
        </div>
    </body>
</html>
