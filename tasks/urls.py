from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('crear_usuario/', views.crear_usuario, name='crear_usuario'),
    path('cerrar_sesion/', views.cerrar_sesion, name='cerrar_sesion'),
    path('iniciar_sesion/', views.iniciar_sesion, name='iniciar_sesion'),
    path('tareas/', views.tareas, name='tareas'),
    path('tareas/crear/', views.crear_tarea, name='crear_tarea'),
    path('tareas/<int:id>/', views.mostrar_tarea, name='mostrar_tarea'),
    path('tareas/<int:id>/delete', views.borrar_tarea, name='borrar_tarea')
]