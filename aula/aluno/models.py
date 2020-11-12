from django.db import models

# Create your models here.

class Cidade(models.Model):
    nm_cidade = models.CharField(max_length=30, verbose_name="Nome da cidade")
    nm_estado = models.CharField(max_length=20)
    nm_pais = models.CharField(max_length=20)
    sg_estado = models.CharField(max_length=2)

    def __str__(self):
        return str(self.nm_cidade) + " - " + str(self.sg_estado)


class Endereco(models.Model):
    nm_rua = models.CharField(max_length=70, verbose_name="Rua")
    nm_bairro = models.CharField(max_length=30)
    fk_cidade = models.ForeignKey(Cidade, on_delete=models.PROTECT)

    def __str__(self): ## Dois _ antes e dois _ depois
        return str(self.nm_rua) + " " + str(self.nm_bairro)

class Aluno(models.Model):
    matricula = models.IntegerField(default=0)
    nome = models.CharField(max_length=50)
    data_nascimento = models.DateField()
    cpf = models.CharField(max_length=14, unique=True)
    nr_endereco = models.IntegerField(null=True, blank=True)
    fk_endereco = models.ForeignKey(Endereco, on_delete=models.PROTECT)
    seila = models.IntegerField