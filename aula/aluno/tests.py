from django.test import TestCase, RequestFactory
from django.urls import reverse

from .models import Aluno

from .views import cad_endereco

from datetime import date
from datetime import timedelta

from random import randint

# Create your tests here.


class AlunoModelTest(TestCase):
    
    def teste_idade_aluno_valida(self):
        tempo = date.today() - timedelta(days=randint(0,105) * 365.2425)
        aluno = Aluno(data_nascimento=tempo)
        self.assertIs(aluno.is_idade(), True)

    def teste_idade_aluno_minimo(self):
        tempo = date.today() + timedelta(days=1)
        aluno = Aluno(data_nascimento=tempo)
        self.assertIs(aluno.is_idade(), False)

    def teste_idade_aluno_maximo(self):
        tempo = date.today() - timedelta(days=106*365.2425)
        aluno = Aluno(data_nascimento=tempo)
        self.assertIs(aluno.is_idade(), False)
    
    def teste_cpf_aluno_invalido(self):
        cpf = "12345678910"
        aluno = Aluno(cpf=cpf)
        self.assertIs(aluno.is_cpf(), False)

    def teste_cpf_aluno_valido(self):
        cpf = "11345125380"
        aluno = Aluno(cpf=cpf)
        self.assertIs(aluno.is_cpf(), True)


class EnderecoViewTeste(TestCase):

    def setUp(self):
        #Tudo o que o meu request precisa para acessar a View
        self.factory = RequestFactory()

    def test_details(self):
        request = self.factory.get(reverse("aluno:cadendereco"))
        response = cad_endereco(request)
        self.assertEqual(response.status_code, 304)