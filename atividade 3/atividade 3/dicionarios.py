meu_dicionario = {
    "codigo_1": "Python",
    "codigo_2": "Java",
    "codigo_3": "PHP"
}
print(meu_dicionario)
print(type(meu_dicionario))

valor_codigo1 = meu_dicionario.get("codigo_1")
print(valor_codigo1)
print(len(meu_dicionario))

dicionario_frutas = dict({
    1: {"nome": "limão", "tipo": "acida"},
    2: {"nome": "laranja", "tipo": "acida"},
    3: {"nome": "manga", "tipo": "semiacida"},
    4: {"nome": "maçã", "tipo": "semiacida"},
    5: {"nome": "banana", "tipo": "doce"},
    6: {"nome": "mamão", "tipo": "doce"}
})

print("chave 1  nome: ", dicionario_frutas[1]["nome"], " tipo:", dicionario_frutas[1]["tipo"])
print("chave 2  nome: ", dicionario_frutas[2]["nome"], " tipo:", dicionario_frutas[2]["tipo"])

for chave, valor in dicionario_frutas.items():
    print(f"chave: {chave} - nome: {valor["nome"]} - tipo: {valor["tipo"]}")