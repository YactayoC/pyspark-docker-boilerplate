# 🚀 PySpark + Docker + JupyterLab + Bases de Datos

Este proyecto proporciona una configuración inicial para ejecutar **PySpark** en un entorno de **Docker**, accediendo a través de **JupyterLab**.
Además, se incluyen contenedores de **PostgreSQL, SQL Server, MySQL y Oracle Free**, ideales para pruebas de conexión y desarrollo de proyectos de Big Data.

---

## 📑 Índice
- [🚀 PySpark + Docker + JupyterLab + Bases de Datos](#-pyspark--docker--jupyterlab--bases-de-datos)
  - [📑 Índice](#-índice)
  - [📦 Requisitos previos](#-requisitos-previos)
  - [⚙️ Levantar el entorno](#️-levantar-el-entorno)
  - [🔑 Acceso a JupyterLab](#-acceso-a-jupyterlab)
  - [🗄️ Conexión a Bases de Datos (Postgres / SQL Server / MySQL / Oracle)](#️-conexión-a-bases-de-datos-postgres--sql-server--mysql--oracle)
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

2. Verificar que los contenedores estén corriendo:
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

   ✅ Ahora tu Notebook estará listo para usar PySpark. Se ha dejado un archivo de prueba llamado `pyspark_test.ipynb` para que verifiques que todo funciona correctamente.

3. Alternativamente, puedes acceder a JupyterLab directamente desde tu navegador con la URL obtenida en el paso 1.

---

## 🗄️ Conexión a Bases de Datos (Postgres / SQL Server / MySQL / Oracle)

Las claves de conexión están configuradas por defecto en el archivo `docker-compose.yml`.

- **SQL Server**
  - Usuario: `sa`
  - Password: `initops2025!`
  - Puerto: `1433`

- **PostgreSQL**
  - Usuario: `user`
  - Password: `initops2025!`
  - Base de datos: `testdb`
  - Puerto: `5432`

- **MySQL**
  - Usuario: `user`
  - Password: `initops2025!`
  - Root Password: `initops2025!`
  - Base de datos: `testdb`
  - Puerto: `3306`

- **Oracle Free (23c)**
  - Usuario administrador: `SYSTEM`
  - Password: `initops2025!`
  - Usuario de aplicación (por defecto): `my_user`
  - Password de aplicación: `initops2025!`
  - **Service Name:** `FREEPDB1`  ← ⚠️ *ya no se usa el SID `XE`*
  - Puerto: `1521`

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
