from django.shortcuts import render
import psycopg2
from django.http import HttpResponse
#def insert(request):
 #   conn = psycopg2.connect(dbname="capitulo_4_db",
  #                          user="capitulo_4_user",
   #                         password="patata")

    #with open("debug.log", "a+") as debug_file:
    #print("Funciona!", file=debug_file)
    #return HttpResponse("Funciona!")

    #cursor = conn.cursor()
    #cursor.execute("INSERT INTO emp VALUES ('7364','HUGO','OFICINISTA',\
    #              '7903', DATE '1980-12-17','800.00',NULL,'20');")

    #return HttpResponse('Registro insertado!!!')

    #exercici insertar select para comprobar que inserta registres
    #cursor.execute("select * from emp")
    #return HttpResponse(cursor.fetchall())
# ---------------------------------------------------------------------------------------------
def insert(request):
    conn = psycopg2.connect(dbname="capitulo_4_db",
                            user="capitulo_4_user",
                            password="patata")
    cursor = conn.cursor()
    return HttpResponse("Insertado")
#def select(request):
def consultar(request):
    conn = psycopg2.connect(dbname="capitulo_4_db",
                            user="capitulo_4_user",
                            password="patata")
    cursor = conn.cursor()
    cursor.execute("select * from emp")
    return HttpResponse(cursor.fetchall())



