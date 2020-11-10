from django.contrib import admin

from .models import Aluno
from .models import Endereco
from .models import Cidade

# Register your models here.


admin.site.register(Aluno)
admin.site.register(Endereco)
admin.site.register(Cidade)