from django.shortcuts import render,redirect
from django.views.generic import CreateView,DeleteView,ListView,UpdateView
from django.urls import reverse_lazy
from .models import Publicacion

class PublicacionList(ListView):
    model = Publicacion
    template_name = 'publicacion.html'