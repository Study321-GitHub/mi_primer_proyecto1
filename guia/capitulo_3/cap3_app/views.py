
from django.shortcuts import render
import random

def hola(request):
  return render (request, 'home.html')
