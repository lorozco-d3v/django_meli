from django.shortcuts import render,redirect
from .models import Seminuevo
from .forms import SeminuevoForm

#Vistas basadas en funciones
def inicio(request):
    seminuevos = Seminuevo.objects.all()
    contexto = {
        'seminuevos':seminuevos
    }
    return render(request, 'index.html',contexto)

def crearSeminuevo(request):
    if request.method == 'GET':
        form = SeminuevoForm()
        contexto = {
            'form': form
        }
    else:
        form = SeminuevoForm(request.POST)
        contexto = {
            'form': form
        }
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'crear_seminuevo.html', contexto)

def editarSeminuevo(request,id):
    seminuevo = Seminuevo.objects.get(id = id)
    if(request.method == 'GET'):
        form = SeminuevoForm(instance = seminuevo)
        contexto = {
            'form':form
        }
    else:
        form = SeminuevoForm(request.POST, instance = seminuevo)
        contexto = {
            'form':form
        }
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'crear_seminuevo.html', contexto)

def eliminarSeminuevo(request,id):
    seminuevo = Seminuevo.objects.get(id = id)
    seminuevo.delete()
    return redirect('index')

#Vistas basadas en clases