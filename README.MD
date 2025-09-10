"""
# 🚀 PySpark + Docker + JupyterLab

Este proyecto proporciona una configuración inicial para ejecutar **PySpark** en un entorno de **Docker**, accediendo a través de **JupyterLab**.
Ideal como base para desarrollar y probar código de **Big Data** con Python.

---

## 📦 Requisitos previos

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [Python](https://www.python.org/downloads/)

---

## ⚙️ Levantar el entorno

1. Construir la imagen y levantar los servicios:
```bash
   docker compose up -d --build
```
2. Verificar que el contenedor esté corriendo:
```bash
   docker ps
```
---

## 🔑 Acceso a JupyterLab

1. Obtener el **token de acceso** desde los logs del contenedor:
```bash
   docker compose logs pyspark-service \
     | grep -m 1 "http://127.0.0.1" \
     | awk '{print "URL:", $NF}'
```
```bash
   Ejemplo de salida:
   URL: http://127.0.0.1:8888/lab?token=33969378520ae1a4d323fba9917c9565271f1a9c3a2c33f4
```
2. Creamos un nuevo archivo `.ipynb` y en la parte derecha posterior nos dara la opcion de seleccionar el kernel **Python 3 (ipykernel)**
3. Seleccionamos la opcion `Servidor de Jupyter existente` y pegamos la URL obtenida.
---

## 📓 Uso del Notebook
1. Probar PySpark con el siguiente código:

   from pyspark.sql import SparkSession
```bash
   # Crear sesión de Spark
   spark = SparkSession.builder.appName("test").getOrCreate()

   # Crear un DataFrame de prueba
   df = spark.range(5).toDF("number")
   df.show()
```
Resultado esperado:
```bash
   +------+
   |number|
   +------+
   |     0|
   |     1|
   |     2|
   |     3|
   |     4|
   +------+
```
---
## 🗄️ Conexión a Bases de Datos (Postgres / SQL Server)
### 🔹 Ejemplo: Conexión a SQL Server
![CONEXION SQL SERVER](https://i.imgur.com/gGlIctq.png)

### 🔹 Ejemplo: Conexión a PostgreSQL
![CONEXION POSTGRESQL](https://i.imgur.com/l0uDPIU.png)
---
## 🛑 Detener el entorno

Para detener los contenedores:

   docker compose down

