# 🚀 PySpark + Docker + JupyterLab

Este proyecto proporciona una configuración inicial para ejecutar **PySpark** en un entorno de **Docker**, accediendo a través de **JupyterLab**.
Ideal como base para desarrollar y probar código de **Big Data** con Python.

---

## 📑 Índice
- [🚀 PySpark + Docker + JupyterLab](#-pyspark--docker--jupyterlab)
  - [📑 Índice](#-índice)
  - [📦 Requisitos previos](#-requisitos-previos)
  - [⚙️ Levantar el entorno](#️-levantar-el-entorno)
  - [🔑 Acceso a JupyterLab](#-acceso-a-jupyterlab)
  - [🗄️ Conexión a Bases de Datos (Postgres / SQL Server)](#️-conexión-a-bases-de-datos-postgres--sql-server)
    - [🔹 Ejemplo: Conexión a SQL Server](#-ejemplo-conexión-a-sql-server)
    - [🔹 Ejemplo: Conexión a PostgreSQL](#-ejemplo-conexión-a-postgresql)
  - [🛑 Detener el entorno](#-detener-el-entorno)

---

## 📦 Requisitos previos

Asegúrate de tener instalados:

- [🐳 Docker](https://docs.docker.com/get-docker/)
- [⚙️ Docker Compose](https://docs.docker.com/compose/install/)
- [🐍 Python](https://www.python.org/downloads/)

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

1. Obtener la **URL de acceso con token** desde los logs del contenedor:
   ```bash
   docker compose logs pyspark-service | grep -m 1 "http://127.0.0.1" | awk '{print "URL:", $NF}'
   ```

   **Ejemplo de salida:**
   ```bash
   URL: http://127.0.0.1:8888/lab?token=33969378520ae1a4d323fba9917c9565271f1a9c3a2c33f4
   ```

2. Si queremos manejarlo desde VSCode, seguir estos pasos:
   - Crear un nuevo archivo `.ipynb`
   - Hacer clic en **Seleccionar kernel** (arriba a la derecha)
   - Elegir **Servidor de Jupyter existente**
   - Pegar la URL obtenida
   - Seleccionar `Python 3 (ipykernel)`

   ✅ Ahora tu Notebook estará listo para usar PySpark, se ha dejado un archivo de prueba llamado `pyspark_test.ipynb` para que puedas verificar que todo funciona correctamente.

   ![SELECCIONAR KERNEL](https://i.imgur.com/wv9Cm34.png)
   ![SERVIDOR JUPYTER](https://i.imgur.com/bbNr4JD.png)
   ![SERVIDOR URL](https://i.imgur.com/bxUfTR5.png)
   ![INGRESAR NOMBRE](https://i.imgur.com/cctOIzh.png)
   ![SELECCION KERNEL](https://i.imgur.com/S3XE0aV.png)
   ![KERNEL ACTUALIZADO](https://i.imgur.com/8U0Jdbt.png)

3. Alternativamente, puedes acceder a JupyterLab directamente desde tu navegador web con la URL obtenida en el paso 1
---

## 🗄️ Conexión a Bases de Datos (Postgres / SQL Server)

Las claves de conexión a las bases de datos de SQL Server y PostgreSQL están configuradas por defecto en el archivo de `docker-compose.yml`, por lo que no es necesario modificarlas a menos que desees personalizarlas.

- **SQL Server**
   - SA_PASSWORD: Password123!

- **PostgreSQL**
   - POSTGRES_PASSWORD: password

### 🔹 Ejemplo: Conexión a SQL Server
![CONEXION SQL SERVER](https://i.imgur.com/gGlIctq.png)

### 🔹 Ejemplo: Conexión a PostgreSQL
![CONEXION POSTGRESQL](https://i.imgur.com/l0uDPIU.png)

---

## 🛑 Detener el entorno

Para detener los contenedores:

```bash
docker compose down
```
