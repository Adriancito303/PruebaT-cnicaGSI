IMPORTANTE EN POSTMAN: Para ejecutar la busqueda unitaria, el metodo put y delete se realiza por medio del ID se debe copiar el ID y pegar en el final de la url y posteriormente ejecutarlo (ejemplo: http://127.0.0.1:8000/posts/delete/41ebc269-b149-4807-99f3-3d8d283e3e1f)
Para ejecutarlo activar el entorno dentro de fastapi-pg con el comando venv/Scripts/activate
En el archivo requirements.txt se tiene todas las librerias usadas en el proyecto, instalarlas en el entorno donde se quiera correr (venv ya los tiene instalados)
para ejecutar el main es dentro de fastapi-pg ejecutar uvicorn main.app
se puede visualizar el las api en postam o a su preferencia en la URL levantada del proyecto (ejemplo: 127.0.0.1:8000) añadir al final '/docs' para la visualizacion gráfica
Independientemente el ID que se escriba al crear el post se reemplazara automaticamente por un ID de tipo uuid (pagina de referencia para dichos ID: https://www.uuidgenerator.net)
