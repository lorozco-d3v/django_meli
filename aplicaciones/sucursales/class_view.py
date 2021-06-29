from django.shortcuts import render,redirect
from django.views.generic import CreateView,DeleteView,ListView,UpdateView
from django.urls import reverse_lazy
from .models import Sucursal

class SucursalList(ListView):
    model = Sucursal
    template_name = 'sucursal.html'