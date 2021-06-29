"""proyecto_ml URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from aplicaciones.seminuevos.views import inicio,crearSeminuevo,editarSeminuevo,eliminarSeminuevo
from aplicaciones.seminuevos.class_view import SeminuevoList,SeminuevoCreate,SeminuevoUpdate,SeminuevoDelete
from aplicaciones.sucursales.class_view import SucursalList
from aplicaciones.sucursales.views import login,redirect
from aplicaciones.publicaciones.class_view import PublicacionList

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', inicio, name='index'),   vista basada en funciones
    path('', SeminuevoList.as_view(), name='index'),
    #path('crear_seminuevo/', crearSeminuevo,name='crear_semminuevo'),
    path('crear_seminuevo/', SeminuevoCreate.as_view(),name='crear_seminuevo'),
    #path('editar_persona/<int:id>', editarSeminuevo,name='editar_seminuevo'),
    path('editar_persona/<int:pk>', SeminuevoUpdate.as_view(),name='editar_seminuevo'),
    #path('eliminar_persona/<int:id>', eliminarSeminuevo,name='eliminar_seminuevo'),
    path('eliminar_persona/<int:pk>', SeminuevoDelete.as_view(),name='eliminar_seminuevo'),
    path('sucursales/', SucursalList.as_view(), name='sucursal'),
    path('publicaciones/', PublicacionList.as_view(), name='publicacion'),
    path('login/', login, name='login'),
    path('redirect', redirect, name='redirect'),
]
