
from django.urls import path
from .views import *

app_name='clientes'

urlpatterns = [
    path('cadastro/',CadastroCliente, name="cadastroCliente" ),
    path('clientes/',ExibeClientesTempoReal, name="exibeClientesTempoReal" ),
    path('clientes/todos',ExibeClientes, name="exibeClientes" ),
    path('clientes/<str:clienteId>/',EncontraCliente,name='encontraCliente'),

    #CRUD
    path('novo/', NewCharacterView, name='new'),
    path('visualizar/', ReadView, name='read'),
    path('atualizar/<uuid:id>', UpdateView, name='update'),
    path('deletar/<uuid:id>', DeleteView, name='delete'),
]
