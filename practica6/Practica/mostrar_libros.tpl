% include('header.tpl', title='Libreria')
            <h1>Libros que se encuentran en la librería</h1>
            <table>
            <tr><th>Id</th><th>Item</th><th>Cantidad</th></tr>
            %for row in rows:
                <tr>
                %for col in row:
                    <td>{{col}}</td> 
                %end
                    <td>
                     <form action="/remove" method="post">
                         <input name="id" type="hidden" value={{row[0]}}/>
                        <input type="submit" value="Eliminar"/>
                    </form>
                    </td>
                </tr>
            %end
            </table>
        </div>
    </body>
</html>

