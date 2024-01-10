from django.shortcuts import render, redirect
from .util import list_entries, save_entry, get_entry
import markdown2
import random

def index(request):
    entries = list_entries()
    
    grouped_entries = {}
    for entry in entries:
        first_letter = entry[0].upper()
        if first_letter not in grouped_entries:
            grouped_entries[first_letter] = []
        grouped_entries[first_letter].append(entry)

    print(grouped_entries)  # Imprime el contenido en la consola de la vista

    return render(request, "encyclopedia/index.html", {
        "grouped_entries": grouped_entries
    })



def search(request, query):
    
    busqueda = get_entry(query)
    html = markdown2.markdown(busqueda)
    
    print(busqueda)
    
    return render(request, 'encyclopedia/page.html', {
        'titulo' : query,
        'contenido' : html
    })
    
def edit_page(request, name):
    contenido = get_entry(name)
    
    return render(request, 'encyclopedia/edit.html', {
        'titulo': name,
        'contenido': contenido,
        'edicion' : True
    })
    
def save_edit(request, name):
    titulos = list_entries()
    mensaje = None
    titulo = name
    contenido = get_entry(name)

    # Envío del formulario.
    if request.method == 'POST':
        contenido_formulario = request.POST.get('content')

        if not contenido_formulario:
            mensaje = 'Error: No puedes dejar campos vacíos.'
        elif titulo not in titulos:
            mensaje = 'Error: El documento no existe.'
        elif contenido == contenido_formulario:
            mensaje = 'Error: No has hecho modificaciones.'
        else:
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

def create_page(request):
    titulos = list_entries()
    mensaje = None
    titulo = None
    contenido = None

    # Envío del formulario.
    if request.method == 'POST':
        titulo = request.POST.get('title')
        contenido = request.POST.get('content')

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

def random_page(request):
    titulos = list_entries()
    numero = random.randint(0, len(titulos) - 1)
    
    return redirect('search', query=titulos[numero])