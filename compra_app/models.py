from django.db import models

# Create your models here.
class Compra(models.Model):
    id_compra = models.IntegerField(null=False, primary_key=True)
    cantidad = models.IntegerField(null=False)
    fecha_compra = models.DateField(null=False)
    forma_pago = models.CharField(max_length=100,null=False)
    total = models.IntegerField(null=False)
    id_producto = models.IntegerField(null=False)
    id_encargo = models.IntegerField(null=False)