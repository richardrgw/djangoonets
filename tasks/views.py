from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import TareaForm
from .models import Tarea
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):
    return render(request, 'home.html')


def crear_usuario(request):
    if (request.method == 'GET'):
        return render(request, 'usuario/crear_usuario.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('tareas')
            except IntegrityError:
                return render(request, 'usuario/crear_usuario.html', {
                    'form': UserCreationForm,
                    'error': 'Usuario ya existe'
                })
        return render(request, 'usuario/crear_usuario.html', {
            'form': UserCreationForm,
            'error': 'Password no coincide'
        })

@login_required
def cerrar_sesion(request):
    logout(request)
    return redirect('home')


def iniciar_sesion(request):
    if (request.method == 'GET'):
        return render(request, 'usuario/iniciar_sesion.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'usuario/iniciar_sesion.html', {
                'form': AuthenticationForm,
                'error': 'Usuario o Password incorrecto'
            })
        else:
            login(request, user)
            return redirect('tareas')

@login_required
def crear_tarea(request):
    if request.method == 'GET':
        return render(request, 'tarea/crear_tarea.html', {
            'form': TareaForm
        })
    else:
        try:
            form = TareaForm(request.POST)
            tareaNueva = form.save(commit=False)
            tareaNueva.usuario = request.user
            tareaNueva.save()
            return redirect('tareas')
        except ValueError:
            return render(request, 'tarea/crear_tarea.html', {
                'form': TareaForm,
                'error': 'Por favor coloque datos validos'
            })

@login_required
def tareas(request):
    tareas = Tarea.objects.filter(usuario=request.user)
    return render(request, 'tarea/tareas.html', {
        'tareas': tareas
    })

@login_required
def mostrar_tarea(request, id):
    if request.method == 'GET':
        tarea = get_object_or_404(Tarea, pk=id, usuario=request.user)
        form = TareaForm(instance=tarea)
        return render(request, 'tarea/tarea_detalle.html', {
            'tarea': tarea,
            'form': form
        })
    else:
        try:
            tarea = get_object_or_404(Tarea, pk=id, usuario=request.user)
            form = TareaForm(request.POST, instance=tarea)
            form.save()
            return redirect('tareas')
        except ValueError:
            return render(request, 'tarea/tarea_detalle.html', {
            'tarea': tarea,
            'form': form,
            'error': 'Error actualizando'
        })
@login_required
def borrar_tarea(request, id):
    tarea = get_object_or_404(Tarea, pk=id, usuario=request.user)
    if request.method == 'POST':
        tarea.delete()
        return redirect('tareas')