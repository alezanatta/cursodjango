from django.urls import path

from . import views

app_name = "aluno"

urlpatterns = [
    path('', views.busca_aluno, name="index"), #/aluno/
    path('busca/', views.busca, name="busca"), # /aluno/busca/
    path('cadastra/', views.cadastra, name="cadastra"), # /aluno/cadastra/
    path('endereco/cadastra/', views.cad_endereco, name="cadendereco"), #/aluno/endereco/cadastra
]