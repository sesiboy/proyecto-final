from django.db import models

# Create your models here.
class Distribuidor(models.Model):
    id_distribuidor = models.IntegerField(null=False, primary_key=True)
    nombre = models.CharField(max_length=100, null=False)
    telefono = models.IntegerField(null=False)
    direccion = models.CharField(max_length=100, null=False)
    ciudad = models.CharField(max_length=100, null=False)
    estado = models.CharField(max_length=100,null=False)
    productos_distribuidos = models.CharField(max_length=1000,null=False)