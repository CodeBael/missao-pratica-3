


def calcular_media(notas):
    return sum(notas) / len(notas)

def verificar_reprovacao(media):
    return media < 6

def alunos_reprovados(dados_alunos, matriculas_reprovaods):
    for aluno in dados_alunos:
        if aluno["matricula"] in matriculas_reprovaods:
             print(f"aluno reprovado: {aluno["nome"]} - matricula: {aluno["matricula"]} - media final: {aluno["media_final"]}")

dados_alunos = [
    {"nome": "maria", "matricula": 26, "notas": [8, 7, 5, 9]},
    {"nome": "Ana", "matricula": 101, "notas": [9, 9, 8, 9]},
    {"nome": "joão", "matricula": 13, "notas": [6, 5, 5, 5]},
    {"nome": "agata", "matricula": 37, "notas": [8, 6, 7.5, 9]},
    {"nome": "joaquim", "matricula": 72, "notas": [6, 5.5, 5, 7]},
    {"nome": "felix", "matricula": 5, "notas": [10, 8, 8, 8]},
]

matriculas_reprovados = []
for aluno in dados_alunos:
    media = calcular_media(aluno["notas"])
    aluno["media_final"] = media
    if verificar_reprovacao(media):
        matriculas_reprovados.append(aluno["matricula"])
alunos_reprovados(dados_alunos, matriculas_reprovados)

