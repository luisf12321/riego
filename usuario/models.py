import datetime

from djongo import models
from datetime import datetime
# Create your models here.


class Usuarios(models.Model):
    id = models.ObjectIdField
    nombre = models.CharField(max_length=25,null=False)
    apellido = models.CharField(max_length=20,null=False)
    numero_identificacion = models.IntegerField()
    celular = models.IntegerField()
    direccion = models.CharField(max_length=25, null=True)

class riego(models.Model):
    id = models.ObjectIdField
    cantidad_agua_cal = models.IntegerField
    cantidad_agua_apli = models.IntegerField
    fecha = models.DateField(auto_now_add=True)
    hora = models.DateTimeField(auto_now=True)
    estado = models.CharField



