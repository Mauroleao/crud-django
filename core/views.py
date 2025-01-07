from django.shortcuts import render, redirect, get_object_or_404
from .models import Pessoa

def home(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'index.html', {'pessoas': pessoas})

def salvar(request):
    if request.method == 'POST':
        nome = request.POST.get('nome', '')
        idade = request.POST.get('idade', 0)
        Pessoa.objects.create(nome=nome, idade=idade)
    return redirect('home')

def editar(request, id):
    pessoa = get_object_or_404(Pessoa, id=id)
    return render(request, 'update.html', {'pessoa': pessoa})

def update(request, id):
    if request.method == 'POST':
        nome = request.POST.get('nome', '')
        idade = request.POST.get('idade', 0)
        pessoa = get_object_or_404(Pessoa, id=id)
        pessoa.nome = nome or 'Sem nome'
        pessoa.idade = idade
        pessoa.save()
    return redirect('home')

def delete(request, id):
    pessoa = get_object_or_404(Pessoa, id=id)
    pessoa.delete()
    return redirect('home')