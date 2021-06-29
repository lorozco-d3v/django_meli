from django.shortcuts import render,redirect
from django.views.generic import CreateView,DeleteView,ListView,UpdateView
from django.urls import reverse_lazy
from .forms import SeminuevoForm
from .models import Seminuevo

class SeminuevoList(ListView):
    model = Seminuevo
    template_name = 'index.html'

    #def get_queryset(self):        Redefinir la función
        #return self.model.objects.filter()
        #return self.model.objects.all()[:2]

class SeminuevoCreate(CreateView):
    model = Seminuevo
    form_class = SeminuevoForm
    template_name = 'crear_seminuevo.html'
    success_url = reverse_lazy('index')

class SeminuevoUpdate(UpdateView):
    model = Seminuevo
    form_class = SeminuevoForm
    template_name = 'crear_seminuevo.html'
    success_url = reverse_lazy('index')

class SeminuevoDelete(DeleteView):
    model = Seminuevo
    template_name = 'verificacion.html'
    success_url = reverse_lazy('index')

