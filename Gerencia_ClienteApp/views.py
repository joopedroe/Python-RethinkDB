import rethinkdb

from django.views.generic import FormView

from django.shortcuts import render, redirect
from django.urls.base import reverse_lazy
from django.urls.base import reverse

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


# Parte pratica temática CRUD

def NewCharacterView(request):
    form = NewCharacterForm
    sucess_url = 'clientes:new'
    template_name = 'Gerencia_ClienteApp/new.html'
    context = {
        'form':form
    }

    if request.method == 'POST':
        form = NewCharacterForm(request.POST)
        tabela = request.POST.get('tabela')

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
            request,template_name,context)

    return render(
        request, template_name, context)

def ReadView(request):
    form = ReadForm
    sucess_url = 'clientes:read'
    template_name = 'Gerencia_ClienteApp/read.html'
    resultados = None
    context = {
        'form':form
    }
    
    if request.method == 'GET':
        search_term = ''
        table = request.GET.get('table', 'viloes')

        if 'search' in request.GET:
            search_term = request.GET.get('search')
            character = r.db(
                'universo_dc'
            ).table(
                f'{table}'
            ).filter(
                {'nome':search_term}
            ).run(connection)

            print(f"READ aqui oh: {character}")

            context['resultados'] = character
            context['search_term'] = search_term

    return render(
        request, template_name, context)

def UpdateView(request, id):
    sucess_url = 'clientes:update'
    template_name = 'Gerencia_ClienteApp/update.html'
    sucess_url = 'clientes:read'
    form = UpdateForm
    table = request.POST.get('table', 'viloes')
    context = {
        'form':form
    }

    print(f"ID aqui: {id} - {table}")

    if table is not None:
        context['personagem'] = r.db(
            'universo_dc'
        ).table(
            f"{table}"
        ).get(
            f"{id}"
        ).run(connection)

        print(context['personagem'])

    if request.method == 'POST':
        form = UpdateForm(request.POST)

        if form.is_valid():
            print('UPDATE tudo certo por aqui!')

            dados = form.clean()
            nome = dados['nome']
            xp = dados['xp']
            habilidade = dados['habilidade']        
            poder = dados['poder']

            r.db(
                'universo_dc'
            ).table(
                f"{table}"
            ).get(
                f"{id}"
            ).update({
                "nome":nome,
                "xp":xp,
                "habilidade":habilidade,
                "poder":poder
            }).run(connection)

            print('acabou aqui oh')

            sucess_url = (
                f"{reverse(sucess_url)}?table="
                f"{request.POST.get('table')}&search="
                f"{request.POST.get('nome')}"
            )

            return redirect(sucess_url)

    return render(
        request, template_name, context)


def DeleteView(request, id):
    template_name = 'Gerencia_ClienteApp/delete.html'
    sucess_url = 'clientes:read'
    form = DeleteForm
    context = {
        'form':form
    }

    print('iniciando')

    if request.method == 'POST':
        print('DELETE tudo certo aqui')
        table = 'viloes'
        r.db(
            'universo_dc'
        ).table(
            f"{table}"
        ).get(
            f"{id}"
        ).delete().run(connection)

        print('DELETE herois')
        table = 'herois'
        r.db(
            'universo_dc'
        ).table(
            f"{table}"
        ).get(
            f"{id}"
        ).delete().run(connection)

        sucess_url = (
            f"{reverse(sucess_url)}?table="
            f"{table}&search="
            f"{request.POST.get('nome')}"
        )

        print(sucess_url)

        return redirect(sucess_url)
        

    return render(
        request, template_name, context)

