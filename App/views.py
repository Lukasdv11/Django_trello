from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User
from .models import Tablero, Lista, Tarea
from .serializers import UserSerializer, TableroSerializer, ListaSerializer, TareaSerializer

def bienvenida(request):
    titulo_app = "TaskBoard - Gestor de Proyectos"
    descripcion_app = "Sistema para la gestión colaborativa de tableros, listas y tarjetas de tareas."
    tableros_activos = 0
    sistema_activo = True
    
    contexto = {
        'titulo': titulo_app,
        'descripcion': descripcion_app,
        'cantidad_tableros': tableros_activos,
        'estado': "Operativo" if sistema_activo else "En Mantenimiento"
    }
    
    return render(request, 'bienvenida.html', contexto)

def error_404(request, exception):
    return render(request, '404.html', status=404)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TableroViewSet(viewsets.ModelViewSet):
    queryset = Tablero.objects.all()
    serializer_class = TableroSerializer

class ListaViewSet(viewsets.ModelViewSet):
    queryset = Lista.objects.all()
    serializer_class = ListaSerializer

class TareaViewSet(viewsets.ModelViewSet):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer