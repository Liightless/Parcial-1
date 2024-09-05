from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView
from .models import Organizador
from .forms import OrganizadorForm
from django.urls import reverse_lazy
from django.http import HttpResponse
from .models import Evento
from .forms import EventoForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView


def inicio(request):
    return HttpResponse("<h1>Bienvenido al sistema de gestión de eventos</h1>")


class OrganizadorListView(ListView):
    model = Organizador
    template_name = 'eventos/organizador_list.html'
    context_object_name = 'organizadores'

class OrganizadorCreateView(CreateView):
    model = Organizador
    form_class = OrganizadorForm
    template_name = 'eventos/organizador_form.html'
    success_url = reverse_lazy('organizador-list')

class EventoListView(ListView):
    model = Evento
    template_name = 'eventos/evento_list.html'
    context_object_name = 'eventos'

class EventoCreateView(LoginRequiredMixin, CreateView):
    model = Evento
    form_class = EventoForm
    template_name = 'eventos/evento_form.html'
    success_url = '/eventos/'

class EventoUpdateView(LoginRequiredMixin, UpdateView):
    model = Evento
    form_class = EventoForm
    template_name = 'eventos/evento_form.html'
    success_url = '/eventos/'