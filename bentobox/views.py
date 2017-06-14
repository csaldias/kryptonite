from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User

from .models import Contenido

def index(request):
    #El index debiera ser el search page.
    #Si no está logeado, que se inicie sesión.
    return render(request, 'bentobox/login.html')

def register(request):
    if request.POST:
        #TODO: Register process
        nombre_usuario = request.POST['user']
        contrasena = request.POST['pass']
        nombre = request.POST['name']
        tipo = request.POST['tipo']

        user = User.objects.create_user(nombre_usuario, 'a@a.com', contrasena)
        user.first_name = nombre
        user.categoria.tipo_aprendizaje = tipo
        user.save()

        print(request.POST)

    tipos_contenido = (
    ('ad', 'Adaptador'),
    ('di', 'Divergente'),
    ('co', 'Convergente'),
    ('as', 'Asimilador'),
    )
    context = {'tipos': tipos_contenido}
    return render(request, 'bentobox/register.html', context)

def login(request):
    if request.POST:
        #TODO: Login process
        print(request.POST)

    return render(request, 'bentobox/login.html')


def searchPage(request):
    tipos_contenido = (
    ('ad', 'Adaptador'),
    ('di', 'Divergente'),
    ('co', 'Convergente'),
    ('as', 'Asimilador'),
    )
    context = {'tipos': tipos_contenido}
    return render(request, 'bentobox/search.html', context)

def searchResults(request):
    search_query = request.POST["search_query"]
    tipo_user = request.POST["tipo"]

    #Aquí va la lógica de searchRank
    results = []
    contenidos = Contenido.objects.filter(aprobado=1)
    for contenido in contenidos:
        num_match = 0
        tags = contenido.tags.split(",")
        #Cuantas keywords de la query coinciden con las keywords del archivo?
        for word in (search_query.split(" ")):
            num_match += tags.count(word)

        #Calculamos el ptje del archivo
        accuracy = num_match / len(tags)
        if tipo_user == "ad":
            file_score = round(accuracy * contenido.clasificacion_adaptador, 3)
        elif tipo_user == "di":
            file_score = round(accuracy * contenido.clasificacion_divergente, 3)
        elif tipo_user == "co":
            file_score = round(accuracy * contenido.clasificacion_convergente, 3)
        elif tipo_user == "as":
            file_score = round(accuracy * contenido.clasificacion_asimilador, 3)

        results.append( (file_score, contenido.link, contenido.descripcion) )

    #Ordenamos los resultados por puntaje desdendente, de esta forma los
    #resultados másrelevantes para el usuario se mostrarán primero.
    results.sort(key=lambda x: x[0], reverse=True)

    context = {
        'search_query': search_query,
        'tipo': tipo_user,
        'resultados': results
        }
    return render(request, 'bentobox/results.html', context)
