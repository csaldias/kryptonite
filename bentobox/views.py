from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from bentobox.models import Contenido
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

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

        return render(request, 'bentobox/login.html', {'msg': 'Registro exitoso.'})

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
        user = request.POST['user']
        passwd = request.POST['pass']

        user = authenticate(request, username=user, password=passwd)
        if user is not None:
            auth_login(request, user)
            return redirect('bentobox:search')
        else:
            return render(request, 'bentobox/login.html', {'msg': 'Usuario o contraseña inválidos.'})
    return render(request, 'bentobox/login.html')

def logout(request):
    auth_logout(request)
    return redirect('bentobox:login')

def searchPage(request):
    if request.user.is_authenticated:
        #El usuario está autenticado
        tipos_contenido = (
        ('ad', 'Adaptador'),
        ('di', 'Divergente'),
        ('co', 'Convergente'),
        ('as', 'Asimilador'),
        )

        for tipo_ab, tipo_str in tipos_contenido:
            if tipo_ab == request.user.categoria.tipo_aprendizaje:
                tipo_user = tipo_str

        context = {'tipos': tipos_contenido,'tipo_user': tipo_user}
        return render(request, 'bentobox/search2.html', context)
    else:
        #El usuario NO está autenticado
        return redirect('bentobox:login')

def searchResults(request):
    search_query = request.POST["search_query"]
    tipo_user = request.user.categoria.tipo_aprendizaje

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

        if file_score > 0: results.append( (file_score, contenido.link, contenido.descripcion) )

    #Ordenamos los resultados por puntaje desdendente, de esta forma los
    #resultados más relevantes para el usuario se mostrarán primero.
    results.sort(key=lambda x: x[0], reverse=True)

    context = {
        'search_query': search_query,
        'tipo': tipo_user,
        'resultados': results
        }
    return render(request, 'bentobox/results2.html', context)

def sugerirContenido(request):
    if request.POST:
        #Agregamos el contenido sin aprobar
        link = request.POST['link']
        descripcion = request.POST['descripcion']
        tags = request.POST['tags']

        contenido = Contenido(link=link, descripcion=descripcion, tags=tags, aprobado=False)
        contenido.save()

        tipos_contenido = (
        ('ad', 'Adaptador'),
        ('di', 'Divergente'),
        ('co', 'Convergente'),
        ('as', 'Asimilador'),
        )

        for tipo_ab, tipo_str in tipos_contenido:
            if tipo_ab == request.user.categoria.tipo_aprendizaje:
                tipo_user = tipo_str

        return render(request, 'bentobox/search2.html',
            {'msg': 'Contenido enviado! Tu contenido será revisado antes de ser aceptado en el sitio.',
             'tipos': tipos_contenido, 'tipo_user': tipo_user})

    return render(request, 'bentobox/dialog.html')
