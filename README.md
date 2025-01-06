# selenium-python-testing

A partir del uso de python y selenium, se realizan pruebas automatizadas a una página de vuelos.

## Tabla de Contenidos

1. [Requisitos previos](#requisitos-previos)
2. [Configuración](#configuración)
3. [Uso](#uso)
4. [Tecnologías Utilizadas](#tecnologías-utilizadas)

## Requisitos previos
1. Se instala la última versión de python desde la [página oficial](https://www.python.org/downloads/). En este caso se utilizó 3.13.1
2. Necesitarás [git](https://git-scm.com/) para clonar el repositorio  
3. Necesitarás un IDE. Desde la [página oficial](https://code.visualstudio.com/download) de visual studio, descargar la última versión para su sistema operativo. Puedes usar cualquier otro IDE de preferencia.

## Configuración
1. Desde el IDE, abrir y seleccionar la opción "Clone Git Repository"
2. Especificar la url: https://github.com/anapaomar/selenium-python-testing e indicar el directorio de trabajo. 
    También lo puedes hacer por comandos desde la terminal
    ```bash
    git clone https://github.com/anapaomar/selenium-python-testing
3. Desde el directorio del proyecto en local, crear un nuevo entorno virtual
    ```bash
    python -m venv venv
4. Activa el entorno virtual
    ```bash
    .\venv\Scripts\activate 
5. Instala las dependencias desde el archivo requirements.txt
    ```bash
    pip install -r requirements.txt
6. Descargar allure report desde [git](https://github.com/allure-framework/allure2/releases). Se descargar el ZIP, se descomprime y se añade la ruta al PATH.
7. Descargar el cliente de [sqlite](https://sqlitebrowser.org/dl/) para tu sistema operativo

## Uso

1. Ejecución básica: 
    Desde la raiz del proyecto ejecutar pytest -s .\test\[nombre_fichero_test].py
    ```bash
    pytest -s .\test\test_case1.py
La opción -s me permite ver la salida de logs desde la terminal.

2. Ejecución paralela
    Desde la raiz del proyecto ejecutar pytest -s -n [numero_workers] .\test\
    ```bash
    pytest -s -n 4 .\test\
La opción -n indica la cantidad de ejecutores. Para este caso se utilizarán 4 y se ejecutarán todas las pruebas que se encuentren en el directorio de test.
    También se puede especificar un solo fichero de test.py

3. Generar reportes con allure
    Desde la raiz del proyecto ejecutar pytest -s .\test\[nombre_fichero_test].py --alluredir=allure-results
    ```bash
    pytest -s .\test\test_case5.py --alluredir=allure-results

La opción --alluredir=allure-results permite almacenar los resultados de las pruebas en el directorio allure-results

4. Visualizar reportes allure
    Ejecutar el comando 
    ```bash
    allure serve allure-results

5. Visualizar los registros de los test en base de datos
    Hacer uso del cliente para SQlite, abrir base de datos e indicar el fichero resultados.db que se genera a partir de las ejecuciones de test.

## Tecnologías utilizadas

* **Python**: Lenguaje de programación utilizado para las pruebas.
* **Selenium**: Herramienta para la automatización de pruebas en navegadores web.
* **pytest**: Framework de testing para ejecutar las pruebas.
* **Allure**: Herramienta para generar reportes interactivos.
* **SQLite**: Base de datos utilizada para almacenar los resultados de las pruebas.











