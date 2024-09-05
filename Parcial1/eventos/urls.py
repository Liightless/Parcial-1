from django.urls import path
from .views import EventoListView, EventoCreateView, EventoUpdateView
from .views import OrganizadorListView, OrganizadorCreateView

urlpatterns = [
    # Rutas para Organizadores
    path('organizadores/', OrganizadorListView.as_view(), name='organizador-list'),
    path('organizadores/nuevo/', OrganizadorCreateView.as_view(), name='organizador-create'),
    
    # Rutas para Eventos
    path('eventos/', EventoListView.as_view(), name='evento-list'),
    path('eventos/nuevo/', EventoCreateView.as_view(), name='evento-create'),
    path('eventos/<int:pk>/editar/', EventoUpdateView.as_view(), name='evento-update'),
]
