import requests
import json
from datetime import date

aluno = {
    "nm_aluno":"Abacate",
    #"dt_criacao": str(date.today())
}
aluno = json.dumps(aluno)

teste = requests.put("http://localhost:8000/aluno/alunos/", data=aluno)

print(teste.text)
print(teste.status_code)