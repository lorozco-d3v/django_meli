from django.db import models

class Seminuevo(models.Model):
    id = models.AutoField(primary_key=True)
    vin = models.CharField(max_length=20)
    num_inv1 = models.IntegerField()
    num_inv2 = models.IntegerField()
    anio = models.IntegerField()
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=100)
    version = models.CharField(max_length=200)
    tipo = models.CharField(max_length=30)
    color_ext = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=100)
    kilometraje = models.IntegerField()
    transmision = models.CharField(max_length=20)
    precio = models.IntegerField()
    extra = models.CharField(max_length=1000, blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    eliminado = models.BooleanField(default=False)
    combustible = models.CharField(max_length=20)
    direccion = models.CharField(max_length=20)
    puertas = models.IntegerField()

    def __str__(self):
        return self.vin