from django.db import models

# Create your models here.


class Aluno(models.Model):
    matricula = models.AutoField(primary_key=True)
    dt_cadastro = models.DateField(auto_now_add=True)
    nm_aluno = models.CharField(max_length=50)

    def __str__(self):
        return f"""{self.nm_aluno}"""

    class Meta:
        ordering = ["matricula"]

    