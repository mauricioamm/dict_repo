from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import dictclass
from .forms import DictForm

def listagem(request):
    data = {}
    data['lista']= dictclass.objetos.all()
    #data['lista']= dictclass.objects.first()
    #data['lista'] = dictclass.objects.last()

    return render(request, 'dictapp/listagem.html', data)

def nova_transacao(request):
    data= {}
    form = DictForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('url_listagem')
    data['form']= form
    return render (request, 'dictapp/form.html', data)

def nova_transacao2(request):
    data= {}
    form = DictForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('url_listagem')
    data['form']= form
    return render (request, 'dictapp/Cadastro_de_fora_vazio.html', data)

def update(request, pk):
    data={}
    lista = dictclass.objetos.get(pk=pk)
    form= DictForm(request.POST or None, instance= lista)
    if form.is_valid():
        form.save()
        return redirect('url_listagem')
    data['form'] = form
    data['lista']= lista
    return render(request, 'dictapp/Cadastro_de_fora.html', data)

"""
def update(request, pk):
    data={}
    lista = dictclass.objetos.get(pk=pk)
    form= DictForm(request.POST or None, instance= lista)
    if form.is_valid():
        form.save()
        return redirect('url_listagem')
    data['form'] = form
    data['lista']= lista
    return render(request, 'dictapp/form.html', data)
"""

def delete(request, pk):
    lista = dictclass.objetos.get(pk=pk)
    lista.delete()
    return redirect('url_listagem')

def page2(request):
    return render(request, "dictapp/Oi.html")

def page3(request, pk):
    data= {}
    objetinho = dictclass.objetos.get(pk=pk)
    form= DictForm(request.POST or None, instance= objetinho)

    if request.POST.get('Listagem'):
        return redirect('url_listagem')

    if request.POST.get('Novo'):
        return redirect('url_nova2')

    if request.POST.get('Salvar'):
        if form.is_valid():
            form.save()
            # aqui o form é recarregado, mas continua na mesma página
            data['form'] = form
            data['objetinho'] = objetinho
            return render(request, 'dictapp/Cadastro_de_fora.html', data)

    if request.POST.get('Excluir'):
        objetinho.delete()
        return redirect('url_listagem')

    if request.POST.get('Sortear'):
        print('Sorteou, sim')
        return redirect('url_listagem')

    if request.POST.get('primeiro'):
        #data['form'] = form
        objetinho = dictclass.objetos.get(pk=1)
        #data['objetinho'] = objetinho
        #return render(request, 'dictapp/Cadastro_de_fora.html')
        #print(objetinho)
        n= 7
        return redirect('url_page3', pk=n)


    if request.POST.get('proximo'):
        data = {}
        objetinho = dictclass.objetos.get(pk=2)
        form = DictForm(request.POST or None, instance=objetinho)
        data['form'] = form
        data['objetinho'] = objetinho
        return render(request, 'dictapp/Cadastro_de_fora.html', data)

    data['form'] = form
    data['objetinho']= objetinho
    return render(request, 'dictapp/Cadastro_de_fora.html', data)

"""
def primeiro(request, pk):
    if request.POST.get('primeiro'):
        #objetinho = dictclass.objetos.get(pk=1)
        return redirect('url_page3', pk=1)
        #return render(request, 'dictapp/Cadastro_de_fora.html', objetinho)
"""
def indexhome(request):
    return render(request, 'dictapp/index.html')

def cadastroteste(request):
    return render(request, 'dictapp/Cadastroteste.html')

def indexfunction(request):
    f = None
    if request.method == 'GET':
        f = request.GET['teste']
    if f:
        print('OK')
    #return HttpResponse('Passou')
    return redirect('url_listagem')

"""
def pageincrementa(request, pk):
    objetinho = dictclass.objetos.get(pk=pk)
    pk= pk + 1
    objetinho = dictclass.objetos.get(pk=pk)
    return render(request, 'dictapp/Cadastro_de_fora.html')

def page3(request, pk):
    #Funcionando lindamente
    data= {}
    objetinho = dictclass.objetos.get(pk=pk)
    form2= DictForm(instance= objetinho)
    if form2.is_valid():
        form2.save()
        return redirect('url_listagem')
    data['form'] = form2
    data['objetinho']= objetinho
    return render(request, 'dictapp/form2.html', data)



from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Transacao
from .forms import TransacaoForm
import datetime

def listagem(request):
    data = {}
    data['transacoes']= Transacao.objects.all()
    return render(request, 'contas/listagem.html', data)

def Home(request):
    data = {}
    data['transacoes']= ['t1','t2','t3']
    data['now']= datetime.datetime.now()
    return render(request, 'contas/home.html', data)

def Casinha(request):
    return render(request, "contas/Oi.html")

def nova_transacao(request):
    data= {}
    form = TransacaoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('url_listagem')
    data['form']= form
    return render (request, 'contas/form.html', data)




"""
