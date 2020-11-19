from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from django.views.decorators.csrf import csrf_exempt

# Create your views here.

from .models import Aluno
from .serializers import AlunoModelSerializer

@csrf_exempt
@api_view(["GET", "POST"])
def alunos(request, matricula=-1):

    if request.method == "GET":
        if matricula == -1:
            alunos = Aluno.objects.all()
            serial = AlunoModelSerializer(alunos, many=True)
            return JsonResponse(serial.data, safe=False)
        elif matricula > 0:
            aluno = Aluno.objects.get(pk=matricula)
            serial = AlunoModelSerializer(aluno)
            return JsonResponse(serial.data)

    elif request.method == "POST":
        dados = JSONParser().parse(request)
        serial = AlunoModelSerializer(data=dados)
        if serial.is_valid():
            serial.save()
            return JsonResponse(serial.data, status=201)
        return JsonResponse(serial.errors, status=400)
#    else:
#        return HttpResponse("Método não suportado", status=405)


class AlunoAPI(APIView):

    def get(self, request):
        pass

    def post(self, request):
        pass