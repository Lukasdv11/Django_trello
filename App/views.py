from django.shortcuts import render

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