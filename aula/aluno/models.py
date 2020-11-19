from django.db import models, connection


from datetime import date
import pandas as pd

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


    def is_idade(self):
        #print((date.today() - self.data_nascimento).days)
        if ((date.today() - self.data_nascimento).days >= 0) and ((date.today() - self.data_nascimento).days <= 105*365.2425):
            return True
        return False

    def is_cpf(self,d1=0,d2=0,i=0):
        cpf = self.cpf
        while i<10:
            d1,d2,i=(d1+(int(cpf[i])*(11-i-1)))%11 if i<9 else d1,(d2+(int(cpf[i])*(11-i)))%11,i+1
        return (int(cpf[9])==(11-d1 if d1>1 else 0)) and (int(cpf[10])==(11-d2 if d2>1 else 0))
    

    @staticmethod
    def aniversario(mes=date.today().month):

        query = f"""
            SELECT nome, data_nascimento FROM aluno_aluno
            WHERE MONTH(data_nascimento) = {mes}
        """

        with connection.cursor() as cursor:
            cursor.execute(query)
            alunos = cursor.fetchall()
            #cursor.callproc("nome_proc", [])

            # fetchall -> ResultSet
            # fetchone -> Somente o primeiro. Mais utilizado com PK ou UQ

            return alunos

    @staticmethod
    def pd_aniversario(mes=date.today().month):
        query = f"""
            SELECT nome, data_nascimento FROM aluno_aluno
            WHERE MONTH(data_nascimento) = {mes}
        """

        df = pd.read_sql(query, connection)
        return df
