
from django.urls import path
from .views import *

app_name='clientes'

urlpatterns = [
    path('cadastro/',CadastroCliente, name="cadastroCliente" ),
    path('clientes/',ExibeClientesTempoReal, name="exibeClientesTempoReal" ),
    path('clientes/todos',ExibeClientes, name="exibeClientes" ),
    path('clientes/<str:clienteId>/',EncontraCliente,name='encontraCliente'),
    path('visualizar/', ReadView, name='read'),
    path('atualizar/', UpdateView, name='update'),
    path('deletar/', DeleteView, name='delete'),
    path('new/', NewCharacterView, name='new')
]
