from django.urls import path
from .views import EventoCreateView, EventoListView, EventoUpdateView, OrganizadorCreateView, OrganizadorListView

urlpatterns = [
    path('', EventoListView.as_view(), name='evento-list'), 
    path('nuevo/', EventoCreateView.as_view(), name='evento-create'), 
    path('<int:pk>/editar/', EventoUpdateView.as_view(), name='evento-edit'),  
    path('organizadores/', OrganizadorListView.as_view(), name='organizador-list'), 
    path('organizadores/nuevo/', OrganizadorCreateView.as_view(), name='organizador-create'),  
]
