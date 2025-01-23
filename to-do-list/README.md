# Lista de Tareas (To-Do List)

## Descripción
Este proyecto es una aplicación web para gestionar tareas, creada con el framework Django. Permite a los usuarios llevar un control de sus actividades mediante las funcionalidades de:
- Agregar nuevas tareas.
- Editar tareas existentes.
- Marcar tareas como completadas o pendientes.
- Eliminar tareas.

El diseño de la aplicación es moderno y responsivo, asegurando una excelente experiencia de usuario tanto en dispositivos móviles como en pantallas grandes.

## Características
- **Frontend**: Diseño responsivo implementado con Bootstrap para garantizar una interfaz limpia y moderna.
- **Backend**: Desarrollado con Django, utilizando vistas basadas en funciones (FBV).
- **Base de datos**: Gestor de base de datos predeterminado de Django (SQLite).

### Funcionalidades principales
1. **Listar tareas**: Muestra todas las tareas en una tabla, indicando su estado (completada o pendiente).
2. **Agregar tarea**: Formulario para crear una nueva tarea.
3. **Editar tarea**: Permite modificar el título, descripción y estado de una tarea.
4. **Eliminar tarea**: Opción para eliminar tareas de la lista.

## Instalación y configuración
1. Clona este repositorio:
   ```bash
   git clone <URL-del-repositorio>
   cd <nombre-del-proyecto>
   ```

2. Crea un entorno virtual e instálalo:
   ```bash
   python -m venv env
   source env/bin/activate # En Windows: env\Scripts\activate
   pip install -r requirements.txt
   ```

3. Realiza las migraciones:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. Inicia el servidor:
   ```bash
   python manage.py runserver
   ```

5. Accede a la aplicación desde tu navegador en `http://127.0.0.1:8000/`.

## Tecnologías utilizadas
- **Django**: Framework web para el backend.
- **CSS**: Para el diseño responsivo.
- **SQLite**: Base de datos predeterminada de Django.

## Mejoras futuras
- Agregar autenticación de usuarios para que cada usuario tenga su propia lista de tareas.
- Implementar categorías o etiquetas para las tareas.
- Integrar API REST para acceso externo a los datos.

## Autor
Desarrollado por Nelson Rojas Camones.

