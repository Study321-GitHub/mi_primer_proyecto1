from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'notas.html')

def añadir(request):
    return  render(request, 'añadir.html')
