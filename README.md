# Proyect 1: Wiki

¡Bienvenido a Wiki! Aquí encontrarás una descripción detallada del proyecto y las instrucciones para ejecutar la aplicación en tu entorno local.

## Descripción del Proyecto

Bienvenido a Wiki, una enciclopedia en línea diseñada para proporcionar información de manera accesible mediante el uso del lenguaje de marcado Markdown.

### Características Principales

1. **Página de Entrada:**
   - Al visitar `/wiki/TITLE`, donde `TITLE` es el título de una entrada, se muestra una página que presenta el contenido de esa entrada de enciclopedia.
   - Si la entrada no existe, se muestra un mensaje indicando que la página solicitada no se encuentra.

2. **Página de Índice:**
   - La página de índice muestra una lista de todas las entradas de la enciclopedia, permitiendo a los usuarios hacer clic en el nombre de cualquier entrada para acceder directamente a esa página.

3. **Búsqueda:**
   - Los usuarios pueden buscar una entrada de la enciclopedia escribiendo una consulta en el cuadro de búsqueda.
   - Si la consulta coincide con el nombre de una entrada, el usuario es redirigido a la página de esa entrada.
   - Si la consulta no coincide, se muestra una página de resultados de búsqueda con entradas que contienen la consulta como subcadena.

4. **Nueva Página:**
   - Los usuarios pueden crear una nueva entrada de enciclopedia al hacer clic en "Crear nueva página".
   - Al ingresar un título y el contenido en formato Markdown, la nueva entrada se guarda y se muestra al usuario.

5. **Editar Página:**
   - En cada página de entrada, el usuario puede hacer clic en un enlace para ir a una página donde puede editar el contenido de Markdown de esa entrada.
   - El contenido existente se muestra en un área de texto, y los cambios se guardan al hacer clic en un botón.

6. **Página Aleatoria:**
   - Al hacer clic en "Página aleatoria," el usuario accede a una entrada de enciclopedia seleccionada al azar.

## Video tutorial

   **Youtube**: "Próximamente"

## Estructura de Archivos de la Aplicación

- **encyclopedia/**: Esta carpeta alberga la aplicación de Django, configurada como un módulo. La ejecución se realiza desde la ruta raíz a través del archivo `manage.py`.

- **templates/**: Aquí se encuentran las plantillas HTML que posibilitan la visualización del contenido de la aplicación.

- **static/**: Contiene archivos estáticos, como hojas de estilo CSS, fuentes y otros recursos utilizados en las plantillas HTML.

## Archivos del Proyecto

- **wiki/**: Carpeta que contiene el proyecto principal de Django, responsable de gestionar la aplicación "Wiki".

### Implementación Técnica

- La aplicación no requiere de una base de datos, por ende no necesitarás generar migraciones antes de la ejecución.
- La carpeta entries almacenará los ficheros de extensión markdown, que servirán para mostrar información en las plantillas HTML.
- El archivo 'util.py' se encarga de la gestión de los ficheros markdown.

## Instrucciones para Desarrolladores

1. **Configuración del Entorno:**
   - Clona este repositorio.
   - Configura un entorno virtual y activa.

```bash
python -m venv venv
source venv/bin/activate  # En sistemas basados en Unix
venv\Scripts\activate  # En Windows
```

2. **Instalación de Dependencias:**
   - Instala las dependencias necesarias.

```bash
pip install -r requirements.txt
```

3. **Acceso a la Aplicación:**
   - Abre tu navegador y accede a `http://localhost:8000` para utilizar la aplicación.

¡Esperamos que disfrutes utilizando Wiki! Si tienes alguna pregunta o necesitas más información, no dudes en contactarme.

## Hecho por: Carlos Adrián Espinosa Luna.