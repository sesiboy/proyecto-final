from django.db import models

# Create your models here.
class Empleados(models.Model):
    ID_empleado = models.PositiveBigIntegerField(null=False, primary_key=True)
    Nombre = models.CharField(max_length=50, null=False)
    Puesto = models.CharField(max_length=50,null=False)
    Sueldo = models.PositiveBigIntegerField(null=False)
    Telefono = models.PositiveBigIntegerField(null=False)
    Fecha_nac = models.DateField(null=False)
    Genero = models.CharField(max_length=50,null=False)

    def __str__(self):
        return self.Nombre