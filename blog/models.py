from django.db import models
from django.contrib.auth.models import User

from tinymce.models import HTMLField

# Create your models here.
class CategoriaPost(models.Model):
    nombre = models.CharField(max_length=50)
    disponibilidad = models.BooleanField(default=True)
    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Categoría de publicación"
        verbose_name_plural = "Categorías de publicación"
    
    def __str__(self):
        return self.nombre

class Post(models.Model):
    titulo = models.CharField(max_length=80)
    resumen = models.CharField(max_length=500)
    imagen = models.ImageField(upload_to='blog', null=True, blank=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    categorias = models.ManyToManyField(CategoriaPost)
    contenido = HTMLField()
    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Publicación"
        verbose_name_plural = "Publicaciones"
    
    def __str__(self):
        return self.titulo
