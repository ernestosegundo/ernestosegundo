from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class CategoriaServicio(models.Model):
    nombre = models.CharField(max_length=50)
    disponibilidad = models.BooleanField(default=True)
    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Categoría de servicio"
        verbose_name_plural = "Categorías de servicio"
    
    def __str__(self):
        return self.nombre

class Servicio(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=250)
    disponibilidad = models.BooleanField(default=True)
    precio = models.FloatField()
    categoria = models.ForeignKey(CategoriaServicio, on_delete=CASCADE)
    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Servicio"
        verbose_name_plural = "Servicios"
    
    def __str__(self):
        return self.nombre