from django.shortcuts import render
from django.http import HttpResponse

from datetime import datetime

from .models import Aluno

from .forms import CidadeForm
from .forms import EnderecoForm

from .forms import BuscaAlunoForm

# Create your views here.

def index(request):
    return render(request, "aluno/index.html", {})

def busca(request):
    return render(request, "aluno/busca.html", {})

def cadastra(request):

    if request.method == "GET":
        form = CidadeForm()
        context = {"form":form}
        return render(request, "aluno/cadastra.html", context)
    
    elif request.method == "POST":        
        form = CidadeForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponse("É valido")
        else:
            return HttpResponse("Não é valido")
    else:
        return HttpResponse("Não tem")

def cad_endereco(request):

    if request.method == "GET":
        form = EnderecoForm()
        context = {
            "form":form,
        }
        return render(request, "aluno/cad_endereco.html", context)
    elif request.method == "POST":
        form = EnderecoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("É valido")
        else:
            return HttpResponse("Não é valido")
    else:
        return HttpResponse("Não tem")

def busca_aluno(request):

    form = BuscaAlunoForm()

    alunos = Aluno.objects.all() # Select * from aluno;

    context = {
        "alunos": alunos,
        "form":form,
    }

    return render(request, "aluno/aluno.html", context)
