from django.db import models

# Create your models here.
class Venta(models.Model):
    id_venta = models.IntegerField(null=False, primary_key=True)
    id_empleado = models.IntegerField(null=False)
    id_cliente = models.IntegerField(null=False)
    id_producto = models.IntegerField(null=False)
    id_sucursal = models.IntegerField(null=False)
    fecha = models.DateField(null=False)
    total = models.IntegerField(null=False)