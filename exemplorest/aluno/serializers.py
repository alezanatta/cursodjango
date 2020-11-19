from rest_framework import serializers

from .models import Aluno

class AlunoModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ["matricula", "dt_cadastro", "nm_aluno"]

class AlunoSerializer(serializers.Serializer):
    matricula = serializers.IntegerField(read_only=True)
    dt_cadastro = serializers.DateField()
    nm_aluno = serializers.CharField(max_length=50)