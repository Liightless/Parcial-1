from django.db import models
from django.core.exceptions import ValidationError

class Organizador(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.nombre

def validar_nombre_evento(value):
    palabras_restringidas = ['prohibido', 'secreto']
    if any(palabra in value.lower() for palabra in palabras_restringidas):
        raise ValidationError(f"El nombre del evento no puede contener palabras restringidas: {', '.join(palabras_restringidas)}")

class Evento(models.Model):
    nombre = models.CharField(max_length=200, validators=[validar_nombre_evento])
    fecha = models.DateField()
    organizador = models.ForeignKey(Organizador, on_delete=models.CASCADE, related_name='eventos')

    def __str__(self):
        return self.nombre
