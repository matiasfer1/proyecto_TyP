from django.urls import path
from .views import agregar_nombre, eliminar_nombre,editar_nombre, eliminar_todos_nombres, sortear

urlpatterns = [
    path('home/', agregar_nombre, name='home'),
    path('eliminar_nombre/<int:nombre_id>/', eliminar_nombre, name='eliminar_nombre'),
    path('editar_nombre/<int:nombre_id>/', editar_nombre, name='editar_nombre'),
    path('eliminar_todos_nombres/', eliminar_todos_nombres, name='eliminar_todos_nombres'),
    path('sortear/', sortear, name='sortear'),
]

