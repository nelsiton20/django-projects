# Blog Simple en Django 📝

Este es un proyecto de blog desarrollado con Django. Permite a los usuarios autenticados realizar publicaciones y gestionar comentarios asociados a cada entrada.

## 🚀 Funcionalidades

- Autenticación de usuarios para realizar publicaciones.
- CRUD (Crear, Leer, Actualizar, Eliminar) para publicaciones.
- Sección de comentarios para cada publicación.
- Diseño moderno y responsive.

## 🛠️ Tecnologías utilizadas

- Django
- HTML, CSS y JavaScript
- SQLite (base de datos por defecto)

## 🏁 Requisitos

Antes de iniciar el proyecto, asegúrate de tener instalados los siguientes componentes:

- Python 3.6 o superior
- Virtualenv (opcional pero recomendado)
- Django (instalación detallada más adelante)

## 📦 Instalación

1. Clona el repositorio:

   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd NOMBRE_DEL_PROYECTO

2. Crea y activa un entorno virtual:
    ```bash
    python3 -m venv env
    source env/bin/activate  # En Windows: env\Scripts\activate

3. Instala las dependencias:
    ```bash
    pip install -r requirements.txt

4. Realiza las migraciones de base de datos:
    ```bash
    python manage.py migrate

5. Ejecuta el servidor de desarrollo:
    python manage.py runserver

6. Accede a la aplicación en http://localhost:8000


## Funcionalidades pendientes
- Implementación de paginación para las publicaciones.
- Mejorar el diseño de la página de inicio.
- Agregar sistemas de likes para las publicaciones.