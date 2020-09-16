from django.shortcuts import render
import random

def home_page_view(request):
    return render(request, 'hola_mundo.html')

def magda_view(request):
    parametros = {'numero_favorito': random.randrange(33)}
    return render(request, 'magda.html', parametros)

def today(request):
     return render(request, 'today.html')










