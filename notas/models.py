from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Nota(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200, verbose_name="Título")
    contenido = models.TextField(verbose_name="Contenido")
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    fecha_edicion = models.DateTimeField(auto_now=True, verbose_name="Fecha de última edición")

    def __str__(self):
        return self.titulo