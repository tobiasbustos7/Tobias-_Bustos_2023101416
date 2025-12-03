# Ganadería Paraguay - Plataforma Informativa de Venta de Ganado

## Cómo Ejecutar el Sistema

La forma recomendada de ejecutar esta aplicación es utilizando Docker Compose, que gestiona tanto el entorno de la aplicación Flask como la base de datos MySQL.

### 1. Configuración de la Base de Datos

Iniciar el Contenedor MySQL:**

**A. Inicia el contenedor de MySQL, asignándole el nombre `ganaderia_db` y conectándolo a la red.**

```bash
docker run --name ganaderia_db -e MYSQL_ROOT_PASSWORD=1234 -e MYSQL_DATABASE=ganaderia_paraguay -p 3306:3306 --network ganaderia-net -d mysql:8
```

**B. Ejecutar Comandos SQL:**

Espera unos momentos para que MySQL se inicialice. Luego, ejecuta los comandos de `sql.sql` para crear las tablas.

```bash
docker exec -i ganaderia_db mysql -uroot -p1234 ganaderia_paraguay < sql.sql
```

### 2. Ejecutar la Aplicación Flask

**A. Ejecución Local (Requiere dependencias de Python):**

1.  Instala las dependencias (asumiendo que `requeriments.txt` lista `Flask` y `mysql-connector-python`):
    ```bash
    pip install -r requeriments.txt
    ```
2.  Ejecuta la aplicación:
    ```bash
    python app.py
    ```

### 3. Acceder a la Aplicación

La aplicación estará expuesta en el puerto estándar de Flask (5000).

Accede al dashboard navegando a:
`http://127.0.0.1:5000/`