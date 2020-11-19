from django import forms # Forms
from django.forms import ModelForm

from .models import Cidade
from .models import Endereco
from .models import Aluno

class CidadeForm(ModelForm):
    class Meta:
        model = Cidade
        fields = ["nm_cidade", "nm_estado","sg_estado"]

class EnderecoForm(ModelForm):
    class Meta:
        model = Endereco
        fields = "__all__" # Inclui tudo oq está no Model
        widgets = {
            "nm_rua": forms.Textarea(attrs={
                "rows": 10,
                "cols": 50,
            }),
        }
        labels = {
            "nm_rua": "Nome da rua",
            "nm_bairro": "Nome do bairro",
            "fk_cidade": "Nome da cidade"
        }
        help_texts = {
            "nm_rua": "No máximo 70 caracteres",
        }
        error_messages = {
            "nm_rua":{
                "required": "O campo é obrigatório",
                "max_length": "No máximo 70 caracteres"
            }
        }


class AlunoForm(ModelForm):
    class Meta:
        model = Aluno
        fields = '__all__'

class BuscaAlunoForm(forms.Form):
    matricula = forms.IntegerField()
    help_texts = {
            "matricula": "Sei lá",
        }

class AniversarioForm(forms.Form):
    mes = forms.IntegerField()