from django.db import models
from django.core.exceptions import ValidationError


class Organizador(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15, null=True, blank=True)  
    email = models.EmailField(null=True, blank=True) 

    def __str__(self):
        return self.nombre


def validar_nombre_evento(value):
    palabras_restringidas = ['prohibido', 'secreto']
    if any(palabra in value.lower() for palabra in palabras_restringidas):
        raise ValidationError(f"El nombre del evento no puede contener palabras restringidas: {', '.join(palabras_restringidas)}")

class Evento(models.Model):
    nombre = models.CharField(max_length=200)
    organizador = models.ForeignKey(Organizador, on_delete=models.CASCADE)
    fecha = models.DateField()
    descripcion = models.TextField(default='No description provided') 

    def __str__(self):
        return self.nombre
