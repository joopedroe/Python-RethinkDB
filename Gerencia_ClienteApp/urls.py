
from django.urls import path
from .views import *

urlpatterns = [
    path('cadastro/',CadastroCliente, name="cadastroCliente" ),
    path('clientes/',ExibeClientesTempoReal, name="exibeClientesTempoReal" ),
    path('clientes/todos',ExibeClientes, name="exibeClientes" ),
    path('clientes/<str:clienteId>/',EncontraCliente,name='encontraCliente'),

]
