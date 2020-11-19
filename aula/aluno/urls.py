from django.urls import path

from . import views

app_name = "aluno"

urlpatterns = [
    
    path('', views.busca_aluno, name="index"), #/aluno/
    path('aniversario/', views.aniversario, name="aniversario"),
    path('<int:cd_aluno>/', views.busca_aluno, name="index"), #/aluno/
    path('<str:tipo>/', views.busca_aluno, name="edit"),
    path('<str:tipo>/<int:cd_aluno>/', views.busca_aluno, name="edit"), #/aluno/
    path('cadastra/', views.cadastra, name="cadastra"), # /aluno/cadastra/
    path('endereco/cadastra/', views.cad_endereco, name="cadendereco"), #/aluno/endereco/cadastra
    
]