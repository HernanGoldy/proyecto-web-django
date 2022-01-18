from distutils.command.upload import upload
from email.headerregistry import ContentDispositionHeader
from pyexpat import model
from tabnanny import verbose
from django.db import models
# Aquí tenemos que crear nuestro "Mapeo ORM" (Mapeo de Objetos Relacionales)

# Create your models here.

class Servicio(models.Model):
    titulo= models.CharField(max_length=50)
    contenido= models.CharField(max_length=50)
    imagen= models.ImageField(upload_to='servicios')
    created= models.DateTimeField(auto_now_add=True)
    updated= models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name= 'servicio'
        verbose_name_plural= 'servicios'
    
    # Creamos una función para que nos devuelva el título del servicio
    def __str__(self):
        return self.titulo
