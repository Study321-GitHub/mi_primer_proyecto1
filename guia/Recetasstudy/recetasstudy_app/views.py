
from django.shortcuts import render

def recetas(request):
    return render(request, 'recetas.html')

def pizza(request):
    return render(request, 'pizza.html')

def canelons(request):
    return render(request, 'canelons.html')

def gazpacho(request):
    return render(request,'gazpacho.html')

def calabacin(request):
    return render(request, 'florcalabacin.html')

def ensaladillarusa(request):
    return render(request, 'ensaladilla.html')

def carbonaraspecial(request):
    return render(request, 'carbonara.html')

def sopa(request):
    return render(request, 'sopa.html')

def mafespecial(request):
    return render(request, 'mafe.html')

def feijoadaspecial(request):
    return render(request, 'feijoada.html')

def menuinfantil(request):
    return render(request, 'menuinfantil.html')

