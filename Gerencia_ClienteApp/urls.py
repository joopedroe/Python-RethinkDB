
from django.urls import path
from .views import *

app_name='clientes'

urlpatterns = [
    path('cadastro/',CadastroCliente, name="cadastroCliente" ),
    path('clientes/',ExibeClientesTempoReal, name="exibeClientesTempoReal" ),
    path('clientes/todos',ExibeClientes, name="exibeClientes" ),
    path('clientes/<str:clienteId>/',EncontraCliente,name='encontraCliente'),
    path('visualizar/', ReadView, name='read'),
    path('atualizar/<int:id>', UpdateView, name='update'),
    path('deletar/<int:id>', DeleteView, name='delete'),
]
