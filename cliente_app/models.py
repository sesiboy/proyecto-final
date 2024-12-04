from django.db import models

# Create your models here.
class Cliente(models.Model):
    id_cliente = models.IntegerField(null=False, primary_key=True)
    nombre = models.CharField(max_length=100, null=False)
    correo = models.EmailField(max_length=100, null=False)
    telefono = models.IntegerField(null=False)
    direccion = models.CharField(max_length=100, null=False)
    ciudad = models.CharField(max_length=100, null=False)
    estado = models.CharField(max_length=100,null=False)