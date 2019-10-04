from django.shortcuts import render, redirect

# Create your views here.

from rethinkdb import RethinkDB
r = RethinkDB()

connection=r.connect( "localhost", 28015)

def CadastroCliente(request):
    if request.method == "POST":
        nome=request.POST.get('nome')
        cpf=request.POST.get('cpf')
        endereco=request.POST.get('endereco')
        r.db("Loja").table("cliente").insert({"nome":nome,"cpf":cpf,"endereco":endereco}).run(connection)
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