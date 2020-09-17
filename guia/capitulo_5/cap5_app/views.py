from django.shortcuts import render

# Create your views here.

import psycopg2
from django.http import HttpResponse
def insert(request):
    conn = psycopg2.connect(dbname="capitulo_4_db",
                            user="capitulo_4_user",
                            password="patata")
    with open("debug.log", "a+") as debug_file:
        print("Funcional!", file=debug_file)
    return HttpResponse("Funciona!")


