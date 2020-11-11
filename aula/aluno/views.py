from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from datetime import datetime

from .models import Aluno

from .forms import CidadeForm
from .forms import EnderecoForm
from .forms import AlunoForm

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

def busca_aluno(request, cd_aluno=0, tipo=""):

    context = {
        "form":None,
        "alunos":None,
        "aluno":None,
        "edit_aluno":None,
    }

    if request.method == "GET":
        if tipo == "edit":
            aluno = Aluno.objects.get(pk=cd_aluno)
            form = AlunoForm(instance=aluno)
            context["edit_aluno"] = form
            return render(request, "aluno/aluno.html", context)

        if cd_aluno:
            aluno = Aluno.objects.get(pk=cd_aluno)
            form = BuscaAlunoForm()
            context["aluno"] = aluno
            context["form"] = form
            
            return render(request, "aluno/aluno.html", context)

        else:
            form = BuscaAlunoForm()
            alunos = Aluno.objects.all() # Select * from aluno;
            context["alunos"] = alunos
            context["form"] = form
            return render(request, "aluno/aluno.html", context)
    elif request.method == "POST":
        if tipo == "delete":
            form = AlunoForm(request.POST)
            if form.is_valid():
                aluno = Aluno()
                aluno.id = form.cleaned_data["id"]
                aluno.delete()



        if tipo == 'edit':
            form = AlunoForm(request.POST)
            if form.is_valid():
                form.save()
                form = BuscaAlunoForm()
                alunos = Aluno.objects.all()
                context["alunos"] = alunos
                context["form"] = form
                return HttpResponseRedirect(reverse("aluno:index"))

        
        form = BuscaAlunoForm(request.POST)
        if form.is_valid():
            matricula = form.cleaned_data["matricula"]
            alunos = Aluno.objects.all().filter(matricula=matricula)
            form = BuscaAlunoForm()
            context["alunos"] = alunos
            context["form"] = form
            return render(request, "aluno/aluno.html", context)
