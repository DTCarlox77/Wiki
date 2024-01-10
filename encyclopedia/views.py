from django.shortcuts import render, redirect
from django.views.defaults import page_not_found
from django.http import Http404
from .util import list_entries, save_entry, get_entry
import markdown2
import random

# Página principal que muestra todos los artículos diponibles.
def index(request):
    entries = list_entries()
    
    # Serialización de los datos para mostrar de una mejor forma las páginas disponibles.
    grouped_entries = {}
    for entry in entries:
        first_letter = entry[0].upper()
        if first_letter not in grouped_entries:
            grouped_entries[first_letter] = []
        grouped_entries[first_letter].append(entry)

    return render(request, "encyclopedia/index.html", {
        "grouped_entries": grouped_entries
    })

# Búsqueda del formulario de búsqueda.
def search_form(request):
    resultados = None
    entries = list_entries()
    
    # Método para la búsqueda de información en Wiki.
    if request.method == 'GET':
        search = request.GET.get('q')
        
        if not search:
            return redirect('index')
        else:
            # Si la búsqueda existe, redirige al artículo.
            if search in entries:
                return redirect('search', query=search)
            
            # Sino, busca posibles coincidencias, si encuentra las retorna.
            else:
                resultados = []
                for entrie in entries:
                    if search in entrie:
                        resultados.append(entrie)
    
    return render(request, 'encyclopedia/search.html', {
        'busqueda' : search,
        'resultados' : resultados
    })

# Búsqueda exacta de un elemento.
def search(request, query):
    
    # Conversión del markdown a HTML.
    busqueda = get_entry(query)
    
    if busqueda:
        html = markdown2.markdown(busqueda)
        
        return render(request, 'encyclopedia/page.html', {
            'titulo' : query,
            'contenido' : html
        })
    
    raise Http404('')
    
# Edición de páginas posteadas.
def edit_page(request, name):
    contenido = get_entry(name)
    
    return render(request, 'encyclopedia/edit.html', {
        'titulo': name,
        'contenido': contenido,
        'edicion' : True
    })

# Almacén de cambios por edición.
def save_edit(request, name):
    titulos = list_entries()
    mensaje = None
    titulo = name
    contenido = get_entry(name)

    # Envío del formulario.
    if request.method == 'POST':
        contenido_formulario = request.POST.get('content')

        # Validaciones previas al envío del formulario.
        if not contenido_formulario:
            mensaje = 'Error: No puedes dejar campos vacíos.'
            
        elif titulo not in titulos:
            mensaje = 'Error: El documento no existe.'
            
        elif contenido == contenido_formulario:
            mensaje = 'Error: No has hecho modificaciones.'
            
        else:
            # Evita los errores de sobrecarga de espacios en el textarea.
            contenido_formulario = contenido_formulario.replace('\r\n', '\n').replace('\r', '\n')
            
            # Almacena el nuevo archivo en caso de tener un título disponible.
            save_entry(titulo, contenido_formulario)
            # Redirige al usuario a la nueva página.
            return redirect('search', query=titulo)

    return render(request, 'encyclopedia/edit.html', {
        'mensaje': mensaje,
        'titulo': titulo,
        'contenido': contenido,
        'edicion' : True
    })

# Formulario para la creación de un artículo.
def create_page(request):
    titulos = list_entries()
    mensaje = None
    titulo = None
    contenido = None

    # Envío del formulario.
    if request.method == 'POST':
        titulo = request.POST.get('title')
        contenido = request.POST.get('content')

        # Validaciones antes de almacenar el artículo.
        if not titulo or not contenido:
            mensaje = 'Error: No puedes dejar campos vacíos.'
            
        elif titulo in titulos:
            mensaje = 'Error: El título ingresado ya está en uso.'
            
        else:
            # Almacena el nuevo archivo en caso de tener un título disponible.
            save_entry(titulo, contenido)
            # Redirige al usuario a la nueva página.
            return redirect('search', query=titulo)

    return render(request, 'encyclopedia/edit.html', {
        'mensaje': mensaje,
        'titulo': titulo,
        'contenido': contenido,
        'edicion' : False
    })

# Genera un número aleatorio en función del tamaño de elementos para mandar a una página aleatória.
def random_page(request):
    titulos = list_entries()
    numero = random.randint(0, len(titulos) - 1)
    
    return redirect('search', query=titulos[numero])

# Página de not found.
def error_404(request, exception):
    return page_not_found(request, '404.html')