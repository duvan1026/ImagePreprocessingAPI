## IMAGE__PREPROCESSING__API

Este es un archivo README para la API de procesamiento de imágenes en Python.

### Publicación en IIS

Para publicar esta API en IIS, sigue los siguientes pasos:

1. **Crear un entorno virtual:**
   - Abre la consola de comandos como administrador.
   - Navega hacia la carpeta donde está ubicada la publicación del aplicativo.
   - Ejecuta el siguiente comando: 
     ```
     python -m venv flaskapivenv
     ```
     El nombre **flaskapivenv** puede ser cambiado según tu aplicación.
2. **Activar el entorno virtual:**
   - Dirígete a la ruta del script `flaskapivenv\Scripts\activate.bat`.
   - Activa el script.
   - Ejemplo de salida después de activar el entorno virtual: 
     ```
     (flaskapivenv) C:\DuvanCastro\Aplicaciones\FlaskWebProjectDemo>
     ```

3. **Instalar Flask en el entorno virtual:**
   - Ejecuta el comando:
     ```
     pip install flask
     ```
   - Espera a que se instale. La versión instalada será, por ejemplo, `flask 3.0.2`.

4. **Instalar Pillow en el entorno virtual:**
   - Ejecuta el comando:
     ```
     pip install pillow
     ```
   - Espera a que se instale. La versión instalada será, por ejemplo, `pillow 10.3.0`.

5. **Instalar dependencias adicionales:**
   - En este caso, para instalar `img2table`, ejecuta:
     ```
     pip install img2table
     ```
   - Y para `requests`, ejecuta:
     ```
     pip install requests
     ```

6. **Ejecutar la APIWEB:**
   - Ejecuta el comando:
     ```
     python runserver.py
     ```
     Asegúrate de que `runserver.py` corresponde al archivo principal de ejecución de la API.

Con estos pasos, tu API debería estar lista para ejecutarse en IIS.

