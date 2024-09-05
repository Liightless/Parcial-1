from django import forms
from .models import Organizador
from .models import Evento

class OrganizadorForm(forms.ModelForm):
    class Meta:
        model = Organizador
        fields = ['nombre', 'email', 'telefono']

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['nombre', 'fecha', 'organizador']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
        }