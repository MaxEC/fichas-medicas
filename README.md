# fichas-medicas

Este proyecto tiene como objetivo automatizar la búsqueda de fichas médicas previamente respondidas desde un formulario de Google y generar un archivo en formato `docs` para impresión. Las fichas médicas son respuestas a un Google Forms que recopilan información sobre los beneficiarios o staff de los campamentos.

## Resumen de Comandos (Windows)

Para configurar y ejecutar el proyecto, sigue estos comandos en el terminal:

```bash
python -m venv env
Get-ExecutionPolicy -List
Set-ExecutionPolicy Remote -Scope CurrentUser
env\Scripts\Activate.ps1
pip install -r requirements.txt
python generator.py
```

## Requisitos

Asegúrate de tener instalado Python y las siguientes herramientas:

- Python 3.x
- pip

## Instalación

0. **Cambia variables del código**:
   - Si el archivo CSV tiene `;` o `,`, edita el código del delimitador en `methods.py`:
     ```python
     with open(archivo_antiguas, newline='', encoding='utf-8') as csvfile:
         reader = csv.reader(csvfile, delimiter=',')
     ```

   - Define los nombres de los archivos CSV (fichas médicas antiguas y nuevas) en `generator.py`:
     ```python
     if __name__ == '__main__':
         archivo_antiguas = 'antiguas.csv'
         archivo_nuevas = 'nuevas.csv'
     ```

1. **Crea un entorno virtual**:

   ```bash
   python -m venv env
   ```

2. **Configura la política de ejecución de PowerShell (solo en Windows)**:

   ```bash
   Get-ExecutionPolicy -List
   Set-ExecutionPolicy Remote -Scope CurrentUser
   ```

3. **Activa el entorno virtual**:

   ```bash
   env\Scripts\Activate.ps1
   ```

4. **Instala las dependencias necesarias**:

   ```bash
   pip install -r requirements.txt
   ```

5. **Ejecuta el generador de fichas médicas**:

   ```bash
   python generator.py
   ```

## Funcionamiento

El código busca en un archivo `antiguas.csv` las fichas médicas respondidas anteriormente y utiliza la información de la ficha más reciente según la "Marca temporal" del usuario. La búsqueda se realiza utilizando el RUT como identificador único.


## Generación de Documentos

Una vez que la búsqueda y el cruce de datos entre `nuevas.csv` y `antiguas.csv` se complete, se generará automáticamente un archivo `docs` que se podrá imprimir.

