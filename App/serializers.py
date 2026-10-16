from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Tablero, Lista, Tarea

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class TareaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarea
        fields = '__all__'

class ListaSerializer(serializers.ModelSerializer):
    tareas = TareaSerializer(many=True, read_only=True)

    class Meta:
        model = Lista
        fields = '__all__'

class TableroSerializer(serializers.ModelSerializer):
    listas = ListaSerializer(many=True, read_only=True)

    class Meta:
        model = Tablero
        fields = '__all__'