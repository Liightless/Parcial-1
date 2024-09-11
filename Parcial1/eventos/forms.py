from django import forms
from .models import Organizador
from .models import Evento

class OrganizadorForm(forms.ModelForm):
    class Meta:
        model = Organizador
        fields = ['nombre', 'telefono', 'email']

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['nombre', 'organizador', 'fecha', 'descripcion']