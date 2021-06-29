from django.db import models

class Sucursal(models.Model):
    id = models.AutoField(primary_key=True)
    id_ag = models.IntegerField()
    nom = models.CharField(max_length=100)
    meli_token = models.CharField(max_length=100, blank=True, null=True)
    meli_refresh_token = models.CharField(max_length=50, blank=True, null=True)
    expiration_token_date = models.CharField(max_length=15, blank=True, null=True)
    last_token_update = models.DateTimeField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    eliminado = models.BooleanField(default=False)
