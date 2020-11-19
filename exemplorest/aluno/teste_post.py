import requests
import json
from datetime import date

aluno = {
    "nm_aluno":"Robin",
    #"dt_criacao": str(date.today())
}
aluno = json.dumps(aluno)

teste = requests.post("http://localhost:8000/aluno/alunos/", data=aluno)

print(teste.text)
print(teste.status_code)