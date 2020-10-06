import psycopg2
import psycopg2.extras
from django.shortcuts import render
from django.shortcuts import redirect
#from django.http import HttpResponse


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
    cursor.execute(f"INSERT INTO notas VALUES ('{prioridad}','{titulo}','{nota}');")

    conn.commit()

    return redirect('home')

#en ex. vista_principal
def notas(request):
    conn = psycopg2.connect(dbname="capitulo_6_db",
                            user="capitulo_6_user",
                            password="magda321")
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    prioridad = request.GET.get('get_prioridad', default='%')
    if prioridad == 'todas':
        prioridad = '%'
    cursor.execute(F"SELECT * FROM notas WHERE prioridad LIKE '{prioridad}';")

    result = cursor.fetchall()
  # conn.commit() no es necesari en aquest cas; commit=guardar
    cursor.close()
    conn.close()
    params = {'notas': result}
    return render(request, 'notas.html',params)




