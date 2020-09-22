import psycopg2
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
# Create your views here.

def notas(request):
    return render(request, 'notas.html')

def anadir(request):
    prioridad = request.POST["name_prioridad"]
    titulo = request.POST["nom_titulo"]
    nota = request.POST["name_nota"]

    conn = psycopg2.connect(dbname="capitulo_6_db",
                            user="capitulo_6_user",
                            password="magda321")

    with open("debug.log", "a+") as debug_file:
         print("notas insertadas", file=debug_file)

    cursor = conn.cursor()
    cursor.execute("INSERT INTO nota VALUES ('Alta','Idiomes','7');")
    conn.commit()
    return (HttpResponse(f'Insertado <br>'
                        f'prioridad: {prioridad}<br>'
                         f'titulo: {titulo}<br>'
                         f'nota: {nota}<br>'))

def finish


