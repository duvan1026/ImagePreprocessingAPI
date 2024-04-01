## IMAGE__PREPROCESSING__API

Este es un archivo README para la API de procesamiento de im�genes en Python.

### Publicaci�n en IIS

Para publicar esta API en IIS, sigue los siguientes pasos:

1. **Crear un entorno virtual:**
   - Abre la consola de comandos como administrador.
   - Navega hacia la carpeta donde est� ubicada la publicaci�n del aplicativo.
   - Ejecuta el siguiente comando: 
     ```
     python -m venv flaskapivenv
     ```
     El nombre **flaskapivenv** puede ser cambiado seg�n tu aplicaci�n.
2. **Activar el entorno virtual:**
   - Dir�gete a la ruta del script `flaskapivenv\Scripts\activate.bat`.
   - Activa el script.
   - Ejemplo de salida despu�s de activar el entorno virtual: 
     ```
     (flaskapivenv) C:\DuvanCastro\Aplicaciones\FlaskWebProjectDemo>
     ```

3. **Instalar Flask en el entorno virtual:**
   - Ejecuta el comando:
     ```
     pip install flask
     ```
   - Espera a que se instale. La versi�n instalada ser�, por ejemplo, `flask 3.0.2`.

4. **Instalar Pillow en el entorno virtual:**
   - Ejecuta el comando:
     ```
     pip install pillow
     ```
   - Espera a que se instale. La versi�n instalada ser�, por ejemplo, `pillow 10.3.0`.

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
     Aseg�rate de que `runserver.py` corresponde al archivo principal de ejecuci�n de la API.

Con estos pasos, tu API deber�a estar lista para ejecutarse en IIS.

