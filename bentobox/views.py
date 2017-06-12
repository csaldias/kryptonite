from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Este es el index de bentobox.")

def searchPage(request):
    return HttpResponse("Este es la página del buscador.")

def searchResults(request):
    return HttpResponse("Esta es la interfaz de resutlados de searchRank.")
