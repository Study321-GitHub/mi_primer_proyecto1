import psycopg2
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
# Create your views here.


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
    cursor.execute(f"INSERT INTO nota VALUES ('{prioridad}','{titulo}','{nota}');")

    conn.commit()

    return redirect('notas')

def notas(request):
    conn = psycopg2.connect(dbname="capitulo_6_db",
                            user="capitulo_6_user",
                            password="magda321")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM nota;")
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    params = {'nota': result}
    return render(request, 'notas.html',params)


