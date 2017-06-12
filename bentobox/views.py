from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Este es el index de bentobox.")

def searchPage(request):
    tipos_contenido = (
    ('sd', 'Sin Definir'),
    ('ad', 'Adaptador'),
    ('di', 'Divergente'),
    ('co', 'Convergente'),
    ('as', 'Asimilador'),
    )
    context = {'tipos': tipos_contenido}
    return render(request, 'bentobox/search.html', context)

def searchResults(request):

    context = {'search_query': request.POST["search_query"], 'tipo': request.POST["tipo"]}
    return render(request, 'bentobox/results.html', context)
