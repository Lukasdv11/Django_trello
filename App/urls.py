from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, TableroViewSet, ListaViewSet, TareaViewSet

router = DefaultRouter()
router.register(r'usuarios', UserViewSet, basename='usuario')
router.register(r'tableros', TableroViewSet, basename='tablero')
router.register(r'listas', ListaViewSet, basename='lista')
router.register(r'tareas', TareaViewSet, basename='tarea')

urlpatterns = [
    path('api/', include(router.urls)),
]