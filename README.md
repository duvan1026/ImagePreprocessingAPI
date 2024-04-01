## IMAGE__PREPROCESSING__API

Este es un archivo README para la API de procesamiento de im�genes en Python.

### Preparaci�n del Entorno

Antes de proceder con la instalaci�n y configuraci�n de la API, aseg�rate de tener Python instalado en tu sistema. Sigue los siguientes pasos:

1. **Instalaci�n de Python 3.12.2 amd64:**
   - Descarga el instalador de Python 3.12.2 amd64 desde [python.org](https://www.python.org/downloads/).
   - Ejecuta el instalador como administrador.
   - Durante la instalaci�n, aseg�rate de seleccionar la opci�n para agregar Python al PATH del sistema.

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

7. **Configurar el IIS:**
   - Abre el Administrador de IIS.
   - Crea un nuevo sitio web.
   - Asigna la carpeta de la API como ruta f�sica del sitio web.
   - Aseg�rate de configurar correctamente los permisos de acceso.
   - Configura cualquier otro ajuste necesario para tu entorno espec�fico.

Con estos pasos, tu API deber�a estar lista para ejecutarse en IIS.

