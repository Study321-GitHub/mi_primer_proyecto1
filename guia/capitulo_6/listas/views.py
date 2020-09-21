from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def notas(request):
    return render(request, 'notas.html')

#def anadir(request):
 #   return HttpResponse("anadir")

def anadir(request):
    prioridad = request.POST["name_prioridad"]
    titulo = request.POST["nom_titulo"]
    nota = request.POST["name_nota"]
    return (HttpResponse(f'Insertado <br>'
                         f'prioridad: {prioridad}<br>'
                         f'titulo: {titulo}<br>'
                         f'nota: {nota}<br>'))



