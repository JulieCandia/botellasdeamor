from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=60)

    def __str__(self):
	    return self.nombre

class Galeria(models.Model):
    titulo = models.CharField(max_length = 80)
    imagen = models.ImageField(upload_to= 'galeria', null= True, blank= True)
    categoria = models.ForeignKey(Categoria, on_delete = models.CASCADE, null= True)

    def __str__(self):
        return self.titulo