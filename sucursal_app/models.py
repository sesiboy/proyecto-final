from django.db import models

# Create your models here.
class Sucursal(models.Model):
    id_sucursal = models.IntegerField(null=False, primary_key=True)
    nombre = models.CharField(max_length=100, null=False)
    direccion = models.CharField(max_length=100, null=False)
    telefono = models.IntegerField(null=False)
    ciudad = models.CharField(max_length=100, null=False)
    estado = models.CharField(max_length=100,null=False)
    codigo_postal = models.IntegerField(null=False)