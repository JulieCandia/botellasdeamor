from django.db import models

# Create your models here.
class Equipo(models.Model):
    nombre = models.CharField(max_length = 80)
    informacion = models.TextField()
    imagen = models.ImageField(upload_to= 'equipo')

    def __str__(self):
	    return self.nombre