from django.urls import path

from . import views

app_name="aluno"

urlpatterns = [
    path('alunos/', views.alunos, name="alunos"), #/aluno/alunos
    path('alunos/<int:matricula>', views.alunos, name="aluno"), #/aluno/alunos
]