Para ejecutarlo activar el entorno dentro de fastapi-pg con el comando venv/Scripts/activate
En el archivo requirements.txt se tiene todas las librerias usadas en el proyecto, instalarlas en el entorno donde se quiera correr (venv ya los tiene instalados)
para ejecutar el main es dentro de fastapi-pg ejecutar uvicorn main.app
se puede visualizar el las api en postam o a su preferencia en la URL levantada del proyecto (ejemplo: 127.0.0.1:8000) añadir al final '/docs' para la visualizacion gráfica
Independientemente el ID que se escriba al crear el post se reemplazara automaticamente por un ID de tipo uuid (pagina de referencia para dichos ID: https://www.uuidgenerator.net)
