# Programación para la Ciencia de Datos - PEC4
**Universitat Oberta de Catalunya**  
**Autora**: María Femenías Hermida  
**Fecha**: Enero de 2025  


Para resolver cada uno de los ejercicios de la PEC, se ha creado un paquete Python llamado "exercises".
Este paquete contiene cinco scripts, uno por cada ejercicio.
Dentro de cada uno de ellos, se implementa la solución según las indicaciones, organizando el código en funciones para cada tarea solicitada.


## ESTRUCTURA DEL PROYECTO

La estructura jerárquica del proyecto es la siguiente:

src/
├── exercises/           # Carpeta para los módulos que contienen la lógica específica de cada ejercicio
│   ├── __init__.py      # Indica que la carpeta sea un paquete
│   ├── ex1.py           # Código de respuesta al ejercicio 1
│   ├── ex2.py           # Código de respuesta al ejercicio 2
│   ├── ex3.py           # Código de respuesta al ejercicio 3
│   ├── ex4.py           # Código de respuesta al ejercicio 4
│   └── ex5.py           # Código de respuesta al ejercicio 5
├── data/                # Carpeta para almacenar el dataset
│   └── dataset.csv
├── img/                 # Carpeta para almacenar la imagen generada en el ejercicio 3
│   └── histograma.png
├── tests/               # Módulos para pruebas unitarias de cada ejercicio
│   ├── test_ex1.py      # Pruebas para ex1.py
│   ├── test_ex2.py      # Pruebas para ex2.py
│   ├── test_ex3.py      # Pruebas para ex3.py
│   ├── test_ex4.py      # Pruebas para ex4.py  
│   ├── test_ex5.py      # Pruebas para ex5.py
├── main.py              # Archivo principal que responde la PEC
├── README.md            # Documentación del proyecto, explicando cómo ejecutarlo
├── setup.py             # Archivo para empaquetar el proyecto
├── requirements.txt     # Dependencias del proyecto
└── LICENSE.txt          # Licencia del proyecto


## Requisitos previos
- Python 3.8 o superior
- Sistema operativo: Compatible con Windows, MacOS y Linux


## USO

El script principal, `main.py`, importa el paquete exercises y utiliza las funciones definidas para resolver cada uno de los ejercicios. Además, permite ejecutar ejercicios específicos o mostrar ayuda.

- Para ejecutar main.py:
    1. Para ejecutar todo el flujo de la PEC: python main.py

    2. Para mostrar un ejercicio específico: python main.py [número de ejercicio]
       Ejemplo: python main.py 2

    3. Para mostrar ayuda:
       python main.py --help


## DEPENDENCIAS

Las dependencias están definidas en requirements.txt.
Para instalar todas las dependencias, ejecuta: pip install -r requirements.txt


## PRUEBAS
El proyecto incluye pruebas unitarias para cada ejercicio, ubicadas en la carpeta tests.
- Para ejecutar las pruebas, desde el directorio tests: python -m unittest discover

- Para mostrar la cobertura de los tests (desde src): 
   1. Ejecutar: coverage run -m unittest discover -s tests
   2. Ejecutar: coverage report
   3. Para un informe en generado en HTML, ejecutar: coverage html
   4. Para borrar datos de cobertura anteriores, ejecutar: coverage erase

- Para ejecutar un test en específico (ej. test del módulo ex4): python -m unittest test_ex4.py

El coverage report para los tests resulta:

Name                    Stmts   Miss  Cover
-------------------------------------------
exercises\__init__.py       0      0   100%
exercises\ex1.py           12      0   100%
exercises\ex2.py           12      1    92%
exercises\ex3.py           29      0   100%
exercises\ex4.py           27      4    85%
exercises\ex5.py           19      0   100%
tests\test_ex1.py          37      1    97%
tests\test_ex2.py          22      1    95%
tests\test_ex3.py          36      1    97%
tests\test_ex4.py          33      2    94%
tests\test_ex5.py          34      1    97%
-------------------------------------------
TOTAL                     261     11    96%

## PEP8

El código sigue la guía de estilo de Python (PEP8). Para demostrarlo, se utilizó la herramienta `pylint` para analizar el paquete `exercises` y el archivo `main.py`.

- Para ejecutar pylint sobre `main.py`: pylint main.py
- Para ejecutar pylint sobre los scripts del paquete `exercises`: pylint exercises/*.py

Para todos los archivos, se obtiene como resultado:
--------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)

## LICENCIA
Este proyecto está licenciado bajo la Licencia MIT. El archivo se puede consultar en [LICENSE](LICENSE.txt) para más detalles.