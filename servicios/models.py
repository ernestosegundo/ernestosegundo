from django.db import models

# Create your models here.
class CategoriaServicio(models.Model):
    pass

class Servicio(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=250)
    disponibilidad = models.BooleanField(default=True)
    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now_add=True)