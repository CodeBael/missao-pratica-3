set_iinicial = {11,12,13,14}
print(set_iinicial)

set_iinicial.add(15)
print(set_iinicial)

set_iinicial.update({1,2,3,4,5})
print(set_iinicial)

set_iinicial.discard(13)
print(set_iinicial)

novo_set = set([20,21,23, 1, 2])
print(novo_set)

uniao = set_iinicial.union(novo_set)
print(uniao)

intercesao = set_iinicial.intersection(novo_set)
print(novo_set)

diference = set_iinicial.difference(novo_set)
print(novo_set)

diference_simetrica = set_iinicial.symmetric_difference(novo_set)
print(novo_set)