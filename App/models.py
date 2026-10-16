from django.db import models
from django.contrib.auth.models import User

class Tablero(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    creador = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tableros')
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

class Lista(models.Model):
    nombre = models.CharField(max_length=100)
    orden = models.PositiveIntegerField(default=0)
    tablero = models.ForeignKey(Tablero, on_delete=models.CASCADE, related_name='listas')

    class Meta:
        ordering = ['orden']

    def __str__(self):
        return f"{self.nombre} ({self.tablero.titulo})"

class Tarea(models.Model):
    titulo = models.CharField(max_length=150)
    descripcion = models.TextField(blank=True, null=True)
    completada = models.BooleanField(default=False)
    fecha_limite = models.DateField(blank=True, null=True)
    lista = models.ForeignKey(Lista, on_delete=models.CASCADE, related_name='tareas')
    asignado_a = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='tareas_asignadas')
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo