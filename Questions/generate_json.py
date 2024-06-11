import json
import re

# Define the prova_id
prova_id = 4

# Leitura do arquivo de texto
with open('questions.txt', 'r', encoding='utf-8') as file:
    data = file.read()

# Regex para capturar cada pergunta e suas respostas
question_pattern = re.compile(
    r'Question #\d+\s*\n(.*?)\s*\nA\.\s(.*?)\s*\nB\.\s(.*?)\s*\nC\.\s(.*?)\s*\nD\.\s(.*?)\s*\nCorrect Answer: (\w)',
    re.DOTALL
)

# Inicialização das listas de perguntas e respostas
questions = []
answers = []
pergunta_pk = 1
resposta_pk = 1

# Processar cada pergunta
for match in question_pattern.finditer(data):
    texto = match.group(1).strip()
    respostas = [match.group(i).strip() for i in range(2, 6)]
    correta = match.group(6).strip()

    # Adicionar pergunta ao JSON
    questions.append({
        "model": "provas.pergunta",
        "pk": pergunta_pk,
        "fields": {
            "prova": prova_id,
            "texto": texto,
            "imagem": None
        }
    })

    # Adicionar respostas ao JSON
    for i, resposta in enumerate(respostas):
        answers.append({
            "model": "provas.resposta",
            "pk": resposta_pk,
            "fields": {
                "pergunta": pergunta_pk,
                "texto": resposta,
                "correta": (correta == chr(65 + i))  # 'A' == chr(65), 'B' == chr(66), etc.
            }
        })
        resposta_pk += 1

    pergunta_pk += 1

# Combinar perguntas e respostas
output = questions + answers

# Salvar no arquivo JSON
with open('questions.json', 'w', encoding='utf-8') as json_file:
    json.dump(output, json_file, indent=4)

print("Arquivo questions.json gerado com sucesso!")

