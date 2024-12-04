from django.db import models

# Create your models here.
class Producto(models.Model):
    id_producto = models.IntegerField(null=False, primary_key=True)
    nombre = models.CharField(max_length=100, null=False)
    categoria = models.CharField(max_length=100,null=False)
    precio = models.IntegerField(null=False)
    cantidad_disponible = models.IntegerField(null=False)
    fecha_vencimiento = models.DateField(null=False)
    id_distribuidor = models.IntegerField(null=False)
    id_sucursal= models.IntegerField(null=False)