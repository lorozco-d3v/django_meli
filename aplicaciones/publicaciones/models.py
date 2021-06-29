from django.db import models
from aplicaciones.seminuevos.models import Seminuevo
from aplicaciones.sucursales.models import Sucursal

class Publicacion(models.Model):
    id = models.AutoField(primary_key=True)
    id_seminuevo = models.ForeignKey(Seminuevo, on_delete=models.CASCADE)
    id_sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE)
    item_meli = models.CharField(max_length=25)
    fecha_publicacion = models.DateTimeField(blank=True, null=True)
    ultima_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_eliminacion = models.DateTimeField(blank=True, null=True)
    category_id = models.CharField(max_length=25)
    listing_type = models.CharField(max_length=25)
