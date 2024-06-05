from django.db import models

class Destino(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    ubicacion = models.CharField(max_length=100)
    fecha_visita = models.DateField()

    def __str__(self):
        return self.nombre
