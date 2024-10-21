from django.shortcuts import render, redirect, get_object_or_404
from .models import Nombre, Sorteo
import random
from datetime import datetime
from django.db import connection
from django.http import JsonResponse


def agregar_nombre(request):
    #Si el metodo del boton es POST
    if request.method == 'POST':
        #asigna el contenido de la celda a la funcion POST del metodo request
        nombre = request.POST['nombre']
        #Crea el objeto nombre en el field ¨nombre¨de la bd
        Nombre.objects.create(nombre=nombre)
        # Redirige para limpiar el formulario después de agregar
        return redirect('home') 
    #Popula la variable nombres con toda la info de la bd para desplegar la lista 
    nombres = Nombre.objects.all()
    #refresca la pagina con la info nueva de ¨nombres"
    date = datetime.now()
    print(date)
    return render(request, 'home.html', {'nombres': nombres, 'fecha':date})

def editar_nombre(request, nombre_id):
    if request.method == 'POST':
        nuevo_nombre = request.POST.get('nuevo_nombre')
        
        print("Nombre ID:", nombre_id)  # Agrega esta línea para depuración
        
        nombre = get_object_or_404(Nombre, id=nombre_id)
        nombre.nombre = nuevo_nombre
        nombre.save()
        
    return redirect('home')

def eliminar_nombre(request, nombre_id):
    nombre = get_object_or_404(Nombre, id=nombre_id)
    if request.method == 'POST':
        nombre.delete()
    return redirect('home')

def eliminar_todos_nombres(request):
    if request.method == 'POST':
        Nombre.objects.all().delete()
    return redirect('home')

def sortear_equipos():
    lista = list(Nombre.objects.values_list('nombre', flat=True))
    random.shuffle(lista)  # Usamos shuffle para mezclar la lista aleatoriamente
    return lista

def sortear(request):
    if request.method == 'POST':
        Sorteo.objects.all().delete()
        with connection.cursor() as cursor:
            cursor.execute("ALTER TABLE app_sorteo AUTO_INCREMENT = 1")
        lista = sortear_equipos()  # Llamamos a la función para obtener la lista mezclada
        for x in range(0, len(lista)):
            value = Sorteo(nombre=lista[x])
            value.save()
        return JsonResponse({'lista': lista})  # Devolvemos la lista como respuesta JSON

    return redirect('home')

