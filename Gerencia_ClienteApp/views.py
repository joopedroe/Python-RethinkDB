import rethinkdb

from django.views.generic import FormView
from django.shortcuts import render, redirect
from .forms import (
    NewCharacterForm, 
    DeleteForm, 
    ReadForm, 
    UpdateForm
)


r = rethinkdb.RethinkDB()

connection = r.connect("localhost", 28015)

def CadastroCliente(request):
    if request.method == "POST":
        nome=request.POST.get('nome')
        cpf=request.POST.get('cpf')
        endereco=request.POST.get('endereco')

        r.db("Loja").table("cliente").insert({
            "nome":nome,
            "cpf":cpf,
            "endereco":endereco
        }).run(connection)

        return redirect('exibeClientesTempoReal')
    else:
        return render (request,'Gerencia_ClienteApp/inicial.html')

def ExibeClientes(request):
    clientes=r.db("Loja").table("cliente").run(connection)
    return render (request,'Gerencia_ClienteApp/exibe.html',{'clientes':clientes})

def ExibeClientesTempoReal(request):
    clientes=r.db("Loja").table("cliente").run(connection)
    feed=r.db("Loja").table("cliente").changes().run(connection)
    return render (request,'Gerencia_ClienteApp/exibe.html',{'clientes':clientes})

def EncontraCliente(request,clienteId):
    cliente=r.db("Loja").table("cliente").get(clienteId).run(connection)
    return render (request,'Gerencia_ClienteApp/cliente.html',{'cliente':cliente})

def NewCharacterView(request):
    form_class=NewCharacterForm
    template_name='Gerencia_ClienteApp/new.html'

    return render(
        request,
        template_name,
        {'form':form_class}
    )

def ReadView(request):
    template_name = 'Gerencia_ClienteApp/read.html'
    sucess_url = 'clientes:read'
    form_class = ReadForm

    # if request.method == "GET":
    #     try:
    #         exercito = None
    #     except rethinkdb.errors.ReqlCompileError as error:
    #         print(error)

    # else:
    #     return render(
    #         request,
    #         template_name,

    #     )

    return render(
        request,
        template_name,
        {'form':form_class}
    )

def UpdateView(request):
    template_name = 'Gerencia_ClienteApp/update.html'
    sucess_url = 'clientes:update'
    form_class = UpdateForm

    return render(
        request,
        template_name,
        {'form':form_class}
    )



def DeleteView(request):
    template_name = 'Gerencia_ClienteApp/delete.html'
    sucess_url = 'clientes:delete'
    form_class = DeleteForm

    return render(
        request,
        template_name,
        {'form':form_class}
    )


