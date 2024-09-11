from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView
from .models import Organizador, Evento
from .forms import OrganizadorForm, EventoForm
from django.urls import reverse_lazy

class OrganizadorListView(LoginRequiredMixin, ListView):
    model = Organizador
    template_name = 'organizador_list.html'
    context_object_name = 'organizadores'

class OrganizadorCreateView(LoginRequiredMixin, CreateView):
    model = Organizador
    form_class = OrganizadorForm
    template_name = 'organizador_form.html'
    success_url = reverse_lazy('organizador-list')

class EventoListView(ListView):
    model = Evento
    template_name = 'eventos/evento_list.html'
    context_object_name = 'eventos'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user  
        return context

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

    login_url = '/login/'
