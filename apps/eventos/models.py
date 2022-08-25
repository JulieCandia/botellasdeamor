from django.db import models

# Create your models here.

class Evento(models.Model):
    titulo = models.CharField(max_length=65)
    fecha = models.DateTimeField('Fecha del evento')
    tipo = models.CharField(max_length =30)
    descripcion = models.CharField(max_length = 200)

    def __str__(self):
        return self.titulo