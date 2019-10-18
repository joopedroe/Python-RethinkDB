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


# Parte pratica temática


def NewCharacterView(request):
    form = NewCharacterForm
    sucess_url = 'clientes:new'
    template_name = 'Gerencia_ClienteApp/new.html'

    if request.method == 'POST':
        form = NewCharacterForm(request.POST)
        tabela = request.POST.get('tabela')
        print(f'Tabela aqui oh: {tabela}')

        if form.is_valid():
            dados = form.clean()
            r.db(
                "universo_dc"
            ).table(
                f"{tabela}"
            ).insert({
                "nome":f"{dados['nome']}",
                "xp":f"{dados['xp']}",
                "habilidade":f"{dados['habilidade']}",
                "poder":f"{dados['poder']}"
            }).run(connection)
            return redirect(sucess_url)

    else:
        return render(
            request,
            template_name,
            {'form':form}
        )

    return render(
        request,
        template_name,
        {'form':form}
    )

def ReadView(request):
    template_name = 'Gerencia_ClienteApp/read.html'
    sucess_url = 'clientes:read'
    form = ReadForm

    return render(
        request,
        template_name,
        {'form':form}
    )

def UpdateView(request):
    template_name = 'Gerencia_ClienteApp/update.html'
    sucess_url = 'clientes:update'
    form = UpdateForm

    return render(
        request,
        template_name,
        {'form':form}
    )


def DeleteView(request):
    template_name = 'Gerencia_ClienteApp/delete.html'
    sucess_url = 'clientes:delete'
    form = DeleteForm

    return render(
        request,
        template_name,
        {'form':form}
    )

